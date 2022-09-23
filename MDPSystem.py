# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 18:06:57 2022

@author: Akshay
"""

import streamlit as st
import pickle

loading = pickle.load(open("C:/Users/pushp/Desktop/MDPSystem/Diabetes_pred.sav","rb"))
heart_model = pickle.load(open("C:/Users/pushp/Desktop/MDPSystem/Heart_pred.sav","rb"))
par_model = pickle.load(open("C:/Users/pushp/Desktop/MDPSystem/Parkinsons_pred.sav","rb"))


st.title("Multiple Disease Prediction System")

st.image("C:/Users/pushp/Desktop/MDPSystem/multiimage.png")


menu = st.sidebar.selectbox("Multiple Disease Prediction System", ["Diabetes Prediction","Heart Disease Prediction","Parkinsons Prediction","BMI Calculator"])
if (menu == "Diabetes Prediction" ):
    # page title
    st.title("Diabetes Prediction")

    Pregnancies = st.selectbox("Pregnancies(Weeks)", sorted([ 6,  1,  8,  0,  5,  3, 10,  2,  4,  7,  9, 11, 13, 15, 17, 12, 14]))
    Glucose = st.number_input("Glucose")
    BloodPressure = st.number_input("BloodPressure")
    SkinThickness = st.number_input("SkinThickness")
    Insulin = st.number_input("Insulin")
    BMI = st.number_input("BMI")
    DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function')
    Age = st.number_input("Age")
    
    # code for Prediction
    Diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test'):
        Diabetes_prediction = loading.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (Diabetes_prediction[0] == 1):
           Diagnosis = 'The person is diabetic'
        else:
           Diagnosis = 'The person is not diabetic'
        
    st.success( Diagnosis)

# =============================================================================
# 
# =============================================================================


if (menu == "Heart Disease Prediction"):

    st.title("Heart Disease Prediction")
    
    age = st.text_input('Age')
    
    sex = st.selectbox('Sex  (Male - 1 , Female - 0)',[1,0])

    cp = st.text_input('Chest Pain types')
    
    trestbps = st.text_input('Resting Blood Pressure')
    
    chol = st.text_input('Serum Cholestoral in mg/dl')
    
    fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)',[0,1])
    
    restecg = st.text_input('Resting Electrocardiographic results')
    
    thalach = st.text_input('Maximum Heart Rate achieved')
    
    exang = st.selectbox('Exercise Induced Angina (1 = yes; 0 = no)',[0,1])
    
    oldpeak = st.text_input('ST depression induced by exercise')
    
    slope = st.text_input('Slope of the peak exercise ST segment')
    
    ca = st.text_input('Major vessels colored by flourosopy')
    
    thal = st.selectbox('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',[0,1,2])
    
    
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'
        
    st.success(heart_diagnosis)
        
    
    
    
    
# =============================================================================
#     
#     
# =============================================================================
if (menu == "Parkinsons Prediction"):

    st.title("Parkinsons Prediction")
    
    fo = st.text_input('MDVP:Fo(Hz)')
    
    fhi = st.text_input('MDVP:Fhi(Hz)')
    
    flo = st.text_input('MDVP:Flo(Hz)')
    
    Jitter_percent = st.text_input('MDVP:Jitter(%)')
    
    Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    
    RAP = st.text_input('MDVP:RAP')
    
    PPQ = st.text_input('MDVP:PPQ')
    
    DDP = st.text_input('Jitter:DDP')
    
    Shimmer = st.text_input('MDVP:Shimmer')
    
    Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    
    APQ3 = st.text_input('Shimmer:APQ3')
    
    APQ5 = st.text_input('Shimmer:APQ5')
    
    APQ = st.text_input('MDVP:APQ')
    
    DDA = st.text_input('Shimmer:DDA')
    
    NHR = st.text_input('NHR')
    
    HNR = st.text_input('HNR')
    
    RPDE = st.text_input('RPDE')
    
    DFA = st.text_input('DFA')
    
    spread1 = st.text_input('spread1')
    
    spread2 = st.text_input('spread2')
    
    D2 = st.text_input('D2')
    
    PPE = st.text_input('PPE')
    

    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = par_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        
    st.success(parkinsons_diagnosis)

# =============================================================================
# 
# =============================================================================

if (menu == "BMI Calculator"):
    weight = st.number_input("Weight (Kg)")
    height = st.number_input("height (cm)")
    
    if st.button("Calculate"):
        
        bmi = (weight / (height * height)) * 10000
    
        st.success(bmi)





# =============================================================================
# 
# =============================================================================

rad = st.sidebar.radio("Navigation",["Home","About us","Contact us","Help"])

if rad == "Home":
    st.write("Thanks for using this .....")

elif rad == "About us":
    
    about = st.selectbox("About Dataset and developer",["Dataset Source","About Developer"])
    if about == "Dataset Source":
        st.write("Training Datasets has been taken from Kaggle and their link is given below")
        st.write("""Diabetes Dataset - https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database """)
        st.write("Heart Disease Dataset - https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset ")
        st.write(' Parkinsons Data Set - https://www.kaggle.com/datasets/nidaguler/parkinsons-data-set')
        st.write("For read and download code plz visite my github link \n https://github.com/LalitMahale/Multiple-Disease-Prediction-System.git")
        
    else:
        st.write("""Hi, we Akshay & Aishwarya, have done our Post Graduate Diploma in Big Data Analytics from CDAC (act's) Chennai """)
    
elif rad == "Contact us":
    st.write("Email:- golharakshay9@gmail.com" , "Email:- aishwaryapituk@gmail.com ")
    
else:
    
    helps = st.selectbox("Help about Data information",["Diabetes Prediction","Heart Disease Prediction","Parkinsons Prediction"])
    
    if helps == "Diabetes Prediction":
            st.write('''Pregnancies : - Number of times pregnant ''')
            st.write('fasting blood sugar :- ( 120 mg/dl) (1 = true; 0 = false)')
            st.write('BloodPressure :- Diastolic blood pressure (mm Hg)')
            st.write('SkinThickness :- Triceps skin fold thickness (mm)')
            st.write('Insulin :- 2-Hour serum insulin (mu U/ml)')
            st.write('BMI :- Body mass index')    
            st.write('Diabetes Pedigree Function :-  Diabetes pedigree function')

    if helps == "Heart Disease Prediction":
            st.write('''resting blood pressure :-  in mm Hg on admission to the hospital  ''')
            st.write(''' chest pain type (4 values) ''')         
            st.write(''' chest pain type (4 values) ''')         
            st.write(''' fasting blood sugar > 120 mg/dl ''')         
            st.write(''' resting electrocardiographic results (values 0,1,2)''')         
            st.write(''' oldpeak = ST depression induced by exercise relative to rest ''')         
            st.write(''' the slope of the peak exercise ST segment ''')         
            st.write(''' number of major vessels (0-3) colored by flourosopy ''')         
            st.write(''' thal: 0 = normal; 1 = fixed defect; 2 = reversable defect ''')         


                
                
    if helps == "Parkinsons Prediction":
            st.write('''MDVP:Fo(Hz) - Average vocal fundamental frequency''')
            st.write('''MDVP:Fhi(Hz) - Maximum vocal fundamental frequency ''')
            st.write('''MDVP:Fhi(Hz) - Maximum vocal fundamental frequency''')
            st.write('''MDVP:Jitter(%),MDVP:Jitter(Abs),MDVP:RAP,MDVP:PPQ,Jitter:DDP - Several measures of variation in fundamental frequency''')
            st.write('''MDVP:Shimmer,MDVP:Shimmer(dB),Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ,Shimmer:DDA - Several measures of variation in amplitude ''')
            st.write('''NHR,HNR - Two measures of ratio of noise to tonal components in the voice''')
            st.write('''status - Health status of the subject (one) - Parkinson's, (zero) - healthy ''')
            st.write('''RPDE,D2 - Two nonlinear dynamical complexity measures''')
            st.write('''DFA - Signal fractal scaling exponent''')
            st.write('''spread1,spread2,PPE - Three nonlinear measures of fundamental frequency variation''')

