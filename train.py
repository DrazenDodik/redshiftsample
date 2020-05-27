import csv

with open('tr_test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if(len(row) > 1) :
                print(f'\tBuyer{row[0]} bought {row[1]} items')
                line_count += 1
    print(f'Processed {line_count} lines.')