#!/usr/bin/env python3

def admin_login(username, password):
    # your code here
    if username == 'admin' and password == '12345':
        return "Access granted"
    elif username == 'ADMIN' and password == '12345':
        return "Access granted"
    else:
        return "Access denied"
    
admin_login('admin', '12345')
admin_login('ADMIN', '12345')
admin_login('sudo', '12345')

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif 40<= temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"
hows_the_weather(33)
hows_the_weather(99)
hows_the_weather(75)

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 ==0:
        return 'FizzBuzz'
    elif num % 3 ==0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return num
fizzbuzz(1)
fizzbuzz(2)
fizzbuzz(3)
fizzbuzz(4)
fizzbuzz(5)
fizzbuzz(15)    

def calculator(operation, num1, num2):
    # your code here
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1*num2
    elif operation == '/':
        return num1/num2
    else: 
        print('Invalid operation!')
        return None
    
calculator('+', 1,2)
calculator('-', 2, 1)
calculator('*', 2, 3)
calculator('/', 4, 2)
calculator('nope', 1, 2)
