#FizzBuzz problem
#Write a function called fizzbuzz that takes a number
#if divisible by 3 return Fizz
#if divisible by 5 return Buzz
#if divisible by both return 'FizzBuzz'
#if not, return the number

def fizz_buzz(num):
    if num % 15 == 0:
        return 'FizzBuzz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    else:
        return num 