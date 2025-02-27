
try:
    df = pd.read_csv('students.csv', encoding='utf-8')  # Pastikan encoding sesuai
    print("Dataset berhasil dimuat!")
    
    # Menampilkan 5 baris pertama dataset
    print(df.head())

except FileNotFoundError:
    print("Error: File 'students.csv' tidak ditemukan. Pastikan file berada di direktori yang benar.")

except pd.errors.EmptyDataError:
    print("Error: File 'students.csv' kosong.")

except pd.errors.ParserError:
    print("Error: Format CSV tidak valid. Periksa delimiter atau struktur file.")
