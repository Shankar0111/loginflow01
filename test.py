from dataclasses import dataclass
from typing import List


@dataclass
class Employee:
    name: str
    salary: float
    performance: int
    years: int
    department: str


def calculate_bonus(employee):
    if employee.performance >= 90:
        rate = 0.20
    elif employee.performance >= 75:
        rate = 0.10
    elif employee.performance >= 60:
        rate = 0.05
    else:
        rate = 0.0

    return employee.salary * rate


def calculate_raise(employee):
    if employee.years >= 5:
        return employee.salary * 0.05
    elif employee.years >= 3:
        return employee.salary * 0.08
    elif employee.years >= 1:
        return employee.salary * 0.03

    return 0


def calculate_tax(salary):
    if salary > 100000:
        return salary * 0.25
    elif salary > 50000:
        return salary * 0.20
    else:
        return salary * 0.10


def final_salary(employee):
    bonus = calculate_bonus(employee)
    raise_amount = calculate_raise(employee)
    tax = calculate_tax(employee.salary)

    return employee.salary + bonus + raise_amount - tax


def department_average(employees, department):
    employees_in_department = [
        employee
        for employee in employees
        if employee.department == department
    ]

    if not employees_in_department:
        return 0

    total = sum(
        employee.salary
        for employee in employees_in_department
    )

    return total / len(employees_in_department)


def highest_performer(employees):
    employee = employees[0]

    for current in employees:
        if current.performance > employee.performance:
            employee = current

    return employee


def eligible_for_promotion(employee):
    return (
        employee.performance >= 80
        and employee.years >= 2
    )


def total_payroll(employees):
    return sum(
        final_salary(employee)
        for employee in employees
    )


def generate_report(employees):
    print("========== EMPLOYEE REPORT ==========")

    print(
        f"Total employees: {len(employees)}"
    )

    print(
        f"Total payroll: "
        f"${total_payroll(employees):,.2f}"
    )

    print("\nEmployee salaries:")

    for employee in employees:
        bonus = calculate_bonus(employee)
        raise_amount = calculate_raise(employee)
        final = final_salary(employee)

        print(
            f"{employee.name}: "
            f"Salary=${employee.salary:,.2f}, "
            f"Bonus=${bonus:,.2f}, "
            f"Raise=${raise_amount:,.2f}, "
            f"Final=${final:,.2f}"
        )

    print("\nDepartment averages:")

    departments = set(
        employee.department
        for employee in employees
    )

    for department in sorted(departments):
        average = department_average(
            employees,
            department
        )

        print(
            f"{department}: "
            f"${average:,.2f}"
        )

    best = highest_performer(employees)

    print(
        f"\nTop performer: "
        f"{best.name} ({best.performance})"
    )

    print("\nPromotion candidates:")

    for employee in employees:
        if eligible_for_promotion(employee):
            print(employee.name)


def main():

    employees = [
        Employee(
            "Rohit",
            90000,
            95,
            4,
            "Engineering"
        ),
        Employee(
            "Alex",
            70000,
            82,
            6,
            "Marketing"
        ),
        Employee(
            "Sarah",
            120000,
            91,
            8,
            "Engineering"
        ),
        Employee(
            "John",
            55000,
            72,
            2,
            "Sales"
        ),
        Employee(
            "Emma",
            80000,
            88,
            3,
            "Marketing"
        ),
    ]

    generate_report(employees)


if __name__ == "__main__":
    main()
