# DEFINE THE DATABASE CREDENTIALS


#experts
dbconf=dict (
        user = '',
        password = '',
        host = '',
        port = 3306,
        database = ''
)


showdebug=False

# echo : engine.py   (echo=False)
# debug: main.py   app.run(debug=True)

# product listing:
#       excel.py      print('          (inside excel_list) ', prod);
#       sqlf.crud.ry 19           print(prod)   line39


'''
product properties setting-
file product.py
        self.vendor_id = 1 (status)

file get_pr_.py
        manufacturer_code = 07.07.2025  (expiry date of sertificate)
        add_price_unit_id=3
        weight_volume_units=32.0000
        basic_price_unit_id=3

records.py
        custom (lines 36,37)

вывод анкет которые корректируются
        file 'dispence_.py'
        line 34 #print( '          updated',  getattr(prod_, 'name_ru-RU') )

вывод анкет которые  добавляются
        file 'crud.py'
        line 22  #print( '          добавлено ',  getattr(prod, 'name_ru-RU') )
'''


excel_format='''
Excel-файл с названием 1.xlsx должен быть в каталоге 'rssp-exp/files'
<br/> Формат Excel-файла: 4 колонки <br/>
1) ФИО <br/>
2) Номер сертификата <br/>
3) Специализация<br/>
3) Дата окончания сертификата <br/>

'''