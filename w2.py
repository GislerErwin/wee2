import streamlit as st
import pandas as pd
import numpy as np
import altair as alt    

def main():
    st.title('App Woche 2')
    st.write('Erste Tabelle')
    data = pd.DataFrame({
        'Erster Datensatz': [1, 2, 3, 4],
        'Zweiter Datensatz': [10, 20, 30, 40],
    })
    st.write('Hello, meine erste Streamlit-App :sunglasses:')
    st.dataframe(data)
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["X-Achse", "Y-Achse", "Daten"])
    chart_data['Daten 2'] = np.random.choice(['A','B','C'], 20)

    st.scatter_chart(
        chart_data,
        x='X-Achse',
        y='Y-Achse',
        color='Daten 2',
        size='Daten',
    )
    color = st.select_slider(
        'Wähle eine Farbe',
        options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
    st.write('Mein gewählte Farbe', color)
        
    st.sidebar.header('Sidebar Title')

    option = st.sidebar.selectbox(
        'Wähle den Unterordner',
        ('Ordner 1', 'Ordner 2', 'Ordner 3')
    )
    slider_value = st.sidebar.slider('Select a value', 0, 100, 50)
    st.title('Hauptinhalt')
    st.write(f'Ausgewählter Ordner: {option}')
    st.write(f'Ausgewählte Grösse: {slider_value}')

if __name__ == "__main__":
    main()