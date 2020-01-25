import re
def usernameValidity(username):
    format = r'^[a-z][\w]{4,11}'
    # format regex: [a-z]  diawali huruf kecil 
    #               [\w]   tidak menggunakan special character kecuali unedrscore
    #               {4,11} repitisi format diatas, min 4 karakter 
    #                      dan max 14 karakter
    return bool(re.fullmatch(format,username))
def passwordValidity(password):
    # cek syarat satu-persatu agar lebih mudah dibaca
    if bool(re.fullmatch(r'^[0-9A-Z\W]{7}$',password)):
      # If bernilai True jika password berupa 7 karakter 
      # dengan kombinasi angka, huruf besar, dan simbol
      if len(re.findall(r'[0-9]',password))==1:
        # If bernilai True jika password memuat 1 angka
        if len(re.findall(r'[\W]',password))==1:
          # If bernilai True jika password memuat 1 simbol
          # return True, karena password adalah kombinasi 
          # 1 simbol, 1 angka dan 5 huruf besar
          return True
    return False