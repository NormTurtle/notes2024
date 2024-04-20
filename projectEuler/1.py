# 1 : using loop
n = 1000 # num till to find multiples
answer = 0  # do no start with 0 , it will make everything 0
for num in range(n):
    # if number is divisible by 3 till n
    if num % 3 == 0 or num % 5 == 0 :
        answer = num + answer
print(answer)

# 2 : using set
print(sum(set(range(0,1000,3)) | set(range(0,1000,5))))
# | stand for union . like join all set with remove dupes(propertry of set)
# range start with 0 . { 0, 3 , 6 } jump of 3 digit

# 2 : using list
print(sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0 ]))
# creating list of all item multiple of 3 or 5. then sum() it



# output:
#233168
