"""
Codecademy insurance portfolio project.

Purpose: To determine different averages of age, gender, bmi, children, smoker status, region, and insurance costs.

"""

import csv

ages = []
genders = []
bmis = []
children = []
smoker_stat = []
region = []
ins_charges = []

def create_dicts(lst, csv_file, column_name):
    with open(csv_file) as csv_info:
        csv_dict = csv.DictReader(csv_info)
        for row in csv_dict:
            lst.append(row[column_name])
        return lst

def ave_age(lst):
    total = 0
    for i in lst:
        total += int(i)
    return str(int((total/len(lst))))

def count_genders(lst):
    female = 0
    male = 0
    for i in lst:
        if i == 'female':
            female += 1
        else:
            male += 1
    all = female + male
    ratio_female = round((female / all), 2) * 100
    ratio_male = round((male / all), 2) * 100
    return female, male, ratio_female, ratio_male

def diff_regions(lst):
    new_regions = []
    for i in lst:
        if i not in new_regions:
            new_regions.append(i)
    return new_regions
    
def ave_ins_charges(lst):
    total_charges = 0
    for i in lst:
        total_charges += float(i)
    return round(total_charges / len(lst), 2)

def cost_by_region(lst1, lst2):
    region_cost_lst = list(zip(lst1, lst2))
    southwest_cost = 0
    sw_count = 0
    southeast_cost = 0
    se_count = 0
    northwest_cost = 0
    nw_count = 0
    northeast_cost = 0
    ne_count =0
    for i in region_cost_lst:
        if i[0] == 'southwest':
            southwest_cost += float(i[1])
            sw_count += 1
        elif i[0] == 'southeast':
            southeast_cost += float(i[1])
            se_count += 1
        elif i[0] == 'northwest':
            northwest_cost += float(i[1])
            nw_count += 1
        elif i[0] == 'northeast':
            northeast_cost += float(i[1])
            ne_count += 1
    ave_southwest = southwest_cost / sw_count
    ave_southeast = southeast_cost / se_count
    ave_northwest = northwest_cost / nw_count
    ave_northeast = northeast_cost / ne_count
    return round(ave_southwest, 2), round(ave_southeast, 2), round(ave_northwest, 2), round(ave_northeast, 2)

def main():
    create_dicts(ages, 'insurance_portfolio_project/insurance.csv', 'age')
    create_dicts(genders, 'insurance_portfolio_project/insurance.csv', 'sex')
    create_dicts(bmis, 'insurance_portfolio_project/insurance.csv', 'bmi')
    create_dicts(children, 'insurance_portfolio_project/insurance.csv', 'children')
    create_dicts(smoker_stat, 'insurance_portfolio_project/insurance.csv', 'smoker')
    create_dicts(region, 'insurance_portfolio_project/insurance.csv', 'region')
    create_dicts(ins_charges, 'insurance_portfolio_project/insurance.csv', 'charges')

    print("The average age is " + ave_age(ages) + " years old.")
    print("There are " + str(count_genders(genders)[0]) + " females and " + str(count_genders(genders)[1])
        + " males.")
    print(str(count_genders(genders)[2]) + "% of patients are female and " + str(count_genders(genders)[-1]) +
        "% are male.")
    unique_regions = diff_regions(region)
    print("The regions served by our insurance company include the " + (', '.join(unique_regions[:-1])) + " and " 
        + unique_regions[-1] + ".")
    print("The average yearly insurance cost is $" + str(ave_ins_charges(ins_charges)) + ".")
    print("The average cost for each region is: \nSouthwest: $" + str(cost_by_region(region,ins_charges)[0])
        + "\nSoutheast: $" + str(cost_by_region(region,ins_charges)[1]) + "\nNorthwest: $"
        + str(cost_by_region(region,ins_charges)[2]) + "\nNortheast: $" + str(cost_by_region(region,ins_charges)[-1]))
    print("Through this analysis, those living in the Southeast region tend to spend more on insurance.")
    


main()


