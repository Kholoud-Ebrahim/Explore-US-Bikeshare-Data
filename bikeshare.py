import pandas as pd
import numpy as np
import time

CITY_DATA = {
    'chicago':'chicago.csv',
    'new york city':'new_york_city.csv',
    'washington':'washington.csv'
}


MONTH_DATA = { 'january': 1  ,'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}

WEEK_DATA = { 'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5,  'sunday': 6}


def get_filters():
    print("\n Hello! Let's explore some US bikeshare data !\n")
    #get user input for the city  
    city_selection=input("To view the available bikeshare data , kindly type:\n The  letter (a)for Chicago\n The letter (b)for New Yourk City\n The letter (c)for Washington\n").lower()
    while city_selection not in ["a","b","c"]:
        print("That's invalid input .")
      #asking again with the same input above
        city_selection=input("To view the available bikeshare data , kindly type:\n The letter (a)for Chicago\n The letter (b)for New Yourk City\n The letter (c)for Washington\n").lower()
   
    city_selections ={"a":'chicago',"b":'new york city',"c":'washington'}
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


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    # The most common month
    most_freq_month = df['month'].mode()[0]
    for num in MONTH_DATA:
        if MONTH_DATA[num]==most_freq_month:
            most_freq_month = num.title()
    print('Most popular month:  {}'.format(most_freq_month))

    # The most common day of week
    most_freq_day = df['day_of_week'].mode()[0]
    for num in WEEK_DATA:
        if WEEK_DATA[num]==most_freq_day:
            most_freq_day = num.title()
    print('Most popular day of week: {}'.format(most_freq_day))
    
    # The most common start hour
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    most_freq_hour = df['hour'].mode()[0]
    print('Most popular hour: {}'.format(most_freq_hour))
    df.drop('hour',axis=1,inplace=True)
    df.drop('day_of_week',axis=1,inplace=True)
    df.drop('month',axis=1,inplace=True)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("--*--"*10)
  
 
def station_stats(df):
    """the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # The most commonly used start station
    s_station=df['Start Station'].mode()[0]
    print('Start Station: {}'.format(s_station))

    # The most commonly used end station
    e_station=df['End Station'].mode()[0]
    print('End Station: {}'.format(e_station))

    # The most frequent combination of start station and end station trip
    most_freq_station_comb = df['Start Station'] + ' to ' + df['End Station']
    print('The most frequnt combination of start station and end station trip : {}'.format(most_freq_station_comb.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("--*--"*10)
    

def trip_duration_stats(df):
    """the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    travel_durations = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])

    # The total travel time
    td_sum = df['Trip Duration'].sum()
    sum_seconds = td_sum%60
    sum_minutes = td_sum//60%60
    sum_hours = td_sum//3600%60
    sum_days = td_sum//24//3600
    print('Total Duration: {} days, {} hours, {} minutes and {} seconds'.format(sum_days, sum_hours, sum_minutes, sum_seconds))

    # The avg travel time
    td_mean = df['Trip Duration'].mean()
    mean_seconds = td_mean%60
    mean_minutes = td_mean//60%60
    mean_hours = td_mean//3600%60
    mean_days = td_mean//24//3600
    print('Avg Duration: {} hours, {} minutes and {} seconds'.format(mean_hours, mean_minutes, mean_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print("--*--"*10)

    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # The counts of user types
    types_of_users = df.groupby('User Type',as_index=False).count()
    print('Number of types of users are {}'.format(len(types_of_users)))
    for i in range(len(types_of_users)):
        print('{}s: {}'.format(types_of_users['User Type'][i], types_of_users['Start Time'][i]))
    print("--*--"*10)

    # The counts of gender
    if 'Gender' not in df:
        print('No gender data for this city. ')
    else:
        gender_of_users = df.groupby('Gender',as_index=False).count()
        print('Number of genders of users mentioned in the data are {}'.format(len(gender_of_users)))
        for i in range(len(gender_of_users)):
            print('{}s: {}'.format(gender_of_users['Gender'][i], gender_of_users['Start Time'][i]))
        print('Gender data for {} users is not available.'.format(len(df)-gender_of_users['Start Time'][0]-gender_of_users['Start Time'][1]))
        print("--*--"*10)
    # The earliest, most recent, and most common year of birth
    if 'Birth Year' not in df:
        print('Data related to birth year of users is not available for this city.')
    else:
        birth = df.groupby('Birth Year', as_index=False).count()
        print('Earliest year : {}.'.format(int(birth['Birth Year'].min())))
        print('Most recent year: {}.'.format(int(birth['Birth Year'].max())))
        print('Most common year: {}.'.format(int(birth.iloc[birth['Start Time'].idxmax()]['Birth Year'])))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print("--*--"*10)

    
def display_data(df):
    disp = input('DO you like to read some of the raw data? (Yes) or (No): \n').lower()
    
    if disp=='yes':
        disp=True
    elif disp=='no':
        disp=False
    else:
        print('You did not enter a valid choice. Let\'s try that again. ')
        display_data(df)
        

    if disp:
        while 1:
            for i in range(5):
                print(df.iloc[i])
            disp = input('DO you like to read Another five? (Yes) or (No): \n').lower()
            if disp=='yes':
                continue
            elif disp=='no':
                break
            else:
                print('You did not enter a valid choice.')
                

def main():
  while True:
   filtered_values= get_filters()
   city,month,day =filtered_values
   print(filtered_values)

   df=load_data(city,month,day)
   time=time_stats(df)
   print(time)
    
   station= station_stats(df)
   print(station)
    
   trip_dur=trip_duration_stats(df)
   print(trip_dur)
    
   user=user_stats(df)
   print(user)
    
   dis_data=display_data(df)
   print(dis_data)
    
   restart = input('\nDO you like to restart? Enter (yes) or (no):\n').lower()
  
   if restart != 'yes' :
    break
      
    
if __name__ == "__main__":
    main()