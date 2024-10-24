def main():
    # Create and print a list named fruit_list
    fruit_list = ["pear", "banana", "apple", "mango"]
    fruit_list.append('orange')
    fruit_list.remove("Banana") 
    fruit_list.reverse()
    print(f"reversed: {fruit_list}")

main()