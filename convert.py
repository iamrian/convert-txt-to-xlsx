import pandas as pd

def txt_to_excel(txt_file, excel_file):
    with open(txt_file, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file if line.strip()]
    
    # Pastikan jumlah data kelipatan 6 (karena setiap set terdiri dari 6 baris)
    if len(lines) % 6 != 0:
        print("Format file tidak sesuai. Harus kelipatan 6 baris per data.")
        return
    
    # Ambil hanya email (baris ke-1), password (ke-2), private key (ke-4), wallet address (ke-5)
    data = []
    for i in range(0, len(lines), 6):
        email = lines[i]
        password = lines[i+1]
        private_key = lines[i+3]
        wallet_address = lines[i+4]
        data.append([email, password, private_key, wallet_address])
    
    # Simpan ke Excel
    df = pd.DataFrame(data, columns=["Email", "Password", "Private Key", "Wallet Address"])
    df.to_excel(excel_file, index=False)
    print(f"Data berhasil disimpan ke {excel_file}")

# Contoh penggunaan
# Ganti 'data.txt' dengan nama file TXT yang sesuai
# Ganti 'output.xlsx' dengan nama file Excel yang diinginkan
txt_to_excel('data.txt', 'output.xlsx')
