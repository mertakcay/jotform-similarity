import streamlit as st
import requests
import subprocess
import json
import pandas as pd 
import numpy as np
import ast
st.set_page_config(page_title="Jotform Form Similarity App",page_icon="../frontend/jotform-icon-dark-400x400.png")

st.markdown("# Jotform - Form Similarity Search")
inputText = st.text_input("Form ID")
formCount = st.slider("Similar Form Count",1,10)

if st.button("Search Form"):
    myobj = {f"formId":{inputText},
            "formCount":{formCount}
            }
    x = requests.get("http://127.0.0.1:8000/similar", params = myobj)
    if(x.status_code == 200):
        
        x = json.loads(x.text)
        x = ast.literal_eval(x)
        st.header("Most Similar Form Informations")
        for i in range(int(formCount)):
            temp = ast.literal_eval(x[i])
            st.subheader(f"General Information Of [{temp['form_id']}](https://api.jotform.com/form/{temp['form_id']}?apiKey=06c38963c5de8d06c64b64c8fa9f31a8)")
            st.json(temp)
    
    
    else:
        st.warning(f"Unexpected Status Code: {x.status_code}")
    




