import pickle
import csv


with open('sorted_dict.pkl','rb') as f:
    sorted_dict = pickle.load(f)


def print_csv_as_dict(filepath):
    result = {}
    with open(filepath, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # skip header row
        for row in reader:
            if row[1] == '':
                result[row[0]] = row[3]
        csvsorted_dict = dict(sorted(result.items()))

        return csvsorted_dict


dict2 = print_csv_as_dict('/Users/shanemion/Downloads/CCSScontacts.csv')


result_dict = {}
for key1, value1 in sorted_dict.items():
    for key2, value2 in dict2.items():
        if value1 == value2:
            result_dict[value2] = key1

        if value1 not in dict2.items():
            result_dict[value1] = key1


orgs = []
emails = []
count = 0
for org in result_dict:
    orgs.append(org)
    emails.append(result_dict[org])
    count += 1

print(orgs)
for org in orgs:
    new = ''
    for ch in org:
        if ch == '-':
            new += ' '
        else:
            new += ch
    print(new)

print("\n\n\n\n\n")

for email in emails:
    new = ''
    for ch in email:
        if ch == '-':
            new += ' '
        else:
            new += ch
    print(new)
    # print(email)



