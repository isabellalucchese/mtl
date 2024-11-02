def calculate_window_cost(window_U_Factor):
    if window_U_Factor == 2.90:
        return 0
    elif window_U_Factor == 1.20:
        return 184
    elif window_U_Factor == 1.21:
        return 485
    elif window_U_Factor == 0.80:
        return 295
    elif window_U_Factor == 0.81:
        return 622
    else:
        raise ValueError("Value of windows_U_Factor not valid")

def calculate_floor_cost(groundfloor_thermal_resistance):
    if groundfloor_thermal_resistance == 0.41:
        return 0
    elif groundfloor_thermal_resistance == 4.76:
        return 59.7
    elif groundfloor_thermal_resistance == 4.77:
        return 77
    elif groundfloor_thermal_resistance == 5.56:
        return 87.9
    elif groundfloor_thermal_resistance == 5.57:
        return 108
    else:
        raise ValueError("Value of groundfloor_thermal_resistance not valid")
    
def calculate_facade_cost(ext_walls_thermal_resistance):
    if ext_walls_thermal_resistance == 0.45:
        return 0
    elif ext_walls_thermal_resistance == 4.00:
        return 182
    elif ext_walls_thermal_resistance == 4.01:
        return 179
    elif ext_walls_thermal_resistance == 6.67:
        return 200
    elif ext_walls_thermal_resistance == 6.68:
        return 222
    else:
        raise ValueError("Value og ext_walls_thermal_resistance not valid")

def calculate_roof_cost(roof_thermal_resistance):
    if roof_thermal_resistance == 0.48:
        return 0
    elif roof_thermal_resistance == 4.55:
        return 89.5
    elif roof_thermal_resistance == 4.56:
        return 105
    elif roof_thermal_resistance == 8.33:
        return 101
    elif roof_thermal_resistance == 8.34:
        return 139
    else:
        raise ValueError("Value of roof_thermal_resistance not valid")

# Calculate total cost
def calculate_total_cost(window_U_Factor, groundfloor_thermal_resistance, ext_walls_thermal_resistance, roof_thermal_resistance):
    window_cost = calculate_window_cost(window_U_Factor=window_U_Factor)
    floor_cost = calculate_floor_cost(groundfloor_thermal_resistance=groundfloor_thermal_resistance)
    facade_cost = calculate_facade_cost(ext_walls_thermal_resistance=ext_walls_thermal_resistance)
    roof_cost = calculate_roof_cost(roof_thermal_resistance=roof_thermal_resistance)
    return window_cost + floor_cost + facade_cost + roof_cost