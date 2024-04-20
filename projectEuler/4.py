import time
a = time.time()
def checkPalindrome(A):
    return str(A) == str(A)[::-1]


palindrome_3_digit_multiple = 0
# going for 3 digit but in reverse
for i in range(999,99,-1):
    if i * 999 < palindrome_3_digit_multiple:  # without this code is slow
        break
    for j in range(999,99,-1):
        mult = i*j
        if checkPalindrome(mult) and mult > palindrome_3_digit_multiple:
            palindrome_3_digit_multiple = mult


print(palindrome_3_digit_multiple)
b = time.time()
print(b-a)


# output:
# 906609
