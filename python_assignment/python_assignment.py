'''
qn0
making a grading system to evaluate the given marks.
'''

all_marks =[23,4,5,6,64,90,67,98,45,23,67,78,89]

marks_less = []
marks_greater = []
def arrannge_marks(all_marks):
    for mark in all_marks:

        if 90 <= mark <= 100:
            
            print(f'{mark} Excellent')
        elif  70 <= mark <= 89:
            
            print (f'{mark} Very Good')
        elif 60<= mark <= 69:
            
            print(f'{mark} Good')    
        elif 40<= mark <= 59:
            print(f'{mark} Poor')
        elif 20<= mark <= 39:
            
            print(f'{mark} Very Poor')
        else:
            print(f'{mark} Repeat')

    for x in all_marks:
        if x > 50:
            marks_greater.append(x)
        elif x < 50:
            marks_less.append(x)

    print(marks_greater)
    print(marks_less)

'''qn1'''
def make_capital():
    x=input('please type an input: ')
    z=x.upper()
    print(z)


'''qn2'''
def divideByFive(*args):
    x=[]
    for num in args:
        if hex(args)% hex(5)==0:
            x.append(args)
        else:
            print('wrong input')
    return x

'''qn4'''

def accountBalance(*args):
    balance=0
    for num in args:
        if num.keys()=={'D'}:
            balance += num['D']
        elif num.keys()=={'W'}:
            balance -= num['W']
        else:
            print('wrong input')
    return balance

''''''