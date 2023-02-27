def acceptance (pr):

    accept = 1
    if  (pr['product_ean'].find('RU') == -1):
        print(f"          строка    ({pr['name_ru-RU']})   ({pr['product_ean']}) не принята, ошибка в номере сертификата" )
        accept = 0

    if  [s for s in pr['name_ru-RU'] if s in '1234567890']:
        print( f"          строка ({pr['name_ru-RU'] }) не принята, ошибка в ФИО" )
        accept = 0

    if  len(str(pr['manufacturer_code']))==0:
        print(f"          строка  ( {pr['name_ru-RU']}) не принята, ошибка в дате сертификата ")
        accept = 0


    return accept

