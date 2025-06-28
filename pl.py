# -*- coding: utf-8 -*-
"""
Created on Wed Jun 25 17:21:37 2025

@author: admin
"""

import numpy as np
import pickle
import streamlit as st

loaded_model=pickle.load(open('C:/Users/admin/Newfolder/placemnt.sav','rb'))

def salary_prediction(input_data):
    
    input_data_as_numpy_array=np.asarray(input_data)
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    #print(prediction)
    return prediction[0]
      
def main():
    
    st.title('💲 Salary Prediction Web App')
    
    col1,col2,col3=st.columns(3)

    with col1:
        ssc_p = st.text_input('SSC Percentage')
    
    with col2:
        hsc_p = st.text_input('HSC Percentage')

    with col3:
        deg_p = st.text_input('Degree Percentage')
    
    with col1:
        etest_p = st.number_input('Etest Percentage')

    with col2:
        mba_p = st.text_input('MBA Pecentage')

    with col1:
        ssc_b = st.selectbox('SSC Board',['Others','Central'])
        scb={
          'Others':0,
          'Central':1
        }
        sb = scb[ssc_b]
  
    with col2:
        hsc_b = st.selectbox('HSC Board',['Others','Central'])
        hcb={
          'Others':0,
          'Central':1
        }
        hb = hcb[hsc_b]

    with col3:
        hsc_s = st.selectbox('HSC Stream',['Commerce','Science','Arts'])
        hcs={
            'Commerce':0,
            'Science':1,
            'Arts':2
        }
        hs = hcs[hsc_s]

    with col1:
        gender = st.selectbox('Gender',['M','F'])
        gn={
          'M':0,
          'F':1
        }
        gnd = gn[gender]
  
    with col2:
        deg_t = st.selectbox('Degree T',['Comm&Mgmt','Sci&Tech','Others'])
        dgt={
          'Comm&Mgmt':0,
          'Sci&Tech':1,
          'Others':2
        }
        dt = dgt[deg_t]

    with col3:
        specialisation = st.selectbox('Specialisation',['Mkt&Fin','Mkt&HR'])
        spc={
            'Mkt&Fin':0,
            'Mkt&HR':1
        }
        sp = spc[specialisation]


    with col1:
        work_exp = st.selectbox('Work Experience',['No','Yes'])
        wex={
          'No':0,
          'Yes':1
        }
        we = wex[work_exp]
  
    with col2:
        status = st.selectbox('Placement Status',['Not Placed','Placed'])
        plcmnt_status={
          'Not Placed':0,
          'Placed':1
        }
        sts = plcmnt_status[status]

    
    
    diagnosis=''
    
    if st.button('Salary'):
        diagnosis = salary_prediction([float(ssc_p),float(hsc_p),float(deg_p),float(etest_p),float(mba_p),float(sb),float(hb),float(hs),float(gnd),float(dt),float(sp),float(we),float(sts)])

        
    st.success(diagnosis)
    
main()