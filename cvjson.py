import pandas as pd
import json

def json_to_excel(json_file, excel_file):
    # Baca file JSON
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Ubah ke DataFrame
    df = pd.DataFrame([data])  # Pakai list agar bisa dibuat DataFrame langsung

    # Simpan ke Excel
    df.to_excel(excel_file, index=False)
    print(f"Data berhasil disimpan ke {excel_file}")

# Contoh penggunaan
json_to_excel('data.json', 'output.xlsx')
