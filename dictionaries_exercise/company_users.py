company_employees = {}

while True:
    command = input()
    if command == "End":
        break
    company_name, employee_id = command.split(" -> ")
    if company_name not in company_employees:
        company_employees[company_name] = [employee_id]
    elif employee_id not in company_employees[company_name]:
        company_employees[company_name].append(employee_id)

for company in company_employees:
    print(company)
    for employee in company_employees[company]:
        print(f"-- {employee}")