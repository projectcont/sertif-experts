
from prodcateg.category import Category
from prodcateg.custom import Custom
import traceback



def prodlist_add (prod_list_add,session):
    '''
    for all 'products' in 'prod_list'
    function adds each 'product' to database
    :param prod_list: list of products
    :param session:  session
    :return:
    '''

    print()
    print('crud1 ЭКСПОРТ ДАННЫХ НА САЙТ')

    for prod in prod_list_add:
        try:
            #print( '          добавлено ',  getattr(prod, 'name_ru-RU') )

            session.add(prod)
            session.flush()
            session.refresh(prod)



            ctp = Category()
            ctp.setpr(prod)

            custom_ru=Custom()
            custom_ru.setpr(prod,lang="ru-RU")
            custom_eng = Custom()
            custom_eng.setpr(prod, lang="en-GB")

            session.add(ctp)
            session.add(custom_ru)
            session.add(custom_eng)

            session.commit()

            ''' 
            print()
            print("          (inside crud) prod =", prod.product_ean)
            print("          (inside crud) product_id=", prod.product_id)
            print("          (inside crud) product_ct=", prod.category_id)
            print(prod)
            print('          (inside crud) ctp=', ctp)
            '''



        except:
            traceback.print_exc()
            print('ОШИБКА СОЕДИНЕНИЯ С БАЗОЙ ДАННЫХ')
            session.rollbask()
            raise
        finally:
            session.close()

    print('crud2 ЭКСПОРТ ДАННЫХ НА САЙТ ВЫПОЛНЕН')
    print()

