import xlrd3 as xlrd
from format import *
from excel.records import *
from excel.acceptance_ import acceptance


def get_pr_list_from_excel (file, number_or_lines ):
    index2=number_or_lines
    #printf2 ('Excel -  получение анкет ')

    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def is_float(s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def is_not_nan(num):
        return num == num

    pr_list = [] #product properties

    try:
        book = xlrd.open_workbook(file)
    except:
        # traceback.print_exc()
        print('ОШИБКА: ВЕРОЯТНО, EXCEL-ФАЙЛ НЕПРАВИЛЬНОГО ФОРМАТА ')
        quit()

    sh = book.sheet_by_index(0)
    printf('EXCEL всего анкет       =',sh.nrows)


    if index2==0: index2=sh.nrows
    printf('EXCEL анкет извлекается =', index2)


    #print('lensh ',type(sh.nrows))
    #print("The number of worksheets is {0}".format(book.nsheets))
    #print("Worksheet name(s): {0}".format(book.sheet_names()))
    #print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
    print ('колонок в EXCEL-файле= ',sh.ncols)
    if  (  sh.ncols!=4  ): raise SystemExit

    #print("Cell 0 is {0}".format(sh.cell_value(rowx=2, colx=0)))
    #print("Cell 1 is {0}".format(sh.cell_value(rowx=2, colx=1)))
    #print("Cell 2 is {0}".format(sh.cell_value(rowx=2, colx=2)))
    #print("Cell 3 is {0}".format(sh.cell_value(rowx=2, colx=3)))
    #range_=sh.nrows
    #rowrecord=sh.row
    #print("sh.nrows ",sh.nrows)
    #print("sh.nrow=== ", sh.row(1))


    for rx in range(1,index2):

        pr={}

        rowline = sh.row(rx)
        #print('rowline=', rowline)
        #input('22222')

        pr=records_ (rowline)

        # check is it real product line
        if (  acceptance(pr)==1 ):

            expdate=pr['manufacturer_code']
            expirydate_xlrd = xlrd.xldate.xldate_as_datetime( expdate,book.date_mode)
            expirydate = expirydate_xlrd.strftime("%d") + '.' + expirydate_xlrd.strftime("%m") + '.' + expirydate_xlrd.strftime("%Y")
            pr['manufacturer_code']=expirydate
            #print('111', type(rowline[3].value),rowline[3].value )
            #print('222', type(pr['manufacturer_code'] ), pr['manufacturer_code'] )
            #print('333', type(expirydate_xlrd), expirydate_xlrd)
            #print('444', type(expirydate), expirydate)


            pr_list.append(pr)

    if not pr_list:
        printf('ОШИБКА EXCEL-ФАЙЛА - ВЕРОЯТНО, КОЛОНКИ В НЕПРАВИЛЬНОМ ПОРЯДКЕ')
        quit()



    return pr_list














