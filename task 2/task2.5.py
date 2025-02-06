def is_palindrome(n):
    return str(n) == str(n)[::-1]

palindromes = [n for n in range(1, 100) if is_palindrome(n)]

result = [n for n in palindromes if is_palindrome(n**2)]

print("Числа, які є паліндромами і їхні квадрати теж паліндроми:")
for num in result:
    print(f"{num}^2 = {num**2}")
