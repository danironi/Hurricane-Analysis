# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}


# test function by updating damages
def updated_damages(damage):
    updated_damages = []
    for i in damage:
        if "M" in i:
            i = float(i[:-1]) * 1000000
        elif "B" in i:
            i = float(i[:-1]) * 1000000000
        else:
            i = "Damages not recorded"
        updated_damages.append(i)
    return updated_damages


damages = updated_damages(damages)
print(
    "1. Returns a new list of updated damages where the recorded data is converted to float values and the missing data is retained as 'Damages not recorded'.->")
print("")
print(damages)
print(" ")


# 2
# Create a Table
def table(name, month, year, wind, area_affected, damage, death):
    table_dict = {}
    for (n, m, y, w, a, da, de) in zip(name, month, year, wind, area_affected, damage, death):
        table_dict[n] = {"Name": n, "Month": m, "Year": y, "Max Sustained Wind": w, "Areas Affected": a, "Damage": da,
                         "Death": de}
    return table_dict


print(
    "2. Constructs a dictionary made out of the lists, where the keys of the dictionary are the names of the hurricanes, and the values are dictionaries themselves containing a key for each piece of data (Name, Month, Year,Max Sustained Wind, Areas Affected, Damage, Death) about the hurricane.->")
print("")
print(table(names, months, years, max_sustained_winds, areas_affected, damages, deaths))
print(" ")
print(" ")


# Create and view the hurricanes dictionary
# 3
# Organizing by Year
def year_dict(hurricane):
    year_dict_list = {}
    for key, value in hurricane.items():
        if value["Year"] not in year_dict_list.keys():
            year_dict_list[value["Year"]] = [value]
        else:
            year_dict_list[value["Year"]].append(value)
            # print("This is it: ",value)

    return year_dict_list


print(
    "3. Converts the current dictionary of hurricanes to a new dictionary, where the keys are years and the values are lists containing a dictionary for each hurricane that occurred in that year.->")
print("")
print(year_dict(table(names, months, years, max_sustained_winds, areas_affected, damages, deaths)))
print(" ")
print(" ")


# create a new dictionary of hurricanes with year and key

# 4
# Counting Damaged Areas

# create dictionary of areas to store the number of hurricanes involved in
def count_area_affected(hurricane):
    count_dict = {}

    for key, value in hurricane.items():
        num = 1
        for area in value["Areas Affected"]:
            if area not in count_dict.keys():
                if area == "Bahamas":
                    count_dict["The Bahamas"] += 1
                else:
                    count_dict[area] = num
            else:
                count_dict[area] += 1
    return count_dict


print(
    "4. Counts how often each area is listed as an affected area of a hurricane. Store and return the results in a dictionary where the keys are the affected areas and the values are counts of how many times the areas were affected.(here there were keys as 'Bahamas' which I put together with the 'The Bahamas')->")
print("")
print(count_area_affected(table(names, months, years, max_sustained_winds, areas_affected, damages, deaths)))
print(" ")


# 5
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in
def most_affected_area(hurricane):
    # most_affected=max(hurricane, key=hurricane.get)
    # return most_affected
    all_values = hurricane.values()
    max_value = max(all_values)
    max_keys = {key: value for (key, value) in hurricane.items() if value == max_value}

    return "Areas affected by the most hurricanes: " + str(max_keys)


print("5. Finds the area affected by the most hurricanes, and how often it was hit.->")
print("")
print(most_affected_area(
    count_area_affected(table(names, months, years, max_sustained_winds, areas_affected, damages, deaths))))
print(" ")


# 6
# Calculating the Deadliest Hurricane

# find highest mortality hurricane and the number of deaths
def most_death(hurricane):
    max_death_dict = {}
    for key, value in hurricane.items():
        max_death_dict[key] = value["Death"]

    max_death = max(max_death_dict, key=max_death_dict.get)

    return "The hurricane that caused the greatest number of deaths is " + max_death + " with the number of " + str(
        max_death_dict[max_death])


print("6. Finds the hurricane that caused the greatest number of deaths, and how many deaths it caused.->")
print("")
print(most_death(table(names, months, years, max_sustained_winds, areas_affected, damages, deaths)))
print(" ")


# 7
# Rating Hurricanes by Mortality
# categorize hurricanes in new dictionary with mortality severity as key
def mortality_rate(hurricane):
    mortality_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for key, value in hurricane.items():
        if value["Death"] == 0:
            mortality_dict[0].append(value)
        elif 0 < value["Death"] <= 100:
            mortality_dict[1].append(value)
        elif 100 < value["Death"] <= 500:
            mortality_dict[2].append(value)
        elif 500 < value["Death"] <= 1000:
            mortality_dict[3].append(value)
        elif 1000 < value["Death"] <= 10000:
            mortality_dict[4].append(value)
        else:
            mortality_dict[5].append(value)
    return mortality_dict


print(
    "7. Rates hurricanes on a mortality scale according to the following ratings, where the key is the rating and the value is the upper bound of deaths for that rating.->")
print("")
print(mortality_rate(table(names, months, years, max_sustained_winds, areas_affected, damages, deaths)))
print(" ")


# 8 Calculating Hurricane Maximum Damage

# find highest damage inducing hurricane and its total cost
def most_costly_hurricane(hurricane):
    max_damage_dict = {}
    for key, value in hurricane.items():
        if value["Damage"] != "Damages not recorded":
            max_damage_dict[key] = value["Damage"]

    max_damage = max(max_damage_dict, key=max_damage_dict.get)

    return "The hurricane that caused the greatest damage is " + max_damage + " with $" + str(
        max_damage_dict[max_damage])


print("8. Finds the hurricane that caused the greatest damage, and how costly it was.->")
print("")
print(most_costly_hurricane(table(names, months, years, max_sustained_winds, areas_affected, damages, deaths)))
print(" ")
# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}


# categorize hurricanes in new dictionary with damage severity as key
def damage_rate(hurricane):
    damage_dict = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for key, value in hurricane.items():
        if value["Damage"] == 0 or value["Damage"] == "Damages not recorded":
            damage_dict[0].append(value)
        elif 0 < value["Damage"] <= 100000000:
            damage_dict[1].append(value)
        elif 100000000 < value["Damage"] <= 1000000000:
            damage_dict[2].append(value)
        elif 1000000000 < value["Damage"] <= 10000000000:
            damage_dict[3].append(value)
        elif 10000000000 < value["Damage"] <= 50000000000:
            damage_dict[4].append(value)
        else:
            damage_dict[5].append(value)
    return damage_dict


print(
    "9. Rates hurricanes on a damage scale according to the following ratings, where the key is the rating and the value is the upper bound of damage for that rating.->")
print("")
print("Damage rates and the belonging hurricanes: " + str(
    damage_rate(table(names, months, years, max_sustained_winds, areas_affected, damages, deaths))))