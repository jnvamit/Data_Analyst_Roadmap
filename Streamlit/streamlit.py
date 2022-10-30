import streamlit as st

def streamlit_intro():
    """function is basic intro to streamlit"""
    
    st.title('Hello Streamlit')

def streamlit_text():
    """function represents texual data usage in streamlit"""
    st.title('Hello Streamlit')
    st.header('Header')
    st.subheader('Sub Header')
    st.markdown("""
                    # h1
                    ## h2
                    ### h3
                    :moon:<br>
                    :sunglasses:
                    **bold**
                    _italic_
                """,True)
    st.write('# Writing ')
    st.write('## Writing')
    

if __name__ == '__main__':
    streamlit_text()