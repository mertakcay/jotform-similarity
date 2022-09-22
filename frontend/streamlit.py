import streamlit as st
import requests
import subprocess
import json
import pandas as pd 
import numpy as np
st.set_page_config(page_title="Jotform Text Search",page_icon="../frontend/jotform-icon-dark-400x400.png")

st.markdown("# Jotform - Form Similarity Search")
inputText = st.text_input("Form ID")
formCount = st.slider("Similar Form Count",1,10)

if st.button("Search Form"):
    #print(inputText)
    #print(formCount)

    myobj = {f"formId":{inputText},
            "formCount":{formCount}
            }
    x = requests.get("http://127.0.0.1:8000/similar", params = myobj)


    if(x.status_code == 200):
        x = json.loads(x.text)
        forms = x['forms'].replace("[","").replace("]","").replace(" ","").split(",")
        distances = x['distances'].replace("[","").replace("]","").replace(" ","").split(",")
        print(forms)
        print(distances)
        
        
        #print(type(forms))
        # print(x['distances'])
        # print(len(x['distances']))
        # print("Type: ",type(x))
        st.markdown(f"## Most Similar Forms")
        col1, col2, col3,col4,col5 = st.columns(5)
        with col1:
            st.header("Rank")
            
        with col2:
            st.header(f" General Content")
            
        with col3:
            st.header(f" Form Distances")
           
        with col4:
            st.header(f" Form Questions")
            
        with col5:
            st.header(f" Form Properties")
            
        for i in range(len(forms)):
            with col1:
                st.write(i)
            with col2:
                st.write(f"[{forms[i]}](https://api.jotform.com/form/{forms[i]}?apiKey=06c38963c5de8d06c64b64c8fa9f31a8)")
            with col3:
                st.write(f"{round(float(distances[i]),4)}")
            with col4:
                st.write(f"[{forms[i]}](https://api.jotform.com/form/{forms[i]}/questions?apiKey=06c38963c5de8d06c64b64c8fa9f31a8)")
            with col5:
                st.write(f"[{forms[i]}](https://api.jotform.com/form/{forms[i]}/properties?apiKey=06c38963c5de8d06c64b64c8fa9f31a8)")
                


    else:
        st.warning(f"Unexpected Status Code: {x.status_code}")
    




