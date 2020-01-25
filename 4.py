# -*- coding: utf-8 -*-
def findDuplicates(kalimat=None):
	if kalimat==None or type(kalimat) != str:
		print('Harus memasukan parameter dan harus string!')
	else:
		char_dict = {}
		for char in kalimat:
			if char in char_dict:
				char_dict[char] += 1
			else:
				char_dict[char] =1
		
		if max(char_dict.values()) > 1:
			for char,count in char_dict.items():
				print(char,':',count)
		else:
			print("Tidak ada karakter yang berulang!")
