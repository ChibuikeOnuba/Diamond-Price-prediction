
import pandas as pd
import streamlit as st
import pickle

pickle_in = open('regressor.pkl', 'rb')
regressor = pickle.load(pickle_in)

with open('xgboost.pkl', 'rb') as file:
    # Load the model from the pickle file
    xgboost = pickle.load(file)

@st.cache_data

def predit(carat, cut, color, clarity, depth, table, x, y, z):
    
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
        
    #making the prediction
    entries = [[carat, cut, color, clarity, depth, table, x, y, z]]

    prediction = regressor.predict(entries)
    return prediction


def classify(carat, color, clarity, depth, table, price, x, y, z):
  
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
        
    #making the prediction
    entries = [[carat, color, clarity, depth, table, price, x, y, z]]

    cluster = xgboost.predict(entries)
    return cluster

selection = st.sidebar.selectbox('Predict', ['Price', 'Rating'])

 
def main():
    st.title('DIAMOND PRICE & RATING PREDICTION APP💎')
    st.header('Predict {}'.format(selection))
    
    
    st.write("""
         ### Enter features of the diamond
    """)
    st.write()
    
    
    #Defining the user inputs
    col1, col2 = st.columns(2)
    
    if selection ==  'Price':
        cut = col1.selectbox('Rating of the diamond', ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal'])
    else:
        price = st.slider('Price of the diamond: ', min_value=10, value=200, step=200, max_value=20000)
        
    carat = col2.number_input('Weight of the diamond: ', min_value=0.1, max_value=5.0, value=1.0, step=0.1)    
    color = col1.selectbox('Color rating', ['J', 'I', 'H', 'G', 'F', 'E', 'D'])
    clarity = col1.selectbox('Clarity rating', ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF'])
    depth = col1.number_input('Diamond depth percentage', min_value=10, max_value=100, step=10)
    table = col1.number_input('Diamond table percentage', min_value=10, max_value=100, step=10)
  
    x = col2.slider('Diamond length(X-cm)', min_value=2.0, max_value=10.0, step=1.0)
    y = col2.slider('Diamond Width(Y-cm)', min_value=2.0, max_value=10.0, step=1.0)
    z = col2.slider('Diamond height(Z-cm)', min_value=1.0, max_value=10.0, step=0.5)

    #creating the Predict button
    if selection == 'Price':
        if st.button('Predict Price'):
            price = predit(carat, cut, color, clarity, depth, table, x, y, z)
            st.success('The estimated price of the diamond is ${} USD'.format(price.round(-1)))
    
    else:
        if st.button('Predict Rating'):
            cut = classify(carat, color, clarity, depth, table, price, x, y, z)
            if cut == 2.0:
                prediction = 'Ideal🎇'
            elif cut == 3.0:
                prediction = 'Premium💎'
            elif cut == 1.0:
                prediction = 'Good😙'
            elif cut == 4.0:
                prediction = 'Very Good😍'
            else:
                prediction = 'Fair🙂'
            st.success('Your diamond is graded {} '.format(prediction.upper()), icon='✔')

        
                

if __name__=='__main__':
    main()