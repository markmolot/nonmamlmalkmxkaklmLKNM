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
        print('1.Снюс со вкусом екарни сир')
        print('2.Снюс со вкусом огромни бобер')
        print('3.Снюс классический')
        e=int(input('Какой берешь?'))
        if e<0:
            print('ты даун?')
        if e>3:
            print('ты даун?')
        if e==1:
            print('ты потерял 10 рублей,понятно?')
            d+=10
            pystota+=" Снюс со вкусом екарни сыр"
        if e==2:
            print('ты потерял 15 рублей,понятно?')
            pystota+=" Снюс со вкусом огромни бобер"
            d+=15
        if e==3:
            print('ты потерял 5 рублей,понятно?')
            d+=5
            pystota+=" Снюс класический"
    if o==2:
        print('1.Бебра забивная')
        print('2.Бебра отбивная')
        print('3.Люти бебра')
        p=int(input('Какую берешь?'))
        if p<0:
            print('ты даун?')
        if p>3:
            print('ты даун?')
        if p==1:
            print('ты потерял 90 рублей,понятно?')
            d+=90
            pystota+=" Бебра забивная"
        if p==2:
            print('ты потерял 70 рублей,понятно?')
            d+=70
            pystota+=" Бебра отбивная"
        if p==3:
            print('ты потерял 50 рублей,понятно?')
            d+=50
            pystota+=" Люти бебра"
    if o==3:
        print('1.Тульский пряник забивной')
        print('2.Тульский пряник со вкусом екарни снюс')
        print('3.Люти тульский пряник')
        y=int(input('Какую берешь?'))
        if y<0:
            print('ты даун?')
        if y>3:
            print('ты даун?')
        if y==1:
            print('ты потерял 75 рублей,понятно?')
            d+=75
            pystota+=" Тульский пряник забивной"
        if y==2:
            print('ты потерял 115 рублей,понятно?')
            d+=115
            pystota+=" Тульский пряник со вкусом екарни снюс"
        if y==3:
            print('ты потерял 95 рублей,понятно?')
            d+=95
            pystota+=" Люти тульский пряник"
    if o==0:
        s-=1