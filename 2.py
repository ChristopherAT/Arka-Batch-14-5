import re
def usernameValidity(username):
    format = r'^[a-z][a-z_\.]{7,11}'
    # format regex: [a-z]  diawali huruf kecil 
    #               [a-z_\.]  hanya menerima huruf kecil, titik, dan underscore
    #               {7,11} repitisi format sebelumnya, min 7 karakter 
    #                      dan max 11 karakter
    return bool(re.fullmatch(format,username))
def passwordValidity(password):
    # cek syarat satu-persatu agar lebih mudah dibaca
    if bool(re.fullmatch(r'^[\w\W]{9}$',password)):
      # If bernilai True jika password berupa 9 karakter 
      # dengan kombinasi angka, huruf besar, dan simbol
      if len(re.findall(r'[0-9]',password))>=1:
        # If bernilai True jika password memuat min 1 angka
        if len(re.findall(r'[\W]',password))>=1:
          # If bernilai True jika password memuat min 1 simbol
          # return True, karena password adalah kombinasi 
          # 1 simbol, 1 angka dan 7 huruf besar
          return True
    return False