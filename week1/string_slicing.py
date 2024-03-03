# Variable[START:STOP:STEP]
# string number start from 0,1,2
# in reverse it count as -1 becuase negative dont start with 0
# string slicining is non-inclusive
t = "string" # ring
print(t[2:])
t = "usami" #
print(t[0:2])  # stop do not include its endpoint
#^>> here i was hoping output to be `usa` but `a` is not include in end
# as the property of [XX:STOP:XX] pramameter in string slicing
t = "1234567890" # 13579
print(t[0:9:2])  # each letter in string is skip by 2 steps
# if u ignore to put some value it will take value as 0
t = "kureha" # kure
print(t[:4]) # it took default value to 0 of START
t = "konoe" # konoe
print(t[:]) # everything to be 0 of value

# using negative
t = "kinjirou" # jiro
print(t[-5:-1:]) # STOP skip to ahead value here
# by not including it self

# print in reverse
t = "subaru" # urabus
print(t[::-1])
