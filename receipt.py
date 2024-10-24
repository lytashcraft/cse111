import csv
from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary."""
    products_dict = {}
    try:
        with open(filename, mode="rt") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:  
                key = row[key_column_index]
                value = [row[0], row[1], float(row[2])]
                products_dict[key] = value

    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
    except PermissionError as e:
        print("Error: permission denied")
        print(e)
    
    return products_dict

def main():
    store_name = "Inkom Emporium"
    sales_tax_rate = 0.06

    products_dict = read_dictionary("products.csv", 0)

    if not products_dict:
        return

    print(store_name)

    total_items = 0
    subtotal = 0
    requested_items = []

    try:
        with open("request.csv", mode="rt") as file:
            reader = csv.reader(file)
            next(reader)

            for row in reader:
                product_number = row[0]
                quantity = int(row[1])

                prod_info_list = products_dict[product_number]

                product_name = prod_info_list[1]
                product_price = prod_info_list[2]

                print(f"{product_name}: {quantity} @ {product_price:.2f}")

                total_items += quantity
                subtotal += quantity * product_price

                requested_items.append((product_name, quantity, product_price))

    except FileNotFoundError as e:
        print("Error: missing request file")
        print(e)
    except KeyError as e:
        print(f"Error: unknown product ID in the request.csv file")
        print(e)
    
    sales_tax = subtotal * sales_tax_rate
    total = subtotal + sales_tax

    print(f"Number of Items: {total_items}")
    print(f"Subtotal: {subtotal:.2f}")
    print(f"Sales Tax: {sales_tax:.2f}")
    print(f"Total: {total:.2f}")
    
    print(f"Thank you for shopping at the {store_name}.")

    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%A, %B %d, %Y %I:%M %p}")

if __name__ == "__main__":
    main()