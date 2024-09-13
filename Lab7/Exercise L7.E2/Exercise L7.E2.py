import os 
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
import matplotlib.pyplot as plt
from cs1033_evaluator import evaluate_lab7

MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE = input().split()
################################################################################
# Please do not edit anything above this line.

# Function to read a file and return speed list.
def get_speed(file_name):
    speed = []
################## YOUR CODE STARTS HERE. ######################################
# Read the file and get the values into the list.
    with open(file_name, 'r') as input_file:    # open input file, read and close it
        for line in input_file:
            try:
                col1, col2 = line.strip().split()   # get speeds to a list
                speed.append(col2)
            except ValueError:
                continue
################## YOUR CODE ENDS HERE. ########################################     
    return speed


# Function gets the filename and returns the speeds in metres per second format.
def convert_kmph_to_ms(filename):
################## YOUR CODE STARTS HERE. ######################################
# Read the values using get_speed function and return the converted values as a list.
    converted_speed_list = []
    speed_in_kmph = get_speed(filename)     # call get_speed function to get speeds in kmph
    
    for value in speed_in_kmph:
        converted_speed = (int(value) * 1000)/3600      # convert kmph to ms^(-1)
        converted_speed_list.append(converted_speed)    # append converted speeds to a new list
    
    return converted_speed_list
   
################## YOUR CODE ENDS HERE. ########################################


# Function gets the speeds as a list of integers in metres per second format and returns the acceleration.
def get_acceleration(speeds):
    #Acceleration list is initialized to zero.
    #i.e. acceleration at time=0 is zero.
    acceleration = [0]
################## YOUR CODE STARTS HERE. ######################################
    #Write the code to calculate the acceleration.  
    speeds = list(map(float, speeds))
    
    for i in range(len(speeds)-1):
        calculate_acceleration = (speeds[i+1] - speeds[i])/(100 * (10**(-3)))       # calculate acceleration
        acceleration.append(calculate_acceleration)
    
################## YOUR CODE ENDS HERE. ########################################
    return acceleration


######## WRITE THE CODE FOR TASK 1.4 and 1.5 BELOW #############################

        # Use MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE variable 
        # names instead of 'model1.txt', 'model2.txt', 'model3.txt' to read files
        
time_list = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
get_file_name = MODEL_1_INPUT_FILE, MODEL_2_INPUT_FILE, MODEL_3_INPUT_FILE
max_acceleration_list = []

for files in get_file_name:         # call each function to get information
    speed_in_meters_per_second = convert_kmph_to_ms(files)
    acceleration_in_square_meter_per_second = get_acceleration(speed_in_meters_per_second)
    max_acceleration = '%0.2f'%(max(acceleration_in_square_meter_per_second))    # get maximum acceleration while converting to two decimal points

    integer_part, decimal_part = max_acceleration.split('.')
    if (float(max_acceleration)-float(integer_part)) == 0.00:   # check whether decimal point value is zero
        max_acceleration_list.append('%0.1f'%(float(max_acceleration)))    # if above condition true return decimal point to one and append to a new list
    else:
        max_acceleration_list.append(max_acceleration)      # else append as it
        
output_file = open('max_acceleration.txt', 'w')     # open output file to enter data

for k in range(len(max_acceleration_list)):
    output_file.write(f'model{k+1} {str(max_acceleration_list[k])}\n')      # write maximum acceleration into the output file in given manner

output_file.close()     # close output file
# Plotting the lines with different styles
# plt.plot(time, model_acceleration[0] , label='model_1')      
x = time_list       # get time for the X-axes
y1 = get_acceleration(convert_kmph_to_ms(MODEL_1_INPUT_FILE))   # # get acceleration of each model for the Y-axes
y2 = get_acceleration(convert_kmph_to_ms(MODEL_2_INPUT_FILE))
y3 = get_acceleration(convert_kmph_to_ms(MODEL_3_INPUT_FILE))

plt.plot(x, y1, 'b--')   # plot model 1 graph in blue colour by using 'dashed' linestyle 
plt.plot(x, y2, 'r:')    # plot model 2 graph in red colour by using 'dotted' linestyle 
plt.plot(x, y3, 'g-.')   # plot model 3 graph in green colour by using 'dash dot' linestyle 
plt.legend(['model_1', 'model_2', 'model_3'])   # label each gragh with correspoding name as model_1, model_2, model_3
plt.yticks(range(int(min(*y1, *y2, *y3)), int(max(*y1, *y2, *y3))+10, 10))      # get Y-axes range from minimum acceleration to the (maximum acceleration+10)
# Adding labels and title
plt.xlabel('Time(s)')
plt.ylabel('Acceleration(ms-2)')
plt.title('Acceleration Vs Time')
plt.show()

################################################################################
# Please do not edit anything below this line.
evaluate_lab7()

##################### End of the programme #####################################
