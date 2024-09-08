from datetime import datetime
from cs1033_evaluator import evaluate_L6_E2

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

def create_NIC_number(data_list):
    ''' create NIC number using given instructions'''
    name_with_NIC = []
    submission_order = {}
    for line in data_list:
        name, dob, gender = list(line.split(' '))       #seperate name, date of birth one by one in each line
        year = dob.split('-')[0]        # seperate year from the dob
        number_of_days = days_to_birthday(dob)

        if gender == 'M':
            days_count = number_of_days     # gender = 'M', number of days to the birth date from January 1st of that year dosn't change
            if len(str(days_count))!=3:     # make days_count into correct form(into three digits)
                days_count = "{:03d}".format(days_count)
        else:
            days_count = number_of_days + 500   # gender = 'M', add 500 number of days to the birth date from January 1st of that year

        if year not in submission_order:    # Keep in touch with the order of submission for each year
            submission_order[year] = 1
        else:
            submission_order[year] += 1

        last_digits = str("{:03d}".format(submission_order[year]))  
        NIC = year+str(days_count)+last_digits      # # concatenate all numbers to generate NIC number
        
        name_with_NIC.append(name+' '+NIC)     # get name and correspoding NIC number into one list
    
    return name_with_NIC

get_input_file = input()      # get the input file
with open(get_input_file, 'r') as input_file:       # open input file, write and close it
    data_list = input_file.read().split('\n')        # get data from input file

names_with_NICs_list = create_NIC_number(data_list)

output_file = open('output.txt', 'w')       # open output file in writing mode 

output_file.write('\n'.join(names_with_NICs_list))        # enter name and nic numbers to the output file
    
output_file.close()     # close output file
################################################################################
# Please do not edit anything below this line.
evaluate_L6_E2()

##################### End of the programme #####################################
