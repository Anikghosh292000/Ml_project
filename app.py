import streamlit as st
import pickle

st.title('MPG ML PROJECT')

displacement =st.number_input('displacement' , value = 300 , placeholder = 'enter a value of displacement')
hoursepower =st.number_input('hoursePower' , value = 130 , placeholder = 'enter a value of horsepower')
weight =st.number_input('weight' , value = 3000 , placeholder = 'enter a value of weight')
acceleration =st.number_input('acceleration' , value = 12 , placeholder = 'enter a value of acceleration')

loaded_model =pickle.load(open('mpg_regression.sav','rb'))
prediction =loaded_model.predict([[displacement,hoursepower,weight,acceleration]])

st.subheader(f' predicted mpg value for above parameter is{prediction}')
st.write(prediction)