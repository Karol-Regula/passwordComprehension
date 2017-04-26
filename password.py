p1 = "ababababbABABABABA217846127846"
p2 = "ababababab123"
pass2 = "Aa1"


low = ['a', 'b']
cap = ['A', 'B']
#sym = ['!', '@']
num = [0, 1, 2, 3, 4 ,5 ,6 ,7, 8, 9]



pass1 = p1
result = [0 if pass1[x] in low else 1 if pass1[x] in cap else 2 for x in range(len(pass1))]
print [1 if 0 in result and 1 in result and 2 in result else 0]
pass1 = p2
result = [0 if pass1[x] in low else 1 if pass1[x] in cap else 2 for x in range(len(pass1))]
print [1 if 0 in result and 1 in result and 2 in result else 0]
