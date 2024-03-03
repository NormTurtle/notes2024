# print by skip the currect letter to its next letter in english alphabates
# e.g `abc` become `bcd`  as a=b,b=c,c=d
alphas = "abcdefghijklmnopqrstuvwxyz" # english has 26 letters
# here im musing modulo to repeat repeat back to starting position
# as the module of give value which is looping/wraping the word
# saving form  errro`out of range`
t = "omi" #  want `pnj` as output
a = 3

alphas.index(t[0]) # 14
alphas.index(t[1]) # 12
alphas.index(t[2]) # 8
alphas.index(t[3%a]) #14# without % modulo its out of range
# ^ now using above method of index retriving
w = ''
w = w + alphas[(alphas.index(t[0])+1)] # usgin `w +` im concanating values
w = w + alphas[(alphas.index(t[1])+1)]
w = w + alphas[(alphas.index(t[2])+1)]
c = w + alphas[(alphas.index(t[3%a])+1)] # using modulo to repeat back to word
c = c + alphas[(alphas.index(t[4%a])+1)] # using modulo to repeat back to word
c = c + alphas[(alphas.index(t[5%a])+1)] # using modulo to repeat back to word
c = c + alphas[(alphas.index(t[6%a])+1)] # using modulo to repeat back to word
c = c + alphas[(alphas.index(t[7%a])+1)] # using modulo to repeat back to word
c = c + alphas[(alphas.index(t[8%a])+1)] # using modulo to repeat back to word
print(w)  # pnj  🤸 got the output
#^ what if my value were out of range?
#> just use modulo
print(c)  # pnjpnjpnj   🧯 fix of out of range problem
