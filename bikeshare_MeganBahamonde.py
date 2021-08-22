import time
import pandas as pd
import numpy as np

# Creates Dictionary for Various Cities

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
   
    city = ''
    city_list = CITY_DATA.keys()
    
    while city not in city_list:
        print('\nWhich city would you like to see information for?')  
        print('\nPlease input ONE of the following: Chicago, New York City, or Washington')
        city = input().lower()
        
        if city not in city_list:
            print('\nI\'m sorry, the city you would like to see information for is not available')
            print('\nPlease try again by using the cities available (Chicago, New York City, or Washington)')
            
    print('\nGreat! You\'ve selected {} as your city'.format(city.title()))
    
    
    # get user input for month (all, january, february, ... , june)
    
    month = ''
    month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    
    while month not in month_list:
        print('\nWhich month would you like to see information for?')  
        print('\nThe available months are: January, February, March, April, May, or June')
        print('\n*Please input "all" if you would like to see information for all months')              
        month = input().lower()
              
        if month not in month_list:
            print('\nI\'m sorry, the month you would like to see information for is not available')
            print('\nPlease try again by using the months available (January, February, March, April, May, or June)')
              
    print("\nThanks! You have selected {} as your month".format(month.title()))
              
    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = ''
    day_list = ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all']
    
    while day not in day_list:
        print('\nWhich day would you like to see information for?')  
        print('\n*Please input "all" if you would like to see information for all days')              
        day = input().lower()
              
        if day not in day_list:
            print('\nI\'m sorry, the day you would like to see information for is not available')
            print('\nPlease try again by using the days available (Monday through Sunday)')
              
    print("\nThanks! You have selected to veiw information on {}, during {} month(s), and {} day(s)".format(city.title(), month.title(), day.title()))
    print('-'*40)
    return city, month, day

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
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_dict = {1: 'January', 2: 'February', 3: 'March', 4:'April', 5: 'May', 6: 'June'}
    popular_month_no = df['month'].mode()[0]
    popular_month = month_dict[popular_month_no]
    print('\nThe most popular month to travel is {}'.format(popular_month))
    
    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('\nThe most popular day to travel is {}'.format(popular_day.title()))

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('\nThe most popular hour is {}'.format(popular_hour))

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('\nThe most popular start station is {}'.format(popular_start_station))

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('\nThe most popular end station is {}'.format(popular_end_station))

    # display most frequent combination of start station and end station trip
    df['Start & End Station'] = df['Start Station'].str.cat(df['End Station'], sep=" and ")
    popular_start_end_station = df['Start & End Station'].mode()[0]
    print('\nThe most popular route is between {}'.format(popular_start_end_station))    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    total_travel_hours = int(total_travel_time // 60)
    total_travel_minutes = int(total_travel_time % 60)
    print('\nThe total travel time is {} hours and {} minutes'.format(total_travel_hours, total_travel_minutes))

    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_travel_hours = int(mean_travel_time // 60)
    mean_travel_minutes = int(mean_travel_time % 60)
    print('\nThe average travel time is {} hours and {} minutes'.format(mean_travel_hours, mean_travel_minutes))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('\nThe user type stats are as follows:\n')
    print(df['User Type'].value_counts())
    
    # Display counts of gender
    try:
        print('\nThe gender stats are as follows:\n')
        print(df['Gender'].value_counts())
    except:
        print('\nThere are no gender stats for this city\n')
        
    # Display earliest, most recent, and most common year of birth
    try:
        print('The date of birth stats are as follows:\n')
        print('  The earliest birth year is:', int(df['Birth Year'].min()))
        print('  The latest birth year is:', int(df['Birth Year'].max()))
        print('  The most common birth year is:', int(df['Birth Year'].mode()[0]))
    except: 
        print('\nThere are no birth stats for this city\n')
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_raw_data(df):
    """ Asks users if they'd like to see the raw data """
    i = 0
    raw = input('Would you like to see the raw data? (Yes/No)\n').lower() # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df[i:i+5]) # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input('Would you like to see five more rows? (Yes/No)').lower() # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        
        try:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break
        except:
            print('\nThe word you entered is invalid.  Please enter yes or no')

if __name__ == "__main__":
	main()
