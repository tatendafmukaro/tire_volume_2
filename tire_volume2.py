# Author Tatenda Felix Mukaro || April 2021 || CIT111 Assignment
#
import math
from datetime import datetime
current_date_time = datetime.now(tz = None)
#print (current_date_time)
date_today = current_date_time.date()

"""Prove that you can write a simple Python program 
that gets input from a user, performs arithmetic, 
and displays output for the user to see."""

# The following section prompts the user for different dimensions or values for tire sizes
first_number = float(input("Enter the width of the tire in mm (ex 205): "))
second_number = float(input("Enter the aspect ratio of the tire (ex 60): "))
third_number = float(input("Enter the diameter of the wheel in inches (ex 15): "))

w = round(first_number)
a = round(second_number)
d = round(third_number)
numerator = math.pi * w**2 * a * (w * a + 2540 * d)
denominator = 10000000
v  = numerator / denominator

# The section below is an addition of the requirements for week 2
# The following creates a new text file and them appends to it the 3 tyre dimensions of 
# from the input and prints it out for output

with open ("volume.txt", "at") as vol_file:
  print(f"{date_today},{w},{a},{d},{v: .1f}", file=vol_file)
 
print(f"The approximate volume is {v: .1f} milliliters")

# The following section defines the variables to be used by the conditional statements to determine prices and model
tyre_models = "Tyre Model"

tyre_type1 = "215/50R13" 
price1 = "R1,049.00"
tyre_type2 = "165/80R13" 
price2 = "R3,885.00"
tyre_type3 = "225/50R13"
price3 =  "R3,565.00"
tyre_type4 = "185/70R13"
price4 =  "R3,565.00"
 
 # Conditional statemens to determine price and model based from input
if (first_number == 215 and second_number == 50 and third_number == 13 ):
  print("")
  print(f"{tyre_models}, {tyre_type1},  {price1}")
elif (first_number == 165 and second_number == 80 and third_number == 13 ):
  print(f"{tyre_models}, {tyre_type2},  {price2}")
elif(first_number == 225 and second_number == 50 and third_number == 13 ):
  print(f"{tyre_models}, {tyre_type3},  {price3}")
elif (first_number == 185 and second_number == 70 and third_number == 13 ):
  print(f"{tyre_models}, {tyre_type4},  {price4}")
else :
  print(" Try Again")
  #print(f"{tyre_models}, {tyre_type5},  {price5}")

ask_user = input("Would you like to place an order for your tires?: ")
if (ask_user == "yes"):
  phone_number = int(input("Enter your phone number: "))
  with open ("volume.txt", "at") as vol_file:
    print(f"{date_today},{w},{a},{d},{v: .1f},{phone_number}", file=vol_file)
 

