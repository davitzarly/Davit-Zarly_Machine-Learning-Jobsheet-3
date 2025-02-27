import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Contoh data usia mahasiswa
data = {'Usia': [20, 21, 22, 20, 23, 22, 21, 20]}  
df = pd.DataFrame(data)

# Membuat plot
plt.figure(figsize=(8,5))
sns.histplot(df['Usia'], bins=5, kde=True, color='steelblue', alpha=0.6)

# Menambahkan judul dan label
plt.title("Distribusi Usia Mahasiswa", fontsize=12)
plt.xlabel("Usia", fontsize=10)
plt.ylabel("Frekuensi", fontsize=10)

# Menampilkan plot
plt.show()
