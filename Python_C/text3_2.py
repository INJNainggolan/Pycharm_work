import math
dayup, dayfactor = 1.0, 0.01
for i in range(365):
    if i % 7 in [6, 0]:
        dayup = dayup * (1 + dayfactor)
    else:
        dayup = dayup * (1 - dayfactor)
print("向上5天向下2天的力量：{:.2f}.".format(dayup))