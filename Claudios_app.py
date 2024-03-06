from click import prompt
import streamlit as st
import pandas as pd
import numpy as np


def main ():
    st.title('This is Claudios first APP')
    st.sidebar.title('NOTHING IMPORTANT HERE')
    st.sidebar.write('1. Everthing is OK')
    st.sidebar.write('If not read the first again')
    st.sidebar.write('Still everthing is OK')

    st.sidebar.subheader('Chat')
    with st.sidebar:
        messages = st.container(height=300)
        if prompt := st.chat_input("Say something"):
            messages.chat_message("user").write(prompt)
            messages.chat_message("assistant").write(f"Echo: {prompt}")



    st.write('-----')
    st.write('Hello people')

    col1, col2, col3 = st.columns(3)
    col1.metric("Temperature", "70 °F", "1.2 °F")
    col2.metric("Wind", "9 mph", "-8%")
    col3.metric("Humidity", "86%", "4%")

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

    st.area_chart(chart_data)

    values = st.slider(
        'Select a range of values',
       0.0, 100.0, (25.0, 75.0))
    st.write('Values:', values)

    st.button("Reset", type="primary")
    if st.button('Say hello'):
        st.write('Why hello there')
    else:
        st.write('This is the END this APP')
        st.write('Goodbye')

if __name__ == '__main__':
    main()