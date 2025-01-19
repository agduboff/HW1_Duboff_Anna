#define a function that takes molecular_weights and solutions_needed 
def calculate_solution_weights(molecular_weights, solutions_needed):
    #create an empty list for the output
    preparation = []
    for solution in solutions_needed:
        #split the list of solutions into chemical and concentration
        chemical, concentration = solution.split('-')
        #check if the chemical exists in molecular_weights
        if chemical in molecular_weights:
            #remove the M and make sure the numbers are numbers to do math
            concentrations = float(concentration[:-1])
            #calculate the weight of the compound in 1 liter solution in grams
            weight = molecular_weights[chemical] * concentrations
            preparation.append(f'{chemical}-{concentration}-{weight:.2f}g')
        else:
            preparation.append('unknown')
    return preparation

calculate_solution_weights(molecular_weights,solutions_needed)