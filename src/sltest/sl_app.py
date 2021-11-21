'''
Created on Nov 20, 2021

@author: immanueltrummer
'''
import streamlit as st

st.header('Hello!')
if st.button('Balloons?'):
    st.balloons()

import firebase_admin
from firebase_admin import credentials

import firebase_admin

cred = credentials.Certificate