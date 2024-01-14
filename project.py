import sys
import csv

def main():
    check_correct_args()
    data = []
    try:
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        sys.exit("CSV File does not exist")

    output = []
    for row in data:
        house = select_house(row["characteristics"])
        grade = select_grade(row["birthdate"])
        output.append({"name": row["name"], "house": house, "grade": grade})

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "house", "grade"])
        writer.writerow({"name": "name", "house": "house", "grade": "grade"})
        for row in output:
            writer.writerow({"name": row["name"], "house": row["house"], "grade": row["grade"]})


def check_correct_args():
    if len(sys.argv) < 3:
        sys.exit("Too few arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not CSV file")

def select_house(character):
    if character in ["courage", "patience"]:
        return "Gryffindor"
    elif character in ["patience", "loyal"]:
        return "Hufflepuff"
    elif character in ["creative", "helping"]:
        return "Ravenclaw"
    elif character in ["playful"]:
        return "Slytherin"
    else:
        return "No house!"


def select_grade(year):
    age = 2024 - int(year)
    grade = age - 5
    return "Grade "+ str(grade)


if __name__ == "__main__":
    main()