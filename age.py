from datetime import datetime 
def age_calculator(given_date):
    #convert string into date format to get day, month and year (raise error if incorrect input)
    try: 
        given_date_format = datetime.strptime(given_date,"%d-%m-%Y").date()
    except ValueError:
        return("incorrect input, please input DD-MM-YYYY")
    #get current time
    current = datetime.now()
    #if current point in the year is earlier than the given date, remove 1 from difference in years
    #else the age is simply difference of years
    if (current.month<= given_date_format.month) and (current.day < given_date_format.day):
        age = current.year - given_date_format.year - 1
    else:
        age = current.year - given_date_format.year
    return age

