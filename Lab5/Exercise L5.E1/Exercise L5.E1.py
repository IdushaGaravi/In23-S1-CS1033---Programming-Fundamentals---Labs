# Exercise L5.E1

def get_min_max_number(numbers):
    ''' find minimum and maximum values'''
    float_numbers=list(map(float,numbers))
    min_index = float_numbers.index(min(float_numbers))   # find index of minimum value
    max_index = float_numbers.index(max(float_numbers))   # find index of maximum value

    print(f"Minimum = {numbers[min_index]}")
    print(f"Maximum = {numbers[max_index]}")

numbers = input().split()   # get numbers separated by white spaces entered from the keyboard
if len(numbers)==10:    # check whether input has 10 numbers
    get_min_max_number(numbers)

