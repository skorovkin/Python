'''found_coins = 20
magic_coins = 70
stolen_coins = 3
coins= found_coins
for i in range (1,53):
    coins = coins + magic_coins - stolen_coins
    print ('Week %s = %s' % (i, coins))'''
'''x=0
while x <= 28:
    if x % 2 == 0:
        print (x)
    x = x+1'''

'''x=0
y=1
ingredients = ['слизни', 'пиявки', 'катышки из пупка гориллы','брови гусеницы', 'пальцы многоножки']
for i in range (5):
    print (y,ingredients[0+x])
    x=x+1
    y=y+1'''

weight = 100
year = 2019
for i in range (15):
    moon_weight = weight*0.165
    print ('Мой лунный вес в %s г. будет равен %s кг.' %(year,moon_weight))
    weight = weight+1
    year = year+1
print (list (range (1,1001)))