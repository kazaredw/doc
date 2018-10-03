#Скрипт сравнивает два ексель файла, выводи разницу
#Пример файла

#13-51329826	Тульская обл
#13-51330235	Тульская обл


import xlrd
mybook = xlrd.open_workbook('kso.xlsx')
mysheet = mybook.sheet_by_name('KSO_GM')

ncr = xlrd.open_workbook('KSONCR.xls')
ncrsheet = ncr.sheet_by_name('Sheet1')

#Вывод mybook
mykso=[]
ncrkso=[]

for item in range(mysheet.nrows):
    if mysheet.row_values(item)[9]!='SN КСО' \
    and mysheet.row_values(item)[0]!='Всего КСО на 195 ГМ' \
    and mysheet.row_values(item)[0]!='ККМ ШТРИХ-МИНИ-01Ф (online)' \
    and mysheet.row_values(item)[0]!='ККМ АТОЛ FPrint-22ПТК (online)' \
    and mysheet.row_values(item)[0]!='TIME END  9:47:06' \
    and mysheet.row_values(item)[0]!='ККМ РИТЕЙЛ-01Ф (online)':
            #print(mysheet.row_values(item)[9],mysheet.row_values(item)[0])
            mykso.append(mysheet.row_values(item)[9])
for item in range(ncrsheet.nrows):
    if ncrsheet.row_values(item)[3]!='Серийный номер':
    #print(ncrsheet.row_values(item)[3],ncrsheet.row_values(item)[5])
        ncrkso.append(ncrsheet.row_values(item)[3])     
                
result=list(set(mykso)^set(ncrkso))

for item in range(ncrsheet.nrows):
    if ncrsheet.row_values(item)[3]!='Серийный номер':
        for i in range(len(result)):
            if ncrsheet.row_values(item)[3]==result[i]:
                print(ncrsheet.row_values(item)[3],ncrsheet.row_values(item)[5])
