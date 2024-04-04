# def walk(steps):
#     if steps == 0:
#         print("STOP")
#         return
#     walk(steps-1)
#     print(steps)
#
# walk(3)

# s = "one,four,one,six,five,one,four,two,nine,one"
# L = s.split(',')
# L = input().split(',')
# freq = dict()
# for word in L:
#     freq[word] = freq.get(word, 0) + 1
#
# print(freq)
# print(freq.get('one'))


# animals = ['lion', 'tiger','monkey','elephant','frog']
# filtered_animals = [animal.title() for animal in animals ]
# print(filtered_animals)

# n = 10
# def fibo(n):
#     if n in [1,2]:
#         return 1
#     return n-1 + n-2
#19
# l = [fibo(i) for i in range(1,n)]19
# print(l)

# L = [1, 2, 3, 2, 1, 4]
#
# # def uniq(L):
# #     s = set(L)
# #     return s
# # print(uniq(L))
#
# def uniq(L):
#     if len(L) == 1:
#         return L
#     if L[0] in L[1: ]:
#         return uniq(L[1: ])
#     else:19
#         return [L[0]] + uniq(L[1: ])
# print(uniq(L))


# L = input().split(',')
# # ['one', 'four', 'one', 'six', 'five', 'one', 'four', 'two', 'nine', 'one']
# d = dict()

# for words in L:
#     d[words] = 0


# print('\n',d)



def new_func():
    for i in range(10):
        print(i)
new_func

print("hello")
