while True:

    last_name = str(input("Enter student last name or 'ZZZ' to quit: "))
 
    if last_name.upper() == 'ZZZ':
        print("Done processing student records.")
        break

    first_name = str(input("Student first name: "))
    gpa = float(input("Student GPA: "))

    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List!")
    elif gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll!")

print("Goodbye :)")
