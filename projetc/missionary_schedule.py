from datetime import datetime

appointments = []


def schedule(type, date, time, name, phone, address):
    current_year = datetime.now().year

    appointment_year = int(date.split('/')[2])

    if appointment_year < current_year:
        print("You can only schedule appointments for the current year or later.")
        return

    for a in appointments:
        if a['date'] == date and a['time'] == time:
            print("Time slot is already taken. Please choose another time.")
            return
    
    appointment = {
        'type': type,
        'date': date,
        'time': time,
        'name': name,
        'phone': phone,
        'address': address
    }
    appointments.append(appointment)
    print(f"{type.capitalize()} scheduled for {date} at {time}.")

def cancel_appointment(date, time):
    global appointments
    previous_appointments = [a for a in appointments if a['date'] == date and a['time'] == time]
    
    if not previous_appointments:
        print("There are no appointments to cancel.")
        return

    appointments = [a for a in appointments if not (a['date'] == date and a['time'] == time)]
    print(f"Appointment for {date} at {time} has been canceled.")

def check_available_dates(month, year):
    print(f"Available dates for {month}/{year}:")
    available_days = {}
    for day in range(1, 32):
        date_str = f"{day:02d}/{month:02d}/{year}"
        available_days[date_str] = []
        for appointment in appointments:
            if appointment['date'] == date_str:
                available_days[date_str].append(appointment)

    for date, appointments_of_day in available_days.items():
        if appointments_of_day:
            print(f"{date}: {appointments_of_day}")
        else:
            print(f"{date}: Available")

def generate_weekly_report():
    print("Weekly Report:")
    with open('projetc/weekly_report.txt', 'w') as f:
        for appointment in appointments:
            line = f"{appointment['type'].capitalize()} - Date: {appointment['date']}, Time: {appointment['time']}, Name: {appointment['name']}\n"
            f.write(line)
            print(line.strip())
    print("Weekly report saved in 'weekly_report.txt'.")

def view_appointments():
    if not appointments:
        print("No appointments recorded.")
        return
    print("Recorded Appointments:")
    for appointment in appointments:
        print(f"{appointment['type'].capitalize()} - Date: {appointment['date']}, Time: {appointment['time']}, Name: {appointment['name']}, Phone: {appointment['phone']}, Address: {appointment['address']}")


def main():
    while True:
        print("\nMain Menu:")
        print("1. Schedule/Cancel – Visits and Baptisms")
        print("2. Weekly Report")
        print("3. View Appointments")
        print("4. Exit")
        option = input("Choose an option: ")

        if option == '1':
            while True:
                print("\n1. Schedule")
                print("2. Cancel appointment")
                print("3. Go back")
                option1 = input("Choose an option: ")

                if option1 == '1':
                    while True:
                        month = input("Select the month (1-12) or type 'back' to go back: ")
                        if month.lower() == 'back':
                            break
                        if month.isdigit() and 1 <= int(month) <= 12:
                            month = int(month)
                            year = int(input("Select the year: "))
                            check_available_dates(month, year)

                            while True:
                                print("\n1. View available dates")
                                print("2. Select date for scheduling")
                                print("3. Go back")
                                suboption = input("Choose an option: ")

                                if suboption == '1':
                                    check_available_dates(month, year)

                                elif suboption == '2':
                                    date = input("Select the date for scheduling (DD/MM/YYYY): ")
                                    time = input("Select the time for scheduling (HH:MM): ")
                                    
                                    if any(a['date'] == date and a['time'] == time for a in appointments):
                                        print("This time slot is already taken. Please choose another time.")
                                        continue

                                    type = input("Choose the type of appointment (Visit or Baptism): ").lower()
                                    if type not in ['visit', 'baptism']:
                                        print("Invalid appointment type. Please choose 'Visit' or 'Baptism'.")
                                        continue
                                    name = input("Visitor's name: ")
                                    phone = input("Visitor's phone: ")
                                    address = input("Visitor's address: ")
                                    schedule(type, date, time, name, phone, address)

                                elif suboption == '3':
                                    break
                        else:
                            print("Invalid month. Please try again.")

                elif option1 == '2':
                    date = input("Enter the date of the appointment (DD/MM/YYYY): ")
                    time = input("Enter the time of the appointment (HH:MM): ")
                    cancel_appointment(date, time)

                elif option1 == '3':
                    break

        elif option == '2':
            generate_weekly_report()
            input("Press Enter to continue...")

        elif option == '3':
            view_appointments()
            input("Press Enter to continue...")

        elif option == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

# Start the program
if __name__ == "__main__":
    main()
