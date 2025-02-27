import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Contoh data
data = {
    'Nama': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
    'Nilai Matematika': [85, 78, 90, 76, 88, 92, 79, 84, 89, 77],
    'Nilai IPA': [88, 80, 91, 80, 87, 90, 78, 85, 86, 82],
    'Jenis Kelamin': ['Perempuan', 'Laki-laki', 'Perempuan', 'Laki-laki', 'Perempuan', 'Perempuan', 'Laki-laki', 'Perempuan', 'Laki-laki', 'Perempuan'],
    'Jurusan': ['Informatika', 'Sistem Informasi', 'Informatika', 'Sistem Informasi', 'Informatika', 'Sistem Informasi', 'Informatika', 'Sistem Informasi', 'Informatika', 'Sistem Informasi']
}

df = pd.DataFrame(data)

# Membuat figure dan axes
fig, axes = plt.subplots(2, 1, figsize=(10, 12))

# Scatter plot
sns.scatterplot(
    data=df,
    x='Nilai Matematika', 
    y='Nilai IPA', 
    hue='Jenis Kelamin', 
    style='Jurusan', 
    palette={'Perempuan': 'blue', 'Laki-laki': 'orange'}, 
    markers={'Informatika': 'o', 'Sistem Informasi': 'X'},
    s=100,  # Ukuran marker diperbesar
    ax=axes[0]
)
axes[0].set_title("Perbandingan Nilai Matematika dan IPA Berdasarkan Jenis Kelamin dan Jurusan", fontsize=12)
axes[0].set_xlabel("Nilai Matematika", fontsize=10)
axes[0].set_ylabel("Nilai IPA", fontsize=10)
axes[0].grid(True, linestyle='--', alpha=0.7)
axes[0].legend(title="Jenis Kelamin & Jurusan", loc='upper left', bbox_to_anchor=(1, 1))

# Box plot
sns.boxplot(
    data=df, 
    x='Jurusan', 
    y='Nilai Matematika', 
    hue='Jenis Kelamin', 
    palette={'Perempuan': 'blue', 'Laki-laki': 'orange'},
    width=0.6,
    dodge=True,  # Memastikan data tidak tumpang tindih
    ax=axes[1]
)
axes[1].set_title("Perbandingan Nilai Matematika Berdasarkan Jurusan dan Jenis Kelamin", fontsize=12)
axes[1].set_xlabel("Jurusan", fontsize=10)
axes[1].set_ylabel("Nilai Matematika", fontsize=10)
axes[1].grid(True, linestyle='--', alpha=0.7)
axes[1].legend(title="Jenis Kelamin", loc='upper left', bbox_to_anchor=(1, 1))

# Menampilkan plot
plt.tight_layout()
plt.show()
