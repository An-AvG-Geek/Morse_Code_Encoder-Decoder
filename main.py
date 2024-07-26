from morse_talk import *
import streamlit as st
from streamlit_option_menu import option_menu

def main():
    st.set_page_config(page_title="Code Converter", page_icon="./-")
    with st.sidebar:
        choice=option_menu(menu_title="Code Converter",options=["Morse Code","Binary Code"])

        if choice=="Morse Code":
            st.title("Morse Code Converter")
            option=option_menu(menu_title=None,options=["Encoder","Decoder"],orientation="horizontal")
            

        elif choice=="Binary Code":
            pass








if __name__=="__main__":
    main()
