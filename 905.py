import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Contoh data nilai mahasiswa
data = {
    'Matematika': [80, 85, 78, 90, 88, 75, 92, 85, 84, 89],
    'IPA': [82, 88, 79, 91, 87, 80, 90, 86, 85, 88],
    'Bahasa Inggris': [78, 85, 80, 89, 90, 77, 91, 84, 83, 87]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Membuat plot
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, width=0.6)

# Menambahkan judul dan label
plt.title("Distribusi Nilai Mahasiswa", fontsize=12)
plt.xlabel("Mata Pelajaran", fontsize=10)
plt.ylabel("Nilai", fontsize=10)

# Menampilkan plot
plt.show()
