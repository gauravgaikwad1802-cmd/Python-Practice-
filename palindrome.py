def check_palindrome(number):
    original = number
    reverse = 0

    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10

    if original == reverse:
        return True
    else:
        return False
print(check_palindrome(121))

print(check_palindrome(234))

