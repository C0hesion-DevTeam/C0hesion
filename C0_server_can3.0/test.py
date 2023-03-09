import csv

# Open the CSV file for reading and writing
with open('teams_request.csv', 'r+') as csv_file:
    csv_reader = csv.reader(csv_file)
    csv_writer = csv.writer(csv_file)

    # Loop through each row in the CSV file
    for row in csv_reader:
        # If the name is "Jane", modify the age to 31
        print(row[0])
        if row[0] == '%u5218%u5B50%u5C27':
            row[1] = '31'

        # Write the modified row back to the CSV file
        csv_writer.writerow(row)
