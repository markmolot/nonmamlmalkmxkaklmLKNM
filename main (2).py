товары_снюс = ['Снюс со вкусом екарни сир', 'Снюс со вкусом огромни бобер', 'Снюс классический']
цены_снюс   = [90, 150,  1090]

товары_бебра = ['Бебра забивная', 'Бебра отбивная', 'Люти бебра']
цены_бебра =   [1790,  70,  50]

товары_бебра = ['Тульский пряник', "Тульско-противотанковая самоходная установка Jagdtiger (SdKFz 186) Самая тяжелая и самая мощная САУ германского производства периода Второй мировой войны применявшаяся в боевых действиях.", 'Пряник тульский']
цены_бебра =   [1790,  70,  50]

общая_стоимость = 0
все_купленные_товары = ''

a = ' '
d=0
s=1
pystota=" "
print('Добро пожаловать в Бебрагазин!')
while s==True:
    print('Категория товара:')
    print('1.Снюс')
    print('2.Бебра')
    print('3.Тульский пряник')
    print("4.Корзина")
    print('0.Конец покупок')
    o=int(input('...'))
    if o<0:
        print('ты даун?')
    if o>4:
        print('ты даун?')
    if o==4:
        print(d,"рублей",pystota )
    if o==1:
        while a!=0:
            a=int(input("Выбирай: 1  снюс 2 Снюс  3 Саратовский пряник 0 уйти"))
            if o==1:
                i = 0
                while i < len(товары_снюс):
                    print(i, '.', товары_снюс[i], цены_[i])
                    i += 1
                b=int(input(""))
                общая_стоимость += цены_снюс[b]
                все_купленные_товары += товары_снюс[b]
            if o==2:
                i = 0
                while i < len(товары_бебра):
                    print(i, '.', товары_бебра[i], цены_бебра[i])
                    i += 1
                b=int(input(""))
                общая_стоимость += цены_бебра[b]
                все_купленные_товары += товары_бебра[b]
            if o==3:
                i = 0
                while i < len(товары_тульскийпряник):
                    print(i, '.', товары_тульскийпряник[i], цены_тульскийпряник[i])
                    i += 1
                b=int(input(""))
                общая_стоимость += цены_тульскийпряник[b]
                все_купленные_товары += товары_тульскийпряник[b]
            if o==0:
                s-=1