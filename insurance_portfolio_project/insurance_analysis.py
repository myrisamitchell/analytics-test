"""
Codecademy insurance portfolio project.

Purpose:

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

main()
