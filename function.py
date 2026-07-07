# 1. Check Even Number

def is_even(n):
    return n % 2 == 0

print(is_even(8))


# 2. Largest of Three Numbers

def largest(a, b, c):
    return max(a, b, c)

print(largest(10, 25, 15))


# 3. Factorial

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(5))


# 4. Reverse Number

def reverse_number(n):
    return int(str(n)[::-1])

print(reverse_number(1234))


# 5. Sum of Digits

def sum_of_digits(n):
    return sum(int(d) for d in str(n))

print(sum_of_digits(1234))


# 6. Count Even Digits

def count_even_digits(n):
    count = 0
    for d in str(n):
        if int(d) % 2 == 0:
            count += 1
    return count

print(count_even_digits(248135))


# 7. Palindrome Number

def is_palindrome(n):
    return str(n) == str(n)[::-1]

print(is_palindrome(121))


# 8. Second Largest in List

def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2]

print(second_largest([10, 20, 30, 40, 50]))


# 9. Remove Duplicates

def remove_duplicates(lst):
    return list(set(lst))

print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))


# 10. Count Vowels

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

print(count_vowels("Python Programming"))


# 11. Common Elements

def common_elements(list1, list2):
    return list(set(list1) & set(list2))

print(common_elements([1,2,3,4], [3,4,5,6]))


# 12. Prime Numbers

def prime_numbers(limit):
    primes = []
    for num in range(2, limit + 1):
        prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                prime = False
                break
        if prime:
            primes.append(num)
    return primes

print(prime_numbers(20))


# 13. Word Count

def word_count(sentence):
    return len(sentence.split())

print(word_count("Python is easy to learn"))


# 14. Highest Frequency Element

def highest_frequency(lst):
    return max(set(lst), key=lst.count)

print(highest_frequency([1,2,2,3,3,3,4,4]))


# 15. Swap Case

def swap_case(text):
    return text.swapcase()

print(swap_case("Python Programming"))
