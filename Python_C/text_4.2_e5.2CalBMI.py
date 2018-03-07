'''
height, weight = eval(input("请输入身高（米）体重（公斤）[中间用逗号分隔开]："))
bmi = weight / pow(height, 2)
print("BMI指数为{:.2f}".format(bmi))
wto, dom = "", ""
if bmi < 18.5:
    wto, dom = "偏瘦", "偏瘦"
elif bmi < 24:
    wto, dom = "正常", "正常"
elif bmi < 25:
    wto, dom = "正常", "偏胖"
elif bmi < 28:
    wto, dom = "偏胖", "偏胖"
elif bmi < 30:
    wto, dom = "偏胖", "肥胖"
else:
    wto, dom = "肥胖", "肥胖"
print("BMI指标为：国际{},国内{}".format(wto, dom))
'''

for s in "BIT":
    for i in range(10):
        print(s, end = "")
        if s == "I":
            break