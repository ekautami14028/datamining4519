import os

try:
    import sklearn
    print("Scikit-learn sudah terinstal.")
except ImportError:
    print("Menginstal scikit-learn...")
    os.system("pip install scikit-learn")
    print("Scikit-learn berhasil diinstal.")
