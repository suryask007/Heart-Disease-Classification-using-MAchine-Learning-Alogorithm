import numpy as np
import pickle
import streamlit as st

#input_data=(52,1,0,125,212,0,1,168,0,1.0,2,2,3)
#loading the saved model
loaded_model=pickle.load(open('model_path','rb'))

#creating a function for prediction
def heart_disease_classification(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
        return "Person don't have heart disease"
    else:
         return "Person have heart disease"
     
        
def main():
    st.title("Heart Disease Prediction Web App")
        
    age = st.text_input('Age')
    sex = st.text_input('Sex')
    cp = st.text_input('Chest Pain Type')
    trestbps = st.text_input('Resting Blood Pressure in mm')
    chol = st.text_input('serum cholesterol in mg/dl')
    fbs = st.text_input('fasting blood sugar > 120 mg/dl (1=true; 0=false)')
    restecg = st.text_input('resting electrocardiographic results')
    thalach = st.text_input('maximum heart rate achieved')
    exang = st.text_input('exercise-induced angina')
    oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    slope = st.text_input('the slope of the peak exercise ST segment')
    ca = st.text_input('number of major vessels (0–3) colored by fluorosopy')
    thal = st.text_input('thalassemia')
    
    #code for prediction
    
    diagnosis = ''
    
    #creating a button for prediction
    if st.button('Result'):
        diagnosis = heart_disease_classification([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal])
        
    st.success(diagnosis)
    
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    