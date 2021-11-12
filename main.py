'''
Calculator for vacation time, overtime pay, and base pay 
'''
import math 


def get_hr_time(Time):
    Vac_Time = Time * 0.05 
    return Vac_Time

def overtime_pay(Time):
    if (Time > 40.0):
        over_pay = ((Time - 40.0)* 0.5)*15
        
    else :
        over_pay = 0
        print("You did not work enough hours to reive overtime")
    return over_pay
    
def cal_pay(Time):
    wage_pay = Time * 15
    return wage_pay

resp_repeat = 'Y'

while resp_repeat == 'Y':
    print("Please enter your time worked for the selected period.")
    hrTime = float(input())
    print("Congradulations, you have earned ", get_hr_time(hrTime), "hours of vacation time.")
    print("You have made $", overtime_pay(hrTime), "in overtime for the selected period.")
    print("This is in addition to your base pay of $", cal_pay(hrTime))

    print("Would you like to calculate for another pay period? (Y/N)")
    resp_repeat = str(input())



