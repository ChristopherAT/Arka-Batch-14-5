# -*- coding: utf-8 -*-
def count_handshake(n):
	counter=0 # Counter untuk jabat tangan
	
	# Jika setiap orang berjabat tangan dengan semua yang hadir dan hanya sekali berjabat tangan tangan dengan orang yang sama
	# Jika ada n orang, orang pertama akan berjabat tangan dengan n-1 orang lainnya.
	# Orang kedua sudah berjabat tangan dengan orang pertama. Jadi orang kedua berjabat tangan dengan n-2 orang.
	# Orang ketiga berjabat tangan n-3 kali, dan seterusnya.
	# orang ke n-1 berjabat tangan dengan 1 orang lainnya. Orang ke-n (terakhir) sudah berjabat tangan dengan semuanya. Jadi ada 0 jabat tangan.
	# Jumlahkan semua jabat tangan dari tiap orang, hasilnya adalah:
	#          n-1 + n-2 + ... + 1 + 0
	for i in range(n):
		counter+=i 
	return counter