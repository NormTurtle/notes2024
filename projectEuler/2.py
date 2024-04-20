 # a Fibonacci sequence is genrate by adding two previous terms
def fibo(n):
    l = [1,2]  # start with 1,2 as base value
    for _ in range(n):
        if l[-1] < 4_000_000:  # limit to 4 millon  of newlyl genrated fibo number
            l.append(l[-1] + l[-2]) # make list with last + second last number genrated so far
    return l

def even_value_in_list(L):
    list_of_even_values = [i for i in L if i % 2 ==0]
    return list_of_even_values

# u can make any threshold but i choose 100 for no reason since condino of 4 mil is fine
answer = sum(even_value_in_list((fibo(100))))
print(answer)

# output :
# 4613732
