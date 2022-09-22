#api dependancy
from fastapi import FastAPI ,HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import json
import pandas as pd
import numpy as np

#model dependancy
from sentence_transformers import SentenceTransformer, util
import faiss
from model import formModel

#function dependancy
from utils import getInformation,get_language,all_preprocessing_stages, remove_stopwords, to_df
import os
import csv
import sys
from dotenv import load_dotenv
load_dotenv()
csv.field_size_limit(sys.maxsize)


app = FastAPI()
index = None
embedder = None

@app.on_event("startup")
async def startup_event():
  global index
  global embedder
  
  
  try:
    index = faiss.read_index("../app/indexer/paraphrase-multilingual-MiniLM-L12-v2-index-faiss") 
  except:
    print("Index is not initalized")
    raise HTTPException(status_code=404, detail="Index is not initalized")    
  try:
    embedder = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2') 
  except:
    print("Embedder is not initalized")
    raise HTTPException(status_code=404, detail="Embedder is not initalized")  


@app.get("/similar",tags=["form"])
def get_similarform(formId:int,formCount:int):
  global index
  global embedder
  
    
  rawData = getInformation(formId) 
  text = all_preprocessing_stages(rawData['Raw_Text'])
  pagetitle = all_preprocessing_stages(rawData['Page_Title'])
  language = get_language(text)
  text = remove_stopwords(text)
  text = text.lower()
  
  text = pagetitle+". "+ text
  if(text != "form" and text != "Form"):
    
    if(len(text.split(" ")) > int(os.getenv('EMBEDDING_DIM'))):
      text = " ".join(text.split(" ")[:int(os.getenv('EMBEDDING_DIM'))])
      
    xq = embedder.encode([text])  
    D,I = index.search(xq,formCount)    
    print(type(I[0].tolist()[0]))
    
    # returnData = formModel(SimilarForm=I[0].tolist(),
    #                        Probability=D[0].tolist())
    data = {
      "forms":f"{I[0].tolist()}",
      "distances":f"{D[0].tolist()}"
    }
    # print(data)
    # return json.dumps(data) #I[0].tolist()
    
    return data
    
    
    
  else:  
    raise HTTPException(status_code=404, detail="Not have sufficient information to recommended form")
    


