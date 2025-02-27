import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Membuat dataset
students_data = {
    'Nama': ['Alice', 'Bob', 'Charlie', 'Daisy', 'Eve'],
    'Usia': [20, 21, 22, 20, 21],
    'Jenis Kelamin': ['Perempuan', 'Laki-laki', 'Laki-laki', 'Perempuan', 'Perempuan'],
    'Jurusan': ['Informatika', 'Informatika', 'Sistem Informasi', 'Sistem Informasi', 'Informatika'],
    'Matematika': [85, 82, 91, 78, 90],
    'IPA': [90, 88, 85, 80, 92],
    'Bahasa Inggris': [78, 74, 89, 84, 88]
}

# Membuat DataFrame
students_df = pd.DataFrame(students_data)

# Menyimpan ke CSV
csv_filename = "students.csv"
students_df.to_csv(csv_filename, index=False)

# Menampilkan tabel
print(students_df)

# Histogram usia mahasiswa
plt.figure(figsize=(6,4))
sns.histplot(students_df['Usia'], kde=True, bins=5)
plt.xlabel("Usia")
plt.ylabel("Frekuensi")
plt.title("Distribusi Usia Mahasiswa")
plt.show()

# Boxplot nilai
plt.figure(figsize=(6,4))
sns.boxplot(data=students_df[['Matematika', 'IPA', 'Bahasa Inggris']])
plt.xlabel("Mata Pelajaran")
plt.ylabel("Nilai")
plt.title("Distribusi Nilai Mahasiswa")
plt.show()

# Scatter plot perbandingan nilai Matematika dan IPA berdasarkan jenis kelamin dan jurusan
plt.figure(figsize=(6,4))
sns.scatterplot(data=students_df, x='Matematika', y='IPA', hue='Jenis Kelamin', style='Jurusan')
plt.xlabel("Nilai Matematika")
plt.ylabel("Nilai IPA")
plt.title("Perbandingan Nilai Matematika dan IPA Berdasarkan Jenis Kelamin dan Jurusan")
plt.legend(title="Jenis Kelamin & Jurusan")
plt.show()

# Boxplot perbandingan nilai Matematika berdasarkan jurusan dan jenis kelamin
plt.figure(figsize=(6,4))
sns.boxplot(x='Jurusan', y='Matematika', hue='Jenis Kelamin', data=students_df)
plt.xlabel("Jurusan")
plt.ylabel("Nilai Matematika")
plt.title("Perbandingan Nilai Matematika Berdasarkan Jurusan dan Jenis Kelamin")
plt.show()
