import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn import tree
import streamlit as st

from web_functions import train_model

def plot_confusion_matrix(y_test, y_pred):
    #Membuat dan menampilkan confusion matrix menggunakan seaborn dan Streamlit.
    mat = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 8))
    sns.heatmap(mat, annot=True, fmt="d", cmap="Blues", cbar=False)
    plt.title('Confusion Matrix')
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    st.pyplot()

def app(df, x, y):
    #Fungsi utama untuk visualisasi prediksi penyakit paru-paru di aplikasi Streamlit.
    warnings.filterwarnings('ignore')

    st.title("Visualisasi Prediksi Penyakit Paru-Paru")

    try:
        if st.checkbox("Plot Confusion Matrix"):
            # Pisahkan data menjadi training dan testing jika belum dilakukan di train_model
            X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

            # Train model menggunakan fungsi yang ada
            model, _ = train_model(X_train, y_train)

            # Prediksi pada data testing
            y_pred = model.predict(X_test)

            # Plot confusion matrix
            plot_confusion_matrix(y_test, y_pred)

        if st.checkbox("Plot Decision Tree"):
            # Train model
            model, score = train_model(x, y)

            # Visualisasi decision tree
            dot_data = tree.export_graphviz(
                decision_tree=model, max_depth=3, out_file=None, filled=True, rounded=True,
                feature_names=x.columns, class_names=["Tidak", "Ya"]
            )
            st.graphviz_chart(dot_data)

    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
