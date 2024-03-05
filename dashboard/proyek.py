import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from babel.numbers import format_currency

sns.set(style='dark')

# Menambahkan judul di tengah
st.title("Dashboard Analisis Bike Sharing")

# Mengimpor dataset
def load_data():
    return pd.read_csv("day.csv")

# Memuat data
df = load_data()

# Mengatur konfigurasi Streamlit untuk menonaktifkan peringatan pyplot global
st.set_option('deprecation.showPyplotGlobalUse', False)

#rename columns
df.rename(columns={'dteday': 'date'}, inplace=True)
df.rename(columns={'mnth': 'month'}, inplace=True)
df.rename(columns={'yr': 'year'}, inplace=True)
df.rename(columns={'weathersit': 'weather'}, inplace=True)
df.rename(columns={'temp': 'temperatur'}, inplace=True)
df.rename(columns={'hum': 'humidity'}, inplace=True)
df.rename(columns={'cnt': 'count'}, inplace=True)

# Menambahkan sidebar
st.sidebar.title("Pilih Visualisasi")
visualization_option = st.sidebar.radio("Visualisasi", ("Perubahan Penggunaan Bulanan", "Pola Penggunaan Berdasarkan Cuaca"))

df.year.replace({0:2011, 1:2012}, inplace=True)
df.month.replace({1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Augst', 9:'Sept', 10:'Okt', 11:'Nov', 12:'Dec'}, inplace=True)
df.weather.replace({1:'Clear', 2:'Mist', 3:'Light Snow', 4:'Heavy Rain'}, inplace=True)

# Visualisasi perubahan penggunaan Bike Sharing dari bulan ke bulan
if visualization_option == "Perubahan Penggunaan Bulanan":
    st.subheader('Perubahan Penggunaan Bike Sharing dari Bulan ke Bulan')

    # Menampilkan widget untuk memilih bulan
    selected_year = st.selectbox("Pilih Tahun", df['year'].unique())

    # Filter data berdasarkan bulan yang dipilih
    filtered_data = df[df['year'] == selected_year]
    monthly_rentals = filtered_data.groupby('month')['count'].sum()

    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=monthly_rentals, marker='o', color='skyblue', ax=ax)
    plt.title('Perubahan Penggunaan Bike Sharing dari Bulan ke Bulan')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(fig)
    
    plt.figure(figsize=(8, 6))
    monthly_rentals.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon', 'orange'])
    plt.title('Pola Penggunaan Bike Sharing Berdasarkan Cuaca')
    plt.xlabel('Cuaca')
    plt.ylabel('Rata-rata Jumlah Peminjaman')
    plt.xticks(rotation=0)
    st.pyplot()

# Visualisasi pola penggunaan Bike Sharing berdasarkan cuaca
elif visualization_option == "Pola Penggunaan Berdasarkan Cuaca":
    st.subheader('Pola Penggunaan Bike Sharing Berdasarkan Cuaca')

    # Menampilkan widget untuk memilih tahun
    selected_year = st.selectbox("Pilih Tahun", df['year'].unique())

    # Filter data berdasarkan tahun yang dipilih
    filtered_data = df[df['year'] == selected_year]
    rentals_by_weather = filtered_data.groupby('weather')['count'].mean()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=rentals_by_weather, marker='o', color='skyblue', ax=ax)
    plt.title('Perubahan Penggunaan Bike Sharing Berdasarkan Cuaca')
    plt.xlabel('Bulan')
    plt.ylabel('Jumlah Peminjaman')
    st.pyplot(fig)

    plt.figure(figsize=(8, 6))
    rentals_by_weather.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon', 'orange'])
    plt.title('Pola Penggunaan Bike Sharing Berdasarkan Cuaca')
    plt.xlabel('Cuaca')
    plt.ylabel('Rata-rata Jumlah Peminjaman')
    plt.xticks(rotation=0)
    st.pyplot()

