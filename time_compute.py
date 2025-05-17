from math import log
your_year = input("请输入你的年龄：")
your_year = int(your_year)
your_day = your_year * 365
your_hour = your_day * 24
your_minute = your_hour * 60

total_years = your_year - 4
total_days = (your_year - 4) * 365
total_hours = (your_year - 4) * 365 * 24
total_minutes = (your_year - 4) * 365 * 24 * 60

if total_years <= 4:
    mental_years = 1
    mental_days = 1
    mental_hours = 1
    mental_minutes = 1
else:
    mental_years = 1/log(total_years)
    mental_days = 1/log(total_days)
    mental_hours = 1/log(total_hours)
    mental_minutes = 1/log(total_minutes)

print("你已经生活了", your_year, "年", "你当前的实际感知的一年时间实际是", mental_years, "年")
print("你已经生活了", your_day, "天", "你当前的实际感知的一天时间实际是", mental_days, "天")
print("你已经生活了", your_hour, "小时", "你当前的实际感知的一小时时间实际是", mental_hours, "小时")
print("你已经生活了", your_minute, "分钟", "你当前的实际感知的一分钟时间实际是", mental_minutes, "分钟")



