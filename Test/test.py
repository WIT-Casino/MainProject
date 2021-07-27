
import datetime
from datetime import timedelta
import random

def main():

    start_date = datetime.date(2018,1,1)
    end_date = datetime.date(2021,7,1)
    range_of_dates = end_date - start_date
    days_in_between = range_of_dates.days
    
    for _ in range(10):
        random_number_of_days = random.randrange(days_in_between)
        random_date = start_date + timedelta(days=random_number_of_days)
        date_in_int = int(random_date.strftime('%Y%m%d'))
        print(date_in_int)


    

if __name__ == "__main__":
    main()