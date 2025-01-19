#define the function extract_parameter that takes the unit_operations_data dictionary, a unit_name, a parameter_name, and an index
def extract_parameter(unit_name, parameter_name, index): 
    #check for invalid inputs first to make sure function does not error and continues to run
    #check if unit_name is in the unit_operations_data dictionary
    if unit_name not in unit_operations_data:
        return "Invalid input"
    #check if parameter_name is found the unit
    feature_names = unit_operations_data[unit_name]
    if parameter_name not in feature_names:
        return "Invalid input"
    #check if the index is within range and return the name of the inputted unit operation, its desired feature name and value if it is
    feature_values = feature_names[parameter_name]
    if 0 <= index < len(feature_values):
        feature_value = feature_values[index]
        return f"{unit_name}_{parameter_name}_{feature_value}"
    else:
        return "Invalid input"