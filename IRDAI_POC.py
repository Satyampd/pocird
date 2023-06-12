import streamlit as st
import pandas as pd
import random
from PIL import Image


im = Image.open(r'Iimg.png')

st.set_page_config(
        page_title="IL-IRDAI POC",
        page_icon = im,
)


st.header('Third Party Insurance Check and Challan System')
tech_type = st.selectbox('Select Type' , ('Using FastTag' , 'using Computer Vision'))

if tech_type == 'Using FastTag':
    file = pd.read_excel('SampleFastTagData.xlsx' , sheet_name='FastTag')

    if 'stage' not in st.session_state:
        st.session_state.stage = 0

    def set_stage(stage):
        st.session_state.stage = stage


    v_rno = st.radio('Sample VRN' , ('01', '02' ), horizontal=True)
    if v_rno== '01':
        idx = 1
    else:
        idx = 0

    vrn = file['Motor Registration Number'][idx]
    col1 = st.columns(3)
    col1[1].button('Get Vehicle Details', on_click=set_stage, args=(1,))
    if st.session_state.stage > 0:    
        
        
        file1 = file[file['Motor Registration Number']==vrn]
        col2= st.columns(3)
        col2[1].subheader(f'VRN-{vrn}')

        st.table(file1[['Motor Manufacturer Year','Motor Manufacturer Name','Model Name']].reset_index(drop = True))
        
        col3= st.columns(3)
        col3[1].button('Get Insurance Details', on_click=set_stage, args=(2,))
        if st.session_state.stage > 1:
            st.table(file1[['Insurance Company','Policy Start Date','Policy End Date', 'Policy Type' , 'Status']].reset_index(drop = True))

            if file1['Status'].values[0]!='Expired':
                st.subheader('No action required with respect to TP insurance!')

            else:
                
#                 col4= st.columns(3)
#                 col4[1].button('Allot TP Insurance', on_click=set_stage, args=(3,))
#                 if st.session_state.stage > 2:
                  st.subheader(f'VRN -{vrn} has been alloted Third Party Insurance worth Rs { file1["TP Charges"].values[0]} and Penalty of Rs 500')


if tech_type == 'Using Computer Vision':
    
    file = pd.read_excel('SampleFastTagData.xlsx' , sheet_name='NonFastTag')
    if 'stage' not in st.session_state:
        st.session_state.stage = 0

    def set_stage(stage):
        st.session_state.stage = stage


    v_rno = st.radio('Sample VRN' , ('01', '02' ), horizontal=True)
    if v_rno== '01':
        idx = 1
    else:
        idx = 0

    if idx == 1:
        image = Image.open('bikevrn1.jpg')
    else: 
        image = Image.open('bikevrn2.jpg')
    
    
    col_img = st.columns(3)
    col_img[1].image(image)
    vrn = file['Motor Registration Number'][idx]

    col1 = st.columns(3)
    col1[1].button('Get Vehicle Details using OCR', on_click=set_stage, args=(1,))
    if st.session_state.stage > 0:    
        
        
        file1 = file[file['Motor Registration Number']==vrn]
        col2= st.columns(3)
        col2[1].subheader(f'VRN-{vrn}')

        st.table(file1[['Motor Manufacturer Year','Motor Manufacturer Name','Model Name']].reset_index(drop = True))
        
        col3= st.columns(3)
        col3[1].button('Get Insurance Details', on_click=set_stage, args=(2,))
        if st.session_state.stage > 1:
            st.table(file1[['Insurance Company','Policy Start Date','Policy End Date', 'Policy Type' , 'Status']].reset_index(drop = True))

            if file1['Status'].values[0]!='Expired':
                st.subheader('No action required with respect to TP insurance!')

            else:
                
#                 col4= st.columns(3)
#                 col4[1].button('Allot TP Insurance', on_click=set_stage, args=(3,))
#                 if st.session_state.stage > 2:
                  st.subheader(f'VRN -{vrn} has been alloted Third Party Insurance worth Rs { file1["TP Charges"].values[0]} and Penalty of Rs 500')




