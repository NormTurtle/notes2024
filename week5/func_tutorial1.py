# Q.!: Write a Python code using functions which
# calculates the number of upper case letters, lower case
# letters, total number of characters and number of words

import re


def up_cha(set):
    """
    finding the upper leeter characters
    """
    up_cha = 0
    for e in set:
        if(e.isupper()):
            up_cha += 1
    return up_cha
def low_cha(set):
    """
    find lower case characters
    """
    low_cha = 0
    for e in set:
        if(e.islower()):
            low_cha += 1
    return low_cha
def t_cha(set):
    """
    find the total characters count
    """
    t_cha = 0
    for c in set:
        t_cha += 1
    return t_cha
def T_word(sen):
    if len(sen)==0:
       return ("invalid sentence")
    else:
        words = 1
        for c in sen:
            if (c == ' '):
                words += 1
        return words
sen = "First Second Third"
Usen = up_cha(sen)
print(f"it have {Usen} uppercase letter")
Lsen = low_cha(sen)
print(f"it have {Lsen} lowercase letter")
Tsen = t_cha(sen)
print(f"it has {Tsen} total letter")
Wsen = T_word(sen)
print(f"it has {Wsen} total word")
