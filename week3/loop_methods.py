# not sure if its called `loop methods` but it maybe pretty close

# BREAK
#^> it break the execution of the loop
# # whehrever we put `break` in loop it stops the whole loop at all and jump to next code
# # for i in range(5):
# #     if i < 3:
# #         print(i)
# #         break
# #^here code will break at 2 and it will not reach the 3
#

# CONTINUE
#^> it skip the only that time of ERROR or some condition that is not matched
# it is usefull to make some operation perform
# or skip to next execution when the condition isn't matched.
for i in range(5):
    if i < 3:
        print(i, end = " ")  # 0 1 2
        continue
#^here code won't break even idk

# PASS
#^> it just mean ignore or just skip without careing what is happenig
#its like `null` operator in python whihc has NONE meaning
# its used as `<placeholder>` in python when we dont know what exact code has to be puted
# instead PASS is placed there as placeholder
