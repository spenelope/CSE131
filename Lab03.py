# 1. Name:
#     Penelope Sanchez
# 2. Assignment Name:
#     Lab 03 : Calendar Program
# 3. Assignment Description:
#      It will manually compute how to display the calendar for a given month without 
#      using Python's datetime (or any other) library. It will start by prompting the 
#      user for the numeric month and year to be displayed
# 4. What was the hardest part? Be as specific as possible.
#     The hardest thing for me was displaying the calendar start when it's a leap year
# 5. How long did it take for you to complete the assignment?
#     4 hrs


def get_month():
    while True: #Loop until user enter valid month
        try:
            month = int(input("Enter month (number): ")) #Input month
            if not 1 <= month <= 12: #Months 1-12
                print("The month has to be an integer between 1 & 12")
            else:
                return month 
        except ValueError: #If the month is not and integer
            print("Please type an integer")


def get_year():
    while True: #Loop until user enter valid year
        try:
            year = int(input("Enter year: ")) #input year
            if not year > 1752:
                print("The year has to be 1753 or later")
            else:
                return year
        except ValueError: #If the year is not and integer
            print("Please type an integer")


def name(month):
    months = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December",
    }
    return months.get(month, None)


def leap_year(year):
    return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


def days_in_month(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]: #Month w/31 days
        return 31
    elif month in [4, 6, 9, 11]: #Month w/30 days
        return 30
    elif month == 2 and leap_year(year): #If leap year Month w/29 days
        return 29
    else: #Non-leap year
        return 28


def days_months(month, year): #days between months
    days = 0
    for m in range(1, month):
        days += days_in_month(m, year) #days of each month
    return days


def days_years(year): #days between years
    days = 0
    while year > 1753:
        year -= 1
        days += 366 if leap_year(year) else 365 #Leap year w/366 days
    return days


def get_difference(month, year):
    days = days_years(year) + days_months(month, year) #No. of days since 1753
    weeks = days % 7 #No. of weeks since 1753
    difference = weeks % 7 #difference of days
    return difference


def display(month, year):
    
    difference = get_difference(month, year) #Find difference
    days = days_in_month(month, year) #days in the month
    columns = difference + 1

    print("{}, {}".format(name(month), year)) #show name & year
    print("%4s%4s%4s%4s%4s%4s%4s" % ("Su", "Mo", "Tu", "We", "Th", "Fr", "Sa")) #show weekdays
    if difference == 6:
        columns = 0
    else:
        while difference >= 0:
            print("%4s" % (" ",), end="")
            difference -= 1
    for day in range(1, days + 1): #days 1,2,3 ... 30
        if columns == 6:
            print("%4d" % (day,))
            columns = 0
        else:
            print("%4d" % (day,), end="")
            columns += 1
    print()


if __name__ == "__main__":

    month = get_month()
    year = get_year()

    print("\nGregorian Calendar of:")
    display(month, year)