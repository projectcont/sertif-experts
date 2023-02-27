from prodcateg.product import Product
import sqlf.сountprod
import traceback


def dispence (session, prod_list_excel):
    '''
    functuion obtains list of employers (instances)
    :param session, prod_list_excel
    :return: prod_list_add
    '''

    def dig(string_):
        result_list = [n for n in string_ if n in '0123456789']
        result_ = ''.join(result_list)
        result2 = str(result_)
        return result2


    print()
    print('DISPENCE')

    count=0
    prod_list_add = []
    allprod = session.query(Product)

    for n in prod_list_excel:

        #print(getattr(n, 'name_ru-RU'), 'n considered')
        prev=0

        for prod_ in allprod:
            #print( str(getattr(prod_, 'name_ru-RU')) )

            if (  dig(prod_.product_ean)==dig(n.product_ean)   ):

                prod_.manufacturer_code = n.manufacturer_code
                descr_ = getattr(n, 'description_ru-RU')
                setattr(prod_, 'description_ru-RU', descr_)

                session.flush()
                session.refresh(prod_)


                count = count + 1
                prev = 1
                print(count, ' меняется ', getattr(prod_, 'name_ru-RU'), prod_.product_ean, n.product_ean, )

        session.commit()

        if prev == 0:
            prod_list_add.append(n)

    print()
    print('на сайте меняется    анкет =', count)
    print('на сайте добавляется анкет =', len(prod_list_add))


    sqlf.сountprod.Countprod.update =count
    sqlf.сountprod.Countprod.add = len(prod_list_add)

    return prod_list_add






