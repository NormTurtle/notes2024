# Number of opening parentheses of a given type is equal to the number of closing parentheses of the same type.
# An opening parenthesis cannot be immediately followed by a closing parenthesis of a different type.
# Every opening parenthesis should be eventually closed by a closing parenthesis of the same type.
def balanced(word):
    """
    Determine if a string is balanced
    Argument:
        word: string
    Return:
        result: bool
    """
    c_c = [ '}' ]
    c_b = [ ']' ]
    c_p = [ ')' ]
    word = list(word)
    bracket = False
    curly = False
    parent = False
    br_next_i = word.index('[') + 1
    if '[' in word:
        if word[br_next_i] != c_c and word[br_next_i] != c_p:
            if ']' in word:
             bracket = True
    if '{' in word:
        if word[br_next_i] != c_b and word[br_next_i] != c_p:
            if '}' in word:
             curly = True
    if '(' in word:
        if word[br_next_i] != c_b and word[br_next_i] != c_c:
            if ')' in word:
             parent= True

    return bracket and curly and parent


print(balanced('([{}])'))
