import streamlit as st

st.set_page_config(layout="wide")

def layout_custom():
    st.markdown(
        """
        <style>
            .sidebar-content {
                font-family: 'Titillium Web', sans-serif !important;
                color: white;
                margin-left: 0px;
                margin-top: 0px;
                font-size: 40px;
                position: relative;
                top: -20px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    with st.sidebar:
        st.markdown('<div class="sidebar-content">LIGHTHOUSE</div>', unsafe_allow_html=True)
        st.page_link("main.py", label = "Business Understanding", icon = "🏠")
        st.page_link("pages/page_1.py", label = "Data Understanding",icon="📊")
        st.page_link("pages/page_2.py", label = "Data Preparation", icon="🧹")
        st.page_link("pages/page_3.py", label = "Modeling", icon = "🤖")
      
    with open("assets/style.css") as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

    st.logo("imgs/6688614a727076417d4ca74c_Group 743.png", size = "large",)


    