import streamlit as st
import requests
from datetime import datetime
import os

####################
### Useful functions
####################

### get files in directory
def GetFiles(useDir):

    print("Working in:", useDir)
    
    # get files in directory
    file_types=[".png",".jpg",".jpeg"]
    fileList=sorted([useDir+f for f in os.listdir(useDir) if any([True for x in file_types if x in f.lower()]) ] )
    print("- files found:", len(fileList))
    
    return fileList


####################
### Main part
####################

# title etc.
st.title("Uploaded Files")

# get files if not defined
if "file_list" not in st.session_state.keys() or st.button("check gallery"):
    useDir=os.getcwd()+"/pages/gallery/"
    st.session_state['file_list']=GetFiles(useDir)
    st.write(f"Got {len(st.session_state['file_list'])} files.")


file_list=st.session_state['file_list']

# latest
st.write(f"## Latest News")
st.image(file_list[0], caption=file_list[0].split('/')[-1])

# history
st.write(f"## Old updates")
for of in file_list[1::]:
    st.write(f"{of}")




