from datetime import datetime

def days_to_birthday(date):
    '''
    Calculates the number of days that have passed since the 1st of January 
    to the given date.

    :param date: A date string in the format of yyyy-mm-dd
    :return: The number of days to the date from 1st of January 
             (eg: date->2021-01-01, return->1)
    '''

    # Convert the date string to a datetime object
    datetime_object = datetime.strptime(date, "%Y-%m-%d")

    # Extract only the date and remove the timestamp
    date = datetime_object.date()

    # Find the number of days since the begining of the year
    num_days = date.timetuple().tm_yday

    return num_days


# Please do not edit anything above this line.
################################################################################


# Your code should be included here. 
# You may use the days_to_birthday(date) function in your solution.
def generate_nic(intput_file, output_file):
    with open(intput_file, 'r'):
    
        lines = f.readlines()
    
    with open(output_file, 'w'):
        for line in lines:
            name, dob, gender = list.strip().split()
            
            year = dob.split('-')[0]
            
            if gender == 'M':
                days_to_birthday(date) == days_to_birthday(date)
            else:
                days_to_birthday(date) == days_to_birthday(date) + 500
                
            NIC = year+days_to_birthday(date)
            output_file.write(NIC)

input_file = 'intput.txt'  # Replace with your input file name
output_file = 'output.txt'  # Replace with your desired output file name

input_dates = days_to_birthday(input_file)        
generate_nic(input_dates, output_file)        

        

################################################################################
# Please do not edit anything below this line.
evaluate_L6_E2()

##################### End of the programme #####################################
