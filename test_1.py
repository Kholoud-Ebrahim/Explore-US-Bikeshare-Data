import pandas as pd
import numpy as np
import time

CITY_DATA = {
    'chicago':'chicago.csv',
    'new york city':'new_york_city.csv',
    'washington':'washington.csv'
}

def get_filters():
    print("\n Hello! Let's explore some US bikeshare data !\n")
    #get user input for the city  
    city_selection=input("To view the available bikeshare data , kindly type:\n The  letter (a)for Chicago\n The letter (b)for New Yourk City\n The letter (c)for Washington\n").lower()
    while city_selection not in ["a","b","c"]:
        print("That's invalid input .")
      #asking again with the same input above
        city_selection=input("To view the available bikeshare data , kindly type:\n The letter (a)for Chicago\n The letter (b)for New Yourk City\n The letter (c)for Washington\n").lower()
   
    city_selections ={"a":'chicago',"b":'new yourk city',"c":'washington'}
    if city_selection in city_selections.keys():
        city=city_selections[city_selection] 
    
     #get user input for the month   
    months=["january","february","march","april","may","june","all"]
    month= input("\nTo filter {}'s data by a particular month, please type the month name or all for not filtering by month :\n -January  -February  -March  -April  -May  -June  -All\n".format(city.title())).lower()
    while month not in months :
      #asking again with the same input above
       print("That's invalid choice , please type a valid month name or all.")
       month= input("To filter {}'s data by a particular month, please type the month name or all for not filtering by month :\n -January  -February  -March  -April  -May  -June  -All\n".format(city.title())).lower()
         
      #get user input for the day
    days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday","all"]
    day= input("\nTo filter {}'s data by a particular day, please type the day name or all for not filtering by day :\n-Monday  -Tuesday  -Wednesday  -Thursday  -Friday  -Saturday  -Sunday  -All\n".format(city.title())).lower()
    while day not in days :
      #asking again with the same input above
       print("That's invalid choice , please type a valid month name or all.")
       day= input("\nTo filter {}'s data by a particular day, please type the day name or all for not filtering by day :\n-Monday  -Tuesday  -Wednesday  -Thursday  -Friday  -Saturday  -Sunday  -All\n".format(city.title())).lower()


    return (city,month,day)


z=get_filters()
print(z)