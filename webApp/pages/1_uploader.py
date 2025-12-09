import streamlit as st
import requests
from datetime import datetime

# title etc.
st.title("File Upload")

# upload check
do_upload=False

# upload file
uploaded_file = st.file_uploader("Input file", type=['png','jpg','jpeg'])

# if uploaded show image and get comment
if uploaded_file is not None:

    # show image
    st.image(uploaded_file, caption="Uploaded image")
    # get comment (y/n)
    comment=st.radio("Is it open?",['Yes','No']) 
    # ready for upload
    do_upload=True

else:
    st.write("Please add file.")

# upload option when ready
if do_upload:

    # where to go
    destination_url = 'https://cernbox.cern.ch/s/WlFpUqiA71ChjNs'
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # construct name with meta data
    # data first for ordering, then comment, then original name
    file_name_edit= datetime.today().strftime("%Y_%m_%d")+"_"+comment+"_"+uploaded_file.name

    # announce ready with button
    st.info("Ready for upload")
    st.write(f"file will be named: {file_name_edit}")
    if st.button("Do upload"):
        files = {'file': (file_name_edit, bytes_data)}  # Specify the file you want to upload
        response = requests.post(destination_url, files=files)
        # show response
        st.write(response)