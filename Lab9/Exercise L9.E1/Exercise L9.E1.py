import os 
os.environ['MPLCONFIGDIR'] = os.getcwd() + "/configs/"
#from cs1033_evaluator import evaluate_lab9
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

input_file_name = input()

# Your code should be included here. 
# Avoid using the print function in the code, as it may cause errors
def output_voltage_of_voltage_divider(V_in, R_1, R_2):
    ''' calculate Output Voltage of the Voltage Divider for given resistors R_1 and R_2 '''
    V_output = int(V_in) * (R_2/(R_1 + R_2))
    return V_output

def power_dissipation_through_resistors(V_in, R_1, R_2):
    ''' calculate Power dissipation through the resistors for given resistors R_1 and R_2 '''
    P = ((int(V_in))**2)/(R_1 + R_2)
    return P

def select_R_1_and_R_2_pairs(resistor_values, V_out_min, V_out_max):
    ''' select a pair of resistors with minimal power dissipation
        for a voltage divider circuit to achieve a specified output voltage
        within a given tolerance range'''
    selected_R_1_R_2 = {}
    min_P_R_list = []

    for i in range(len(resistor_values)):
        R_1 = resistor_values[i]
        select_R_2 = resistor_values[:i] + resistor_values[i+1:]    # get values for R_2 for the given values

        for R_2 in select_R_2:
            output_voltage = output_voltage_of_voltage_divider(V_in, R_1, R_2)  # calculate output voltage for each R_2

            if (float(output_voltage) >= V_out_min) and (float(output_voltage) <= V_out_max):   # check whether output voltage is in the range
                power_dissipation = power_dissipation_through_resistors(V_in, R_1, R_2)     # if so then, calculate power_dissipation

                if len(min_P_R_list) == 0:      # get the first set of values as minimal power dissipation
                    min_P_R_list.append(R_1)
                    min_P_R_list.append(R_2)
                    min_P_R_list.append('%0.6f'%power_dissipation)

                else:
                    if power_dissipation < float(min_P_R_list[2]):      # get correct minimal power dissipation comparing with previous set
                        min_P_R_list[0] = R_1
                        min_P_R_list[1] = R_2
                        min_P_R_list[2] = power_dissipation
              
    return min_P_R_list

with open(input_file_name, 'r') as input_file:      # open input file, read and close it
    get_data = list(input_file.read().split('\n'))  
    V_in, V_out, t = get_data[0].split(',')     # get input voltage, output voltage and tolerence
    resistors = get_data[1].split(',')      # get the values of the resistors
    
    resistor_values = []
    for res_values in resistors:
        resistor_values.append(int(res_values))

    V_out_min = int(V_out) - float(t)       # calculate output voltage within a given tolerance range
    V_out_max = int(V_out) + float(t)

    R_1_R_2_pairs = select_R_1_and_R_2_pairs(resistor_values, V_out_min, V_out_max)

    output_list = R_1_R_2_pairs[:2]     # get the pair of resistors with minimal power dissipation
with open('output.txt', 'w') as output_file:    # open output file, read and close it
    output_file.write(", ".join(map(str, output_list)))

# Part 2

def get_R_2_R_L_equivalent_resistor(output_list):
    ''' calculate equivalent resistor for the parallel resistors R_2 and R_L'''
    R_2 = output_list[1]
    equivalent_resistor_list = []
    for R_L in range(10, 1001, 10):
        calculate_R_eq = (R_2 * R_L)/(R_2 + R_L)
        equivalent_resistor_list.append('%0.6f'%calculate_R_eq)
    return equivalent_resistor_list

def get_new_voltage(V_in, output_list):
    ''' calculate new output voltage varies with load resistance'''
    R_1 = output_list[0]
    R_2 = output_list[1]

    R_eq = get_R_2_R_L_equivalent_resistor(output_list)

    new_voltage = []
    for resistor_eq in R_eq:
        get_new_Voltage = int(V_in) * (float(resistor_eq)/(R_1 + float(resistor_eq)))
        new_voltage.append(get_new_Voltage)

    return new_voltage

V_new = get_new_voltage(V_in, output_list)

x = [R_L for R_L in range(10, 1001, 10)]    # get R_L values for the x-axes
y = V_new   # get new output voltage values for y-axes

plt.plot(x, y)
plt.xticks(range(0, 1100,100))      # get x-axes range from 10 to 1010
plt.yticks(range(0,5))      # get y-axes range from 1 to 5

# Adding labels and title
plt.xlabel('Resistance(ohms)')
plt.ylabel('Voltage(V)')
plt.title('Voltage vs Resistance')
plt.grid()      # draw grid lines in the graph
plt.minorticks_on()
plt.gca().xaxis.set_minor_locator(AutoMinorLocator(10))
plt.show()
################################################################################
# Please do not edit anything below this line.
#evaluate_lab9()

##################### End of the programme #####################################
