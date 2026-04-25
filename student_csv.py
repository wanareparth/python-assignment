import csv


with open("students.csv", "w", newline='') as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Roll No", "Marks"])


    name = input("Enter name: ")
    roll = input("Enter roll no: ")
    marks = input("Enter marks: ")

    writer.writerow([name, roll, marks])

print("Data written to CSV file successfully!")
