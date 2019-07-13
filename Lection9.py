'''
#abs
print(abs(10))
print(abs(-10))
steps = -3
if abs(steps) > 0:
    print('Персонаж двигается')
#bool
print(bool(0))
print(bool(1))
print(bool(-100))
print(bool(1000))
print(bool(None))
print(bool("a"))
print(bool(" "))
print(bool('Как назвать свинью на соревнованиях по карате? \n Свинная отбивная!'))
my_silly_list = []
print(bool(my_silly_list))
my_silly_list = ['s', 'i', 'l', 'l', 'y']
print(bool(my_silly_list))'''
'''year = input('Введите год рождения:')
if bool(year.rstrip()):
    print('Ваш год рождения - %s' %(year))
if not bool(year.rstrip()):
    print('Вам следует ввести год рождения')'''
# dir/help
'''print(dir(['Это', 'Короткий', 'Список']))'''
'''popcorn = 'Еда для кино'
print(dir(popcorn))
help(popcorn.upper)'''
# eval exec
'''calc = input('Введите выражение:')
print(eval(calc))'''
"""my_little_program = '''print('бутер')
print('с колбасой')'''
exec(my_little_program)"""
# float
'''print(float(12))
print(float('123.5555546548'))'''
'''your_age = input('Введите свой возраст')
age = float(your_age)
if age > 13:
    print('Вы старше, чем положено на %s лет' % (age - 13))
elif age > 0 and age <= 13:
    print('Ваш возраст подходит!')
else:
    print('Введите корректное значение')'''
'''print(int('123'))
print(int(123.1235))
# len
print(len('this is a test string'))
print(len(['s', 'i', 'l', 'l', 'y']))
print(len({'pigeon': 'garbige', 'horse':'cowboy', 'monkey':'tower'}))'''
'''fruit = ['яблоко', 'банан', 'клементин', 'питайя']
length = len(fruit)
for i in range(0,length):
    print('фрукт с индексом %s: %s' % (i, fruit[i]))'''
# min max
"""numbers = [5, 4, 10, 30, 22]
word = "vtorostepennost"
print(max(numbers))
print(max(word))
print(min(word))
my_number = 65
guys_numbers = [1, 7, 56, 24]
if max(guys_numbers) > my_number:
    print('Команда проиграла')
else:
    print('Ведущий проиграл')"""
# sum
'''print(sum(list(range(40, 20, -2))))'''
# open read w
test_file = open('C:\\Users\\Goo\\Desktop\\test.txt')
text = test_file.read()
print(text)
test_file = open('C:\\Users\\Goo\\Desktop\\my_file.txt', 'w')
test_file.write('Это тестовый файл, псина!')
test_file.close()
test_file = open('C:\\Users\\Goo\\Desktop\\my_file.txt')
print(test_file.read())
# homework task 1
a = abs(10) + abs(-10)
print(a)
b = abs(-10) + -10
print(b)
# homework task 2
x = "этот если способ вы плохо это подходит читаете для что-то шифрования пошло важных не сообщений так"
x = x.split()
for i in range (0, len(x), 2):
    print(x[i])
# homework task 3
file = open('C:\\Users\\Goo\\Desktop\\my_file.txt')
x = str(file.read())
copy_file = open('C:\\Users\\Goo\\Desktop\\copy_file.txt', 'w')
copy_file.write(x)
copy_file.close()
copy_file = open('C:\\Users\\Goo\\Desktop\\copy_file.txt')
print(copy_file.read())