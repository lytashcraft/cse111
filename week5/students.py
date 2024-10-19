import csv

def main():
    student_number = 0
    student_name = 1

    students_dict = read_dictionary("week5/students.csv", student_number)

    while True:  # Loop till it is a valid number
        inumber = input("Please enter an I-Number (xx-xxx-xxxx): ")
        inumber = inumber.replace("-", "")

        if not inumber.isdigit():
            print("Invalid character in I-Number. Please try again.")
        else:
            if len(inumber) < 9:
                print("Invalid I-Number: too few digits. Please try again.")
            elif len(inumber) > 9:
                print("Invalid I-Number: too many digits. Please try again.")
            else:
                if inumber not in students_dict:
                    print("No such student. Please try again.")
                else:
                    value = students_dict[inumber]
                    name = value[student_name]
                    print(name)
                    break  # break the loop

def read_dictionary(filename, key_column_index):
    dictionary = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list

    return dictionary

if __name__ == "__main__":
    main()
