import calendar

if __name__ == "__main__":
    calendar.setfirstweekday(calendar.SUNDAY)
    # 2020 年的日历
    print(calendar.calendar(2020))
    # 是否是闰年
    print(calendar.isleap(1900))
    print(calendar.leapdays(1996,2010))
    # 2200 3月的日历
    print(calendar.month(2200,3))
    pass
