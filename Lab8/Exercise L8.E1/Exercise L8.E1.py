#from cs1033_evaluator import evaluate_lab8
# Please do not edit anything above this line.
################################################################################


# Your code should be included here. 
# You should define and use the analyseSeriesCircuit(), analyseParallelCircuit() functions in your solution.
import math
def get_angular_frequency(f):
    """calculata corresponding angular frequency"""
    angular_frequency = 2 * math.pi * int(f)
    return angular_frequency

def get_impedance_of_inductor(angular_frequency, L):
    """calculate magnitude of impedance of the inductor"""
    impedance_of_inductor = angular_frequency * (int(L) * (10**(-3)))
    return impedance_of_inductor

def get_impedance_of_capacitor(angular_frequency, C):
    """calculate magnitude of impedance of the capacitor"""
    impedance_of_capacitor = 1/(angular_frequency * (int(C) * (10 ** (-6))))
    return impedance_of_capacitor

def get_current_through_circuit(V, Z_total):
    """calculate current through the circuit"""
    current = int(V)/Z_total
    return current

def get_angle_between_voltage_and_current_series(impedance_of_inductor, impedance_of_capacitor, R):
    """In a serires connection find phase angle between voltage and current in radian and convert it to degrees"""
    angle_series = (180/math.pi) * (math.atan((impedance_of_inductor - impedance_of_capacitor)/ int(R)))
    return angle_series

def get_angle_between_voltage_and_current_parallel(impedance_of_inductor, impedance_of_capacitor, R):
    """In a parallel connection find phase angle between voltage and current in radian and convert it to degrees"""
    angle_parallel = (180/math.pi) * (math.atan(((1/impedance_of_inductor) - (1/impedance_of_capacitor)) * int(R)))
    return angle_parallel

def analyseSeriesCircuit(omega, L, C, R):
    """analyzing series R-L-C circuits and return Z_L, Z_C, Z_total, A, phase"""
    info_series_list = []
    
    Z_L = get_impedance_of_inductor(omega, L)
    Z_C = get_impedance_of_capacitor(omega, C)
    Z_total_series = ((int(R)**2) + (Z_L - Z_C)**2)**0.5
    I = get_current_through_circuit(V, Z_total_series)
    angle = get_angle_between_voltage_and_current_series(Z_L, Z_C, R)

    info_series_list = ['%0.1f'%Z_L] + ['%0.1f'%Z_C] + ['%0.1f'%Z_total_series] + ['%0.1f'%I] + ['%0.1f'%angle]     # rounded  to one decimal point and add them to one list
    return info_series_list

def analyseParallelCircuit(omega, L, C, R):
    """analyzing parallel R-L-C circuits and return Z_L, Z_C, Z_total, A, phase"""
    info_parallel_list = []
    
    Z_L = get_impedance_of_inductor(omega, L)
    Z_C = get_impedance_of_capacitor(omega, C)
    Z_total_parallel = 1/(((1/(int(R)**2)) + ((1/(Z_L)) - (1/(Z_C)))**2)**0.5)
    I = get_current_through_circuit(V, Z_total_parallel)
    angle = get_angle_between_voltage_and_current_parallel(Z_L, Z_C, R)

    info_parallel_list = ['%0.1f'%Z_L] + ['%0.1f'%Z_C] + ['%0.1f'%Z_total_parallel] + ['%0.1f'%I] + ['%0.1f'%angle]      # rounded  to one decimal point and add them to one list
    return info_parallel_list

get_input_file = input()    # get the input from the user
final_list = []
with open(get_input_file, 'r') as input_file:       # open input file, read and close it
    circuit_types = input_file.read().strip().split('\n')

    for data in circuit_types:
        Type, R, L, C, V, f = data.split(' ')       # get type, R,L,C,V and f for each circuit

        omega = get_angular_frequency(f)    # calculate angular frequency regarding to the given data
        
        if Type == 'series':        # check whether circuit is a series connection
            series_output_list = analyseSeriesCircuit(omega, L, C, R)   # calculate each value for a series connection
            final_list.append(series_output_list)   # get all the value to one list
        else:               # check whether circuit is a parallel connection
            parallel_output_list = analyseParallelCircuit(omega, L, C, R)       # calculate each value for a parallel connection
            final_list.append(parallel_output_list)     # get all the value to one list

with open('result.txt', 'w') as output_file:    # open output file, read and close it
    for i in range(len(final_list)):
        output_file.write(' '.join(final_list[i]))       #output the following calculated values in a single line separated by spaces
        if i != len(final_list)-1:
            output_file.write('\n')     # print new line after a line

################################################################################
# Please do not edit anything below this line.
#evaluate_lab8()

##################### End of the programme #####################################
