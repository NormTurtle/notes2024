def int_to_eng(num):
    NumInEnDict = {
            0:"Zero",1:'One',2:"Two",3:"Three",4:"Four",
            5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",
            11:"Eleven",12:"Twelve",13:"Thirteen",14:'Fourteen',15:"Fifteen",
            16:"Sixteen",17:"Seventeen",18:"Eighteen",19:'Nineteen',20:"Twenty",
            30:"Thirty",40:"Fourty",50:"Fifty",60:'Sixty',70:"Seventy",
            80:"Eighty",90:"Ninety",100:"Hundred",1000:'Thousand'
            }
    if num <= 20 :
        return NumInEnDict[num]
    elif num == 100 or num == 1000:
        return 'One' + NumInEnDict[num]
    elif num % 100 == 0 :
        return NumInEnDict[num//100] + NumInEnDict[100]
    elif num > 20 and num < 100 :
        return NumInEnDict[(num//10 * 10)] + '' + int_to_eng(num%10)
    elif num > 100  and num < 1000:
        return NumInEnDict[num//100]+ '' + NumInEnDict[100] + 'and' + int_to_eng(num%100)


# l = []
# for n in range(1,1000+1):
#     l.append(int_to_eng(n))
# # print(l)
# ans = 0
# for i in l:
#     ans += len(i)
# print(ans)


print(int_to_eng(1000))
