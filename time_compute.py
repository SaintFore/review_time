from math import log
your_year = input("请输入你的年龄：")
your_year = int(your_year) - 4

total_years = your_year
total_days = your_year * 365
total_hours = total_days * 24

if total_years <= 4:
    mental_years = 1
else:
    mental_years = 1/log(total_years)

mental_days = 1/log(total_days)
mental_hours = 1/log(total_hours)



print("你现在的对于一年实际感知是", mental_years, "年")
print("你现在的对于一天的实际感知是", mental_days, "天")
print("你现在的对于一小时的实际感知是", mental_hours, "小时")
