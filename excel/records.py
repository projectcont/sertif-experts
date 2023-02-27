def records_ (rowline):


    pr={}


    vl = []
    for column in rowline:
        column_=str(column.value)
        vl.append(column_)

    # remove space from ends of record
    column0 = vl[0].strip(' ')  #sert_number
    column1 = vl[1].strip(' ')  #fio
    column2 = vl[2].strip(' ')  #area

    try:
        column3 = float(vl[3])   #expirydate
    except ValueError:
        column3 = ''


    column4 = column2  #custom
    column5 = column2  #custom

    alias_ = str(column1)
    alias_list=[ n for n in alias_ if n in '0123456789' ]
    alias=''.join(alias_list)
    alias=str(len(column0))+str(alias)
    #print('alias=',alias)


    #correspondence between columns(excel) and pr
    pr['product_ean'] = column1  # sert_number
    pr['name_ru-RU'] =  column0.title()  # fio
    pr['description_ru-RU'] = column2
    pr['manufacturer_code'] = column3 #expirydate

    pr['custom1'] = 'feature1'
    pr['custom2'] = 'feature2'

    pr['short_description_ru-RU'] = column2
    pr['alias_ru-RU'] = alias


    return pr