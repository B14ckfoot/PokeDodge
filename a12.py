import pickle, os

def saveData(dObj):
    with open("a12pickle.txt", "wb") as fPickle:
        pickle.dump(dObj, fPickle)
        fPickle.close()
    print("\nData Saved.\n")

def loadData():
    with open("a12pickle.txt", 'rb') as fPickle:
        dObj = pickle.load(fPickle)
        fPickle.close()
    print("\nData Loaded.\n")
    return dObj
if os.path.exists('a12pickle.txt'):
    employee_database = loadData()
else:
    # Initialize the employee database
    employee_database = {
        'emp1': {'name': 'Bob', 'Mgr': ' 80k'},
        'emp2': {'name': 'Kim', 'Dev': ' 150k'},
        'emp3': {'name': 'Sam', 'Dev': ' 150k'}
    }
    saveData(employee_database)
# Function to add a new employee record
def add_employee(emp_id, name, position, salary):
    if emp_id not in employee_database:
        employee_database[emp_id] = {'name': name, position: salary}
        print(f"Employee '{name}' added successfully.")
    else:
        print(f"Employee with ID '{emp_id}' already exists in the database.")
    saveData(employee_database)
# Function to remove an employee record
def remove_employee(emp_id):
    if emp_id in employee_database:
        del employee_database[emp_id]
        print(f"Employee with ID '{emp_id}' removed successfully.")
    else:
        print(f"Employee with ID '{emp_id}' does not exist in the database.")
# Main function to interact with the employee database
def main():
    while True:
        print("^.^ " * 21)
        print("1. Add Employee".center(58))
        print("2. Remove Employee".center(59))
        print("3. View Employee Database".center(67))
        print("4. Exit".center(49))
        print("^.^ " * 21)
        choice = input("Enter your choice: ")
        print("^.^ " * 21)
        if choice == '1':
            emp_id = input("Enter employee ID: ")
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            salary = input("Enter employee salary: ")
            add_employee(emp_id, name, position, salary)
            saveData(employee_database)
        elif choice == '2':
            emp_id = input("Enter employee ID to remove: ")
            remove_employee(emp_id)
            saveData(employee_database)
        elif choice == '3':
            print("Employee Database:")
            for emp_id, details in employee_database.items():
                print(f"ID: {emp_id}, Name: {details['name']}, Position: {next(iter(details.keys() - {'name'}))}, Salary: {details[next(iter(details.keys() - {'name'}))]}")

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            saveData(employee_database)
            break

        else:
            print("Invalid choice. Please enter a valid option.")
main()

