import json
import pandas as pd

def json_to_excel(json_file, excel_file):
    # Membaca file JSON
    with open(json_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Pastikan JSON berupa list of dicts
    if not isinstance(data, list):
        print("Format JSON tidak sesuai. Harus berupa list.")
        return

    # Konversi ke DataFrame
    df = pd.DataFrame(data)

    # Simpan ke Excel
    df.to_excel(excel_file, index=False)
    print(f"Data berhasil disimpan ke {excel_file}")

# Contoh penggunaan
json_to_excel('data.json', 'output.xlsx')
