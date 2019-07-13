'''def zahod (i):
    print ('Privet',i)
for i in range (1,18):
    zahod(i)'''
'''x= 'Pil'
y= 'Mil'
def simplefunction (name,name2):
    print ('Hello, %s %s!' % (name,name2))
simplefunction (x,y)'''
'''def savings (salary,passive_revenue,spendings):
    return (salary+passive_revenue-spendings)
print (savings(10,10,5))'''

'''def variable_test ():
    first_variable = 10
    second_variable = 20
    return (first_variable*second_variable)
print(variable_test())'''

def building_spaceship (cans):
    total_cans = 0
    for week in range (1,53):
        total_cans = cans+total_cans
        print ('Week %s , result %s' % (week,total_cans))
building_spaceship(5)
