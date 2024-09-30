#from cs1033_evaluator import evaluate_lab9

INPUT_FILE_NAME = input()
################################################################################
# Do not change anything above this line
################################################################################

# Enter your code here
# Use INPUT_FILE_NAME variable to read the file instead of 'contamination_analysis.txt'
import re

def check_for_conditions(category, elements):
    ''' check conditions.
        if condition satisfy remove those elements and keep rest.
        if criteria not meet return false and return all elements.
        if criteria meet, then return true and rest of elements after removing'''
    temp_elements = [ele.copy() for ele in elements]

    for element, no_of_molecules in category.items():
        found = False
        for ele in temp_elements:
            if ele[0] == element and int(ele[1]) >= no_of_molecules:
                found = True
                ele[1] = str(int(ele[1]) - no_of_molecules)     # substract number given in condition and get remain number of molecules
                if ele[1] == '0':       # if no. of molecules are zero then remove that molecule
                    temp_elements.remove(ele)
                break
        if not found:
            return False, elements
    return True, temp_elements

def categorizing_chemicals(elements):
    ''' criteria should be followed for categorizing chemicals'''
    category_Level_1 = {'S': 1, 'O': 4, 'Na': 1}
    category_Level_2 = {'S': 1, 'O': 3, 'Mg': 1}
    category_Level_3 = {'O': 2, 'Cl': 3}

    # check for level 1 conditions
    chemicals_in_level_1, remaining_molecules_level_1 = check_for_conditions(category_Level_1, elements)
    if chemicals_in_level_1:    # if chemical satisfy level 1 conditions, check for level 2 and level 3
        chemicals_in_level_2, _ = check_for_conditions(category_Level_2, remaining_molecules_level_1)
        chemicals_in_level_3, _ = check_for_conditions(category_Level_3, remaining_molecules_level_1)

        if chemicals_in_level_2 or chemicals_in_level_3:
            return 'Level_4'    # If any contaminant belongs to more than one category above then the chemical is categorized as ‘Level_4’.
        return 'Level_1'

    # check for level 2 conditions
    chemicals_in_level_2, remaining_molecules_level_2 = check_for_conditions(category_Level_2, elements)
    if chemicals_in_level_2:        # if chemical satisfy level 2 conditions, check for level 3
        chemicals_in_level_3, _ = check_for_conditions(category_Level_3, remaining_molecules_level_2)

        if chemicals_in_level_3:
            return 'Level_4'    # If any contaminant belongs to more than one category above then the chemical is categorized as ‘Level_4’
        return 'Level_2'

    # check for level 3 conditions
    chemicals_in_level_3, _ = check_for_conditions(category_Level_3, elements)
    if chemicals_in_level_3:
        return 'Level_3'
    
    return 'Level_0'   # If the contaminant doesn’t belong to any of the above categories then the chemical is categorized as ‘Level_0.

def get_data_from_input_file(file_name):
    chemical_formula = {}
    with open(file_name, 'r') as input_file:
        get_data = input_file.read().strip().split('\n')

    for data in get_data:
        chemical_name, molecular_structure = data.strip().split()
        molecular_formula = molecular_structure.split('-')
        sub_list = []
        for i in molecular_formula:
            number = re.findall(r'[0-9]+', i)
            if not number:
                number = ['1']
            element = re.findall(r'[a-zA-Z]+', i)

            sub_list.append([''.join(element), ''.join(number)])

        chemical_formula[chemical_name] = sub_list

    return chemical_formula

chemical_formula = get_data_from_input_file(INPUT_FILE_NAME)

Level_0 = ['Level_0']
Level_1 = ['Level_1']
Level_2 = ['Level_2']
Level_3 = ['Level_3']
Level_4 = ['Level_4']
Level_5 = ['Level_5']

for chemical_name, elements in chemical_formula.items():
    level = categorizing_chemicals(elements)
    if level == 'Level_0':
        Level_0.append(chemical_name)
    elif level == 'Level_1':
        Level_1.append(chemical_name)
    elif level == 'Level_3':
        Level_3.append(chemical_name)
    else:
        Level_4.append(chemical_name)
        
final_list = []
final_list.append(Level_0)
final_list.append(Level_1)
final_list.append(Level_2)
final_list.append(Level_3)
final_list.append(Level_4)

for file in range(len(final_list)):
    with open(final_list[file][0], 'w') as output_file:
        output_data = final_list[file][1:]
        output_file.write('\n'.join(map(str,output_data)))
   
    
################################################################################
# Do not change anything below this line.
#evaluate_lab9()
