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
    pass
    total = 0
    for i in lst:
        total += int(i)
    return str(int((total/len(lst))))
    
def main():
    create_dicts(ages, 'insurance_portfolio_project/insurance.csv', 'age')
    create_dicts(genders, 'insurance_portfolio_project/insurance.csv', 'sex')
    create_dicts(bmis, 'insurance_portfolio_project/insurance.csv', 'bmi')
    create_dicts(children, 'insurance_portfolio_project/insurance.csv', 'children')
    create_dicts(smoker_stat, 'insurance_portfolio_project/insurance.csv', 'smoker')
    create_dicts(region, 'insurance_portfolio_project/insurance.csv', 'region')
    create_dicts(ins_charges, 'insurance_portfolio_project/insurance.csv', 'charges')

    print("The average age is " + ave_age(ages) + ".")

main()
