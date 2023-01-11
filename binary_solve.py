def fn(a, b):
    return a**2 + b**(1/3)

interval = 100000000
target = 0.025
x = 3
z = fn(x, interval/2)
tries = 0
l, m, r = -interval, 0, interval
print("Z Inical:", z)
while abs(z - target) > 0.000000001 and tries < 2000:
    z = fn(x, m)
    if z < target:
        l, m, r = m, (m+r)/2, r
    else:
        l, m, r = l, (l+m)/2, m
    tries += 1
    
print("Z final:", z)
print("Tentativas:", tries)
