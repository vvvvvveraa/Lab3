# Define a dictionary to store employee information
employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

def get_employees_by_age_range(age_lower_limit, age_upper_limit):
    result = []

    # check for age limits and append the item to result
    for item in employee_data:
        if int(item["age"]) > int(age_lower_limit) and int(item["age"]) < int(age_upper_limit):
            result.append(item)

    return result

def calculate_average_salary(employee_salary):
    # Initialize total_salary
    total_salary = 0

    # Iterate through the list of employee data dictionaries
    for employee in employee_data:
        # Add the salary of the current employee to the total
        total_salary += employee["salary"]

    # Calculate the average salary
    if len(employee_data) > 0:
        average_salary = total_salary / len(employee_data)
    else:
        # If employee_data list is empty, return 0 as the average salary
        average_salary = 0

    # Return the average salary
    return average_salary

def get_employees_by_dept(department):
    result = []

    # Iterate through the employee data and add employees from the specified department to the result list
    for employee in employee_data:
        # Check if the employee's department matches the specified department (case-insensitive)
        if employee["department"].lower() == department.lower():
            result.append(employee)

    return result

def display_all_records():
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_data:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))


def display_records(employee_info):
    print(("Name" + "\t" +"Age" +"\t" +"Department" +"\t" +"Salary" ).expandtabs(15))
    for item in employee_info:
        print((item["name"] + "\t" + str(item["age"]) + "\t" + item["department"] + "\t" + str(item["salary"])).expandtabs(15))

def display_main_menu():

    print("\n----- Employee information Tracker -----")

    print("Select option\n")

    print("1 - Display all records")
    print("2 - Display average salary")
    print("3 - Display employee within age range")
    print("4 - Display employee in a department")


    print("Q - Quit")

    option = input("Enter selection =>")

    if option == '1':
        display_all_records()
    elif option == '2':
        average_salary = calculate_average_salary(employee_data)
        print(f"Average salary: ${average_salary:.2f}")
    elif option == '3':
        age_lower = int(input("Enter age lower limit: "))
        age_upper = int(input("Enter age upper limit: "))
        employees_in_age_range = get_employees_by_age_range(age_lower, age_upper)
        display_records(employees_in_age_range)
    elif option == '4':
        department = input("Enter department name: ")
        employees_in_department = get_employees_by_dept(department)
        display_records(employees_in_department)

    elif option == 'Q':
        quit()

def main():

    while (True):
        display_main_menu()


if __name__ == "__main__":
    main()