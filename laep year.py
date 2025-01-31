def is_leap_year_modulo(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("it is leap year")
    else:
        print("not a leap year")
year_to_check = int(input("enter the year:"))
result_modulo = is_leap_year_modulo(year_to_check)
{result_modulo}