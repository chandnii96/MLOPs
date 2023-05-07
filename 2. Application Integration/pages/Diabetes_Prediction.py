import streamlit as st
import numpy as np
from pickle import load
import os
import pickle
from sklearn.preprocessing import StandardScaler



#absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
#absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
#absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "models")
best_model=os.path.join(dir_of_interest,"standard_scaler.pkl")
scaler= load(open(best_model, 'rb'))

best_model2=os.path.join(dir_of_interest,"sv_model.pkl")
sv_model= load(open(best_model2,'rb'))

st.title('Diabetes Prediction ')
st.subheader(':green[Enter your Values to check Diabetes:]c')


#Background Image
img = '''
<style>
.stApp {
background-image: url("https://tse3.mm.bing.net/th?id=OIP.FYBpfrf1SnBsblDl9-GVqgHaEc&pid=Api&P=0");
background-size: cover;
background-position: top center;
background-repeat: no-repeat;
background-attachment: local;
background-blur;
}
</style>
'''

st.markdown(img, unsafe_allow_html=True)


Age=st.text_input("Age", placeholder="Enter Age")
BMI=st.text_input("BMI", placeholder="Enter BMI")
Glucose= st.text_input("Glucose", placeholder="Enter Glucose")
BP = st.text_input("Blood Pressure", placeholder="Enter Blood Pressure")
ST = st.text_input("Skin Thickness", placeholder="Enter Skin Thickness")
Insulin= st.text_input("Insulin", placeholder="Enter Insulin")
DPF=st.text_input("Diabetes Pedigree Function", placeholder="Enter Diabetes Pedigree Function")
Pregnancies = st.text_input("Pregnancies", placeholder="Enter Number of Pregnancies")


btn_click = st.button("Predict")

if btn_click == True:
    if  Pregnancies and Glucose and BP and ST and Insulin and BMI and DPF and Age:
        input_data_as_numpy_array = np.asarray([int(Pregnancies), float(Glucose), float(BP),  float(ST),float(Insulin),float(BMI),float(DPF), int(Age)])
        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

        # standardize the input data
        std_data = scaler.transform(input_data_reshaped)

        prediction =sv_model.predict(std_data)
        print(prediction)

        if (prediction[0] == 0):
            print('The person is not diabetic')
        else:
             print('The person is diabetic')
    
    else:
        st.error("Enter the values properly.")