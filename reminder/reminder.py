import datetime

user_input = input("enter your goal with it's deadline in this format goal:day.month.year \n").split(':')
date_time_str = user_input[1]
date_time_obj = datetime.datetime.strptime(date_time_str, '%d.%m.%Y')

print((date_time_obj.date() - datetime.datetime.now().date()).days)
