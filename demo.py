#basic syntax
print [i * i for i in range (1, 10)]
print [(i, i * i) for i in range (1, 10)]
print [{i: i * i} for i in range (1, 10)]

#conditional comprehensions
print [ (i, i * i) for i in range (1, 10) if i % 2 == 0] #even only

#ternary operators
x = 40
print 255 if x > 255 else x
x = 500
print 255 if x > 255 else x

print [i * i if i % 2 == 0 else 0 for i in range (1, 10)] #even only, else 0

print ''
#List of all multiples of 2 from 2 to 100
print [i for i in range (2, 100) if i % 2 == 0] #even only
print range(4, 100, 2)#start, end, step
print ''
#List of all multiples of 3 from 2 to 100
print [i for i in range (2, 100) if i % 3 == 0] #even only
print range(3, 100, 3)
print range(6, 100, 3)
print ''
#List of all the composite numbers from 2 to 100 (repeats are allowed)
print [i for i in range (2, 100) for j in range (2, i) if i % j == 0]
#print [i for i in range (2, 100) if i % j == 0 for j in range (2, 100)]

print ''
print [range(i * 2, 100, i) for i in range(2, 10)]
print ''
print sum([range(i * 2, 100, i) for i in range(2, 10)], [])#non 2d list method
print ''
print [not_a_prime for i in range(2,10) for not_a_prime in range (i * 2, 100, i)]#nested list comprehension
print ''
np = [not_a_prime for i in range(2,10) for not_a_prime in range (i * 2, 100, i)]
print [p for p in range(2, 100) if p not in np]

#print ''
#np2 = [not_a_prime for i in range(2,100) for not_a_prime in range (i * 2, 10000, i)]
#print [p for p in range(2, 10000) if p not in np2]
