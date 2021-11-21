'''
Created on Nov 20, 2021

@author: immanueltrummer
'''
import google.cloud.firestore
import openai
import streamlit as st

fb_creds = {k:v for k, v in st.secrets['firebase'].items()}
ai_creds = st.secrets['openai']

db = google.cloud.firestore.Client.from_service_account_info(fb_creds)
docs = db.collection('conversations')
openai.api_key = ai_creds

try:
    response = openai.Completion.create(
        engine='davinci-codex', prompt='Q: What is a recoverable schedule? A:', 
        temperature=0, max_tokens=50, stop='Q:')
    print(response['choices'][0]['text'])
except Exception as e:
    print(f'Error querying Codex: {e}')

print(f'Documents: {docs}')
for doc in docs.stream():
    print(doc.to_dict())

st.header('Hello!')
if st.button('Balloons?'):
    st.balloons()
