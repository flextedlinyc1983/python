# encoding: utf-8

# print "Hello World"
# print "Hello World"
# print "Hello World"
# print "Hello World"
# print "Hello World"
# passwd={'Mars':00000,'Mark':56680}
# print passwd

import  xdrlib ,sys
import xlrd

def open_excel(file= 'file.xls'):
	try:
		data = xlrd.open_workbook(file)
 		return data
 	except Exception,e:
		print str(e)

def excel_table_byname(file= 'file.xls'):
	data = open_excel(file)
	return data

def main():
	data = excel_table_byname()
	table = data.sheets()[0]
	print table.row_values(0)
	print table.row_values(5)
 	
 	print table.cell(5,0).value
 	print table.cell(5,1).value
 	print table.cell(5,2).value
 	print table.cell(5,3).value
	


if __name__=="__main__":
	main()