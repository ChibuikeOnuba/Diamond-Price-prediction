import streamlit as st
from PIL import Image

    
def main():
    st.title('About Me')
    col1, col2 = st.columns(2)
    #image = Image.open(r"C:\Users\HP\Documents\ML Projects\Diamond Price prediction\pages\my_picture.jpg")
    #ol1.image(image, width=225)
    col1.image('pages/my_picture.jpg')
    
    col2.write('I am a Data Scientist with passion for building ML solutions and making visuals to analyze business insights.') 
               
    col2.write('I am a final year studying Computer Science major at the University of Nigeria')
    col2.write('Feel free to go through my projects and contact me for collaborations :)')
    
    
    
    
    expander = st.expander("check out my other projects")
    expander.selectbox(label='select', options=['Diabetes Prediction', 'Covid 19 prediction', 'Iris Classification', 'Customer Segmentation'])  
    st.write('Visit my personal website')
    if st.button("Visit Portfolio"):
    # Replace 'https://chibuikeonuba/github.io' with the URL you want to visit
        st.markdown(
            f'<a href="https://chibuikeonuba.github.io" target="_blank">Portfolio Site</a>',
            unsafe_allow_html=True
        )

if __name__ == '__main__':
    main()
