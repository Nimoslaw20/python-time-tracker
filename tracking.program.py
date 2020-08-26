import csv    # for csv files
from datetime import datetime
import time


user_project_name = input(
    'Please enter the name for the project: ')

# Start time
try:
    user_start_datetime = input(
        'Please enter start date time for the task in format  11/22/06 16:30: ')
    actual_start_time = datetime.strptime(
        user_start_datetime,  "%m/%d/%y %H:%M")
except:
    print("Kindly use the date format provided in the instruction")
    user_start_datetime = input(
        'Please enter start date time for the task in format  11/22/06 16:30: ')
    actual_start_time = datetime.strptime(
        user_start_datetime,  "%m/%d/%y %H:%M")


try:
    user_end_datetime = input(
        'Please enter end date time for the task in format  11/22/06 16:30: ')
    actual_end_time = datetime.strptime(
        user_end_datetime,  "%m/%d/%y %H:%M")
except:
    print("Kindly use the date format provided in the instruction")
    user_end_datetime = input(
        'Please enter end date time for the task in format  11/22/06 16:30: ')
    actual_end_time = datetime.strptime(
        user_end_datetime,  "%m/%d/%y %H:%M")

print(actual_start_time)
print(actual_end_time)
time_spent = actual_end_time - actual_start_time
print(time_spent)

print("days in time spent: ", time_spent.days)
print("seconds in time spent: ", time_spent.seconds)
hours_spent = (time_spent.days*24) + (time_spent.seconds / 3600)
print("The project name is ", user_project_name)
print("The time spent is: " + "{}".format(hours_spent))
# print(hours_spent)
amount_money_earned = hours_spent*5
print("The amount of money earned is: $" +
      "{:.2f}".format(amount_money_earned))


with open('tracker.csv', 'a', newline='') as obj:
    # creating excel field names
    fieldnames = ['Project Name', 'Start Date_Time', 'End Date_Time',
                  'Time Spent', 'Amount of Money']
    write = csv.DictWriter(obj, dialect='excel', quotechar='|',
                           quoting=csv.QUOTE_MINIMAL, fieldnames=fieldnames)
# set them as headers.
    write.writeheader()

# creating row with their header and value.
    write.writerow({'Project Name': user_project_name, 'Start Date_Time': user_start_datetime, 'End Date_Time': user_end_datetime,
                    'Time Spent': hours_spent, 'Amount of Money': amount_money_earned})
