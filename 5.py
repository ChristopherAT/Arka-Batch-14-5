# -*- coding: utf-8 -*-
def findHighestProfit(saham):
	n = len(saham)
	max_profit=0
	for i in range(n):
		for j in range(i,n):
			selisih = saham[j] - saham[i]
			if selisih>max_profit:
				max_profit=selisih
	return max_profit