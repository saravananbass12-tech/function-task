# function series even 1

def series1():
    for i in range(2,17,2):
        print(i)
series1()


# function series reverse 2

def series2():
    for i in reversed(range(10,60,10)):
        print(i)
series2()


# function square 3

def square(a):
        print(a**2)
square(3)


# function cube 4

def cube(a):
    print(a**3)
cube(3)

# split digits digits one by  one 5

def split_digits(a):
    while a>0:
        last=a%10
        a=a//10
        print(last,end="")
split_digits(4327)


#armstrong number 6

def armstrong(n):
    original = n
    count = 0
    temp = n
    while temp > 0:
        count += 1
        temp = temp // 10  # Use // not /
    total = 0
    temp2 = n
    while temp2 > 0:
        last = temp2 % 10
        total += last ** count
        temp2 = temp2 // 10  # // gives integer, / gives float
    if total == original:
        print("armstrong number")
    else:
        print("not armstrong number")
armstrong(153)


# Spy number 7

def spy(n):
    temp = n
    s = 0
    p = 1

    while temp > 0:
        d = temp % 10
        s += d
        p *= d
        temp = temp // 10

    if s == p:
        print("Spy Number")
    else:
        print("Not Spy Number")

spy(1124)

# Square of each digit 8

def square_digits(n):
    while n > 0:
        d = n % 10
        print(d * d, end=" ")
        n = n // 10

square_digits(42316)


# Count digits 9

def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    print(count)
count_digits(34562)


# Count digits 10

def divisors(n):
    total = 0

    for i in range(1, n + 1):
        if n % i == 0:
            print(i)
            total = total + i

    print("Sum =", total)

divisors(10)


# Laptop discount 11

def price():
    return float(input("Enter Price: "))

def calculate_charge(price):
    if price >= 50000:
        discount = price * 0.10
    elif price >= 30000:
        discount = price * 0.05
    else:
        discount = price * 0.02

    print("Discount =", discount)
    print("Final Price =", price - discount)

p = price()
calculate_charge(p)


# Add integer and float 12

def values(a, b):
    print(a + b)

values(10, 5.5)

# Check capital letter 13

def capital(ch):
    if ch >= 'A' and ch <= 'Z':
        print("Capital Letter")
    else:
        print("Not Capital Letter")
capital('G')


# Check vowel or consonant 14

def vowel(ch):
    if ch in "AEIOUaeiou":
        print("Vowel")
    else:
        print("Consonant")
vowel('e')


# Convert to lowercase 15

def small_letter(ch):
    print(ch.lower())
small_letter('M')




