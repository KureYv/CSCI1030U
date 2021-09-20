# 03 Loops

# x = 0

# while x < 10:
#     print('Hello')
#     x += 1
#
# for x in range(30,10, -2): #range(start, stop, step)
#     print(x)

pi_estimate = 0.0
for i in range(1,10000000):
    term = (-1)**i/(2*i-1)
    pi_estimate += term
print(f'An estimate for Pi is {pi_estimate * -4}')


# infinite Loop:
# while True:
#    print('Hello')