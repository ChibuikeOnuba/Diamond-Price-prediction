import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression 

model = LinearRegression()
model.load_model('regressor_param.txt')

def predict(carat, cut, color, clarity, depth, table, x, y, z):
    
    if cut == 'Ideal':
        cut = 2.0
    elif cut == 'Premium':
        cut = 3.0
    elif cut == 'Good':
        cut = 1.0
    elif cut == 'Very Good':
        cut = 4.0
    else:
        cut = 0.0
        
        
    if color == 'J':
            color = 0
    elif color == 'I':
        color = 1
    elif color == 'H':
        color = 2
    elif color == 'G':
        color = 3
    elif color == 'F':
        color = 4
    elif color == 'E':
        color = 5
    elif color == 'D':
        color = 6
    
    if clarity == 'I1':
        clarity = 0
    elif clarity == 'SI2':
        clarity = 1
    elif clarity == 'SI1':
        clarity = 2
    elif clarity == 'VS2':
        clarity = 3
    elif clarity == 'VS1':
        clarity = 4
    elif clarity == 'VVS2':
        clarity = 5
    elif clarity == 'VVS1':
        clarity = 6
    elif clarity == 'IF':
        clarity = 7
        
    entries = pd.DataFrame([[carat, cut, color, clarity, depth, table, x, y, z]], columns=['carat', 'cut', 'color', 'clarity', 'depth', 'table', 'x', 'y', 'z']) 

    prediction = model.predict(entries)
    return prediction


st.title('DIAMOND PRICE PREDICTOR')
st.header('Enter the features of the diamond')

#Defining the user inputs
carat = st.number_input('Weight of the diamond: ', min_value=0.1, max_value=10.0, value=1.0)
cut = st.selectbox('Rating of the diamond', ['Fiar', 'Good', 'Very Good', 'Premium', 'Ideal'])
color = st.selectbox('Color rating', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
clarity = st.selectbox('Clarity rating', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
depth = st.number_input('Diamond depth percentage', min_value=0.1, max_value=100.0, value=1.0)
table = st.number_input('Diamond table percentage', min_value=0.1, max_value=100.0, value=1.0)
x = st.number_input('Diamond length(X)', min_value=0.1, max_value=100.0, value=1.0)
y = st.number_input('Diamond width(Y)', min_value=0.1, max_value=100.0, value=1.0)
z = st.number_input('Diamond height(Z)', min_value=0.1, max_value=100.0, value=1.0)

#creating the input button

if st.button('Predict'):
    price = predict(carat, cut, color, clarity, depth, table, x, y, z)
    st.success('The price of the diamond is {} USD'.format(price))
