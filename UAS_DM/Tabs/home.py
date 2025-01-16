import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import pandas as pd
import os

def generate_plots(df):
    # Plot histogram
    st.subheader("Histogram Distribusi Fitur")
    for column in df.columns:
        if df[column].dtype != 'O':  # Plot hanya untuk fitur numerik
            plt.figure(figsize=(12, 6))
            sns.histplot(df[column], bins=20, kde=True)
            st.pyplot(plt)
            plt.clf()  # Clear the figure after plotting
            st.write(f"### Distribusi dari {column}")

    # Plot correlation heatmap
    st.subheader("Heatmap Korelasi Fitur")
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f', linewidths=.5)
    st.pyplot(plt)
    plt.clf()  # Clear the figure after plotting

# Load dataset
def load_data():
    # Load dataset sesuai kebutuhan
    df = pd.read_csv('/mount/src/datamining4519/UAS_DM/Penyakit_Paru.csv')
    return df

def app():
    # Judul halaman aplikasi
    st.title("APLIKASI PREDIKSI TERKENA PENYAKIT PARU-PARU")
    
    # Load dataset
    df = load_data()

    # Tampilkan gambar
    file_path = "/mount/src/datamining4519/UAS_DM/paruu.jpeg"
    st.image(file_path, caption="Paru-Paru", use_column_width=True)
    
    # Tampilkan keterangan
    st.write("Penyakit paru-paru adalah salah satu penyebab kematian tertinggi di dunia. "
             "Penyakit ini dapat disebabkan oleh berbagai faktor. Penyakit paru-paru merupakan "
             "salah satu penyebab utama kematian di dunia, yang dapat dipicu oleh berbagai faktor "
             "seperti kebiasaan merokok, polusi udara, infeksi, genetika, dan paparan zat berbahaya "
             "di lingkungan atau tempat kerja. Aplikasi ini dapat digunakan untuk memperkirakan risiko "
             "seseorang terkena penyakit paru-paru berdasarkan faktor-faktor risiko yang dapat diukur. "
             "Aplikasi ini sudah melakukan riset kepada 30 ribu orang yang dilihat dari beberapa faktor "
             "yaitu: Usia, Jenis_Kelamin, Merokok, Bekerja, Rumah_Tangga, Aktivitas_Begadang, Aktivitas_Olahraga, "
             "Asuransi, Penyakit_Bawaan, Hasil.")
             
    # Tampilkan grafik
    generate_plots(df)

if __name__ == "__main__":
    app()
