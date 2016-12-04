# encoding: utf-8

import  xdrlib ,sys
import xlrd

def main():
	print("Hello world")
	book =  xlrd.open_workbook('file.xls')
	sheet0 = book.sheet_by_index(0)
	# print(sheet0.row(0))

	count = 0
	while True:
		print(sheet0.row(count))
		count += 1
		if count >= 5:
			break

	# table = data.sheets()[0]


	# print table.cell(0,0).value
	# print table


if __name__=="__main__":
	main()