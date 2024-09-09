# Exercise L7.E1

get_input = input()     # get input file name from the user
with open(get_input, 'r') as input_file:    # open input file, write and close it
    data_list = input_file.read().split('\n')        # get data from input file

for i in range(len(data_list)):
    length, Youngs_Modulus, Moment_Of_Inertia, load = list(data_list[i].split(' '))      # get length, Youngs_Modulus, Moment_Of_Inertia, load for corresponding beam   

    D_max = ((float(load) * 1000) * ((float(length))**3))/(48 * (int(Youngs_Modulus) * (10**9)) * float(Moment_Of_Inertia))     # get the maximum deflection at the center of the beam
    S_max = (((float(load) * 1000) * (float(length)))/(4 * float(Moment_Of_Inertia)))       # get the maximum bending stress at the center of the beam

    print(f'Beam {i+1}: Length: {length} m, Max Deflection: {"%0.6f"%D_max} m, Max Bending Stress: {"%0.2f"%S_max} Pa')     # print the output in given form
