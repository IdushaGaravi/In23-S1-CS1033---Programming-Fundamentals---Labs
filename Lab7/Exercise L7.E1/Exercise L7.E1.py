# Exercise L7.E1

get_input = input()     # get input file name from the user
with open(get_input, 'r') as input_file:
    data_list = input_file.read().split('\n')

D_max_list = []
S_max_list = []
length_list = []

for line in data_list:
    length, Youngs_Modulus, Moment_Of_Inertia, load = list(line.split(' '))
    length_list.append(length)

    D_max = ((float(load) * 1000) * ((float(length))**3))/(48 * (int(Youngs_Modulus) * (10**9)) * float(Moment_Of_Inertia))
    S_max = (((float(load) * 1000) * (float(length)))/(4 * float(Moment_Of_Inertia)))

    D_max_list.append('%0.6f'%D_max)
    S_max_list.append('%0.2f'%S_max)

for i in range(len(list(data_list))):
    print(f'Beam {i+1}: Length: {length_list[i]} m, Max Deflection: {D_max_list[i]} m, Max Bending Stress: {S_max_list[i]} Pa')
