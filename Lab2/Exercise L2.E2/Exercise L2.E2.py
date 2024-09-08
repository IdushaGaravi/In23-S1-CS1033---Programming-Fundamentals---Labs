# Exercise L2.E2
y, m, d=list(map(int, input().split()))
if m<3:
    m=m+12
    y=y-1
    a = (2*m) + (6*(m + 1) // 10)
    b = y + (y//4) - (y//100) + (y//400)
    f1 = d + a + b +1
    f = f1%7
else:
    a = (2*m) + (6*(m + 1) // 10)
    b = y + (y//4) - (y//100) + (y//400)
    f1 = d + a + b +1
    f = f1%7
print(f)
