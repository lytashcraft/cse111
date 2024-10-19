import csv

def main():
    text_list = read_list("week5/reading/provinces.txt")

    text_list.pop()

    for i in range(len(text_list)):
        if text_list[i] == "AB":
            text_list[i] = "Alberta"

    print(text_list)

def read_list(filename):
    text_list = []

    with open(filename, "rt") as text_file:
    

        reader = csv.reader(text_file)
        next(reader)

        for line in text_file:
            clean_line = line.strip()
            text_list.append(clean_line)  
    return text_list

if __name__ == "__main__":
    main()
