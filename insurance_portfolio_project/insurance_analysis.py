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
    
def main():
    create_dicts(ages, 'insurance.csv', 'age')
    create_dicts(genders, 'insurance.csv', 'sex')
    create_dicts(bmis, 'insurance.csv', 'bmi')
    create_dicts(children, 'insurance.csv', 'children')
    create_dicts(smoker_stat, 'insurance.csv', 'smoker')
    create_dicts(region, 'insurance.csv', 'region')
    create_dicts(ins_charges, 'insurance.csv', 'charges')

main()
