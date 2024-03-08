import csv
import datetime

now = datetime.datetime.now()

def get_csv_header(csv_file):
    with open(csv_file, 'r', newline='') as file:
        reader = csv.reader(file)
        header = next(reader)
    return header

habits = list(get_csv_header(str(now.month) + "_" + str(now.year) + ".csv"))


if(now.day == 1):
    while True:
        temp = input("enter new habit for this month: ")
        if temp == "":
            break
        habit.append(temp)

    with open(str(now.month) + "_" + str(now.year) + ".csv", 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(habits)

completed = []

for habit in habits:
    temp = input("did you complete " + habit + "? ")
    completed.append(temp)


with open(str(now.month) + "_" + str(now.year) + ".csv", 'a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(completed)

print("Habits have been recorded!")

