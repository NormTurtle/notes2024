def genPrime(n):
    primes = [ ]
    for nums in range(2,n):
        prime = True
        for sub_nums in range(2,nums):
            if nums % sub_nums == 0 :
                prime = False
                break
        if prime:
            primes.append(nums)
    return primes

# i guessed answer should be under 10000 primes which is real
big_factor_primes = [  ]
for primes in genPrime(10000):
    if 600851475143 % primes == 0 :
        big_factor_primes.append(primes)


print(big_factor_primes[-1]) # last one is the biggest factor which is also prime

# this code is slow too much
# output:
# 6857
