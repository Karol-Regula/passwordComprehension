low = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cap = [x.upper() for x in low]
sym = ['!', '@', '#', '$', '%', '^', '&', '*']
num = [0, 1, 2, 3, 4 ,5 ,6 ,7, 8, 9]

#checks if password meets requirements (upper and lower letters and one number)
def task1(pass1):
  result = [0 if pass1[x] in low else 1 if pass1[x] in cap else 2 for x in range(len(pass1))]
  out = [1 if 0 in result and 1 in result and 2 in result else 0]
  #print out
  return out

def task2(pass1):
  return


p1 = "ababababbABABABABA217846127846"
p2 = "ababababab123"
p3 = "Aa1"
print task1(p1)
print task1(p2)
print task1(p3)





# pass1 = p1
# result = [0 if pass1[x] in low else 1 if pass1[x] in cap else 2 for x in range(len(pass1))]
# print [1 if 0 in result and 1 in result and 2 in result else 0]
# pass1 = p2
# result =
# print [1 if 0 in result and 1 in result and 2 in result else 0]
