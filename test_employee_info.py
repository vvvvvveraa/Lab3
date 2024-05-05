import employee_info as info

print('I\'m so tired lol')
def get_employees_by_age_range():
    age_small = 30
    age_big = 40
    people = info.get_employees_by_age_range(age_small, age_big)
    # Expected number of employees in the age range 30 to 40
    expected_count = 4  # Update this value according to the expected data
    # Check the number of employees in the specified age range
    assert len(people) == expected_count, f"Expected {expected_count} employees, but got {len(people)}"

def calculate_average_salary():
    # Call the function to calculate the average salary
    average_salary = info.calculate_average_salary(info.employee_data)

    # Calculate the expected average salary based on the data
    total_salary = sum(emp["salary"] for emp in info.employee_data)
    expected_average = total_salary / len(info.employee_data)

    # Check that the calculated average matches the expected average
    assert average_salary == expected_average, f"Expected average salary {expected_average}, but got {average_salary}"


def get_employees_by_dept(): 
    department = 'Sales'
    people = len(get_employees_by_dept(department))
    # Expected number of employees in the 'Sales' department
    expected_count = 2  # Update this value according to the expected data
    # Check the number of employees in the specified department
    assert len(people) == expected_count, f"Expected {expected_count} employees in department {department}, but got {len(people)}"

    get_employees_by_age_range()
    calculate_average_salary()
    get_employees_by_dept()
