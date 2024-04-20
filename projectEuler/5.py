function reverse(n)
reversed = 0
while n > 0
reversed = 10*reversed + n mod 10
n = n/10
return reversed
