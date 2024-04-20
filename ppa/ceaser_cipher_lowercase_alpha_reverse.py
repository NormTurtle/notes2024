import string as st
n = 'abc'
n = list(n)
alpha = st.ascii_lowercase
cipher = []
# ix = 0
for i,v in enumerate(n):
    ix = alpha.index(str(v)) +1
    cipher.append(alpha[-ix])


ci = ''.join(cipher)
print(ci)
