# readline reads line by line from line 0 to end line
# when it reaches end it return '' A empty string
f = open('100_lines.txt','r')

s = '0'
while(s != ''):
    s = f.readline()
    if s != '':
        n = int(s)
        if n == 100:
            print(f'{n} was found')
