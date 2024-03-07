# Continue

list1 = range(4)  # 0,1,2,3
for x in list1:
    if x == 2:
        continue
    print(
        x
    )  # 0,1 ,3    | it skip the value 2 and continue after that till the range exist
