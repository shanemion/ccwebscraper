import csv


def print_csv_as_dict(filepath):
    result = {}
    with open(filepath, 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # skip header row
        for row in reader:
            if row[1] == '':
                result[row[0]] = row[3]
        csvsorted_dict = dict(sorted(result.items()))

        print(csvsorted_dict)


print_csv_as_dict('/Users/shanemion/Downloads/CCSScontacts.csv')


