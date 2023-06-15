import streamlit as st
import pandas as pd
import random
from PIL import Image
from streamlit.components.v1 import html
from streamlit_image_select import image_select
import time

im= Image.open(r'Iimg.png')
st.set_page_config(
        page_title="IL-IRDAI PoC",
        page_icon = im,
)



hide_menu_style = """
        <style>
        css-pxxe24 {visibility: hidden;}
        #MainMenu {visibility: hidden; }
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)



st.header('Third Party Insurance Check and Challan System')
tech_type = st.selectbox('Select Type' , ('Using FASTag' , 'Using Computer Vision'))

if tech_type == 'Using FASTag':
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
                  st.info('Disclaimer: All Vehicle No, Insurance Company, Panelty, TP Insurance Price are only sample values, they might not be real.')


if tech_type == 'Using Computer Vision':
    
    file = pd.read_excel('SampleFastTagData.xlsx' , sheet_name='NonFastTag')
    if 'stage' not in st.session_state:
        st.session_state.stage = 0

    def set_stage(stage):
        st.session_state.stage = stage


    image1 = Image.open('bikevrn1.jpg')
    image2 = Image.open('bikevrn2.jpg')
    image3 = Image.open('bikevrn3.jpg')
    image4 = Image.open('bikevrn4.jpg')


    img = image_select(
        label="Select a Number",
        images=[ image1, image2, image3 ,image4],use_container_width=False,return_value="index")

    vrn = file['Motor Registration Number'][img]

    col1 = st.columns(3)

    with st.spinner('Reading VRN from Image'):
        time.sleep(3)

    
    file1 = file[file['Motor Registration Number']==vrn]
    st.info('VRN from Image')
    col2= st.columns(3)
    col2[1].subheader(f'VRN-{vrn}')

    with st.spinner('Getting Vehicle and Insurance Details'):
        time.sleep(3)
    st.info('Vehicle and Insurance Details')
    st.write(file1[['Model Name' , 'Insurance Company','Policy Start','Policy End', 'Policy Type' , 'Status']].reset_index(drop = True) , )
    
    with st.spinner('Checking TP Status'):
        time.sleep(3)

    if file1['Status'].values[0]!='Expired':
        st.info('TP Status')
        st.subheader('No action required with respect to TP insurance!')
    else:
        st.info('TP Status')
        st.subheader(f'VRN -{vrn} has been alloted Third Party Insurance worth Rs { file1["TP Charges"].values[0]} and Penalty of Rs 500')




