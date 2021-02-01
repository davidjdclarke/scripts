import pandas as pd
from matplotlib import pyplot as plt


def get_all_cases(data):
    data_keys = []
    for i in range(len(data)):
        if data[i] not in data_keys:
            data_keys.append(data[i])
    return data_keys


def percentage(death_numbers, prints=True):
    percent = (death_numbers['deaths'] / death_numbers['cases']) * 100
    if prints:
        print('Age Range: ' + str(age))
        print('Death Percentage: ' + str(percent) + '%')
    return percent


def numbers_by_range(age_range=0, print_statement=False):
    num_deaths = 0
    num_survivals = 0
    total = 0
    if age_range == 0:
        age_range = ['40s']
    for i in range(len(df["Age_Group"])):
        if df["Outcome1"][i] == 'Resolved' and df['Age_Group'][i] in age_range:
            num_survivals += 1
            total += 1
        elif df["Outcome1"][i] == 'Fatal' and df['Age_Group'][i] in age_range:
            num_deaths += 1
            total += 1

    if print_statement:
        print("Age Range: " + str(age_range))
        print('Total Cases: ' + str(total))
        print('Survived: ' + str(num_survivals))
        print('Deaths: ' + str(num_deaths))

    return {'deaths': num_deaths, 'cases': total, 'survivals': num_survivals, 'age_range': age_range}


def temp(df):
    dates = get_all_cases(df['Accurate_Episode_Date'])
    num_entries = len(dates)
    num_cases = len(df['Accurate_Episode_Date'])
    data = {'active_cases': [0]*num_entries, 'deaths': [], 'recoveries': [], 'total_deaths': [],
            'total_recoveries': [], 'total_cases': [], 'date': dates}

    active_id = []
    index = 0

    num_entries = len(df['Accurate_Episode_Date'])

    for i in range(len(data['date'])):
        if i > 0:
            data['active_cases'][i] = data['active_cases'][i-1]
        for j in range(num_cases):
            if df['Accurate_Episode_Date'][j] == data['date'][i]:
                data['active_cases'][i] += 1
                index += 1
                print(index)
        for case_id in active_id:
            if df['Test_Reported_Date'][case_id] == data['date'][i]:
                pass
                # data['active_cases'][i] -= 1

    return data


if __name__ == "__main__":
    df = pd.read_csv('conposcovidloc.csv')

    age_ranges = ['<20', '20s', '30s', '40s', '50s', '60s', '70s', '80s', '90s']
    data = {}

    '''for age in age_ranges:
        data[age] = numbers_by_range([age])
        percentage(data[age])

    data['total'] = numbers_by_range(age_ranges)'''

    '''info = df['Case_AcquisitionInfo']
    x = get_all_cases(info)'''

    x = temp(df)
