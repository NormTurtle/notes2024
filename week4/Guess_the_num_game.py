import random
n = (random.randint(1,500))
print("Welcome to guess the number game ")
print("PLEASE give your first guess ")
ask = int(input())
retry = 1
while ask != n:
    if n > ask :
        print("go little high\n ")
    else:
        print("go little low\n ")
    ask = int(input(""))
    retry += 1

if ask == n :
    print("🥳 u won")
