import csv
import os
from datetime import datetime

CLIENTS_FILE = "clients.csv"
PROJECTS_FILE = "projects.csv"

if not os.path.exists(CLIENTS_FILE):
    with open(CLIENTS_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ClientID", "Name", "Email", "Phone"])

if not os.path.exists(PROJECTS_FILE):
    with open(PROJECTS_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["ProjectID", "ClientID", "ProjectName", "Description", "StartDate", "EndDate", "Status", "Rate", "HoursWorked"])

def add_client():
    client_id = input("Enter Client ID: ")
    name = input("Enter Client Name: ")
    email = input("Enter Client Email: ")
    phone = input("Enter Client Phone: ")

    with open(CLIENTS_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([client_id, name, email, phone])
    print("Client added successfully!\n")

def view_clients():
    with open(CLIENTS_FILE, mode='r') as file:
        reader = csv.reader(file)
        clients = list(reader)[1:]
        if not clients:
            print("No clients found.\n")
            return
        print(f"{'ClientID':<10}{'Name':<20}{'Email':<25}{'Phone'}")
        print("-"*70)
        for client in clients:
            print(f"{client[0]:<10}{client[1]:<20}{client[2]:<25}{client[3]}")
        print("-"*70 + "\n")

def add_project():
    project_id = input("Enter Project ID: ")
    client_id = input("Enter Client ID for this project: ")
    project_name = input("Enter Project Name: ")
    description = input("Enter Project Description: ")
    start_date = input("Enter Start Date (YYYY-MM-DD) or leave empty for today: ")
    if not start_date:
        start_date = datetime.today().strftime("%Y-%m-%d")
    end_date = input("Enter End Date (YYYY-MM-DD) or leave empty if ongoing: ")
    status = input("Enter Status (Ongoing/Completed): ")
    try:
        rate = float(input("Enter hourly rate ($): "))
    except ValueError:
        print("Invalid rate. Setting to 0.")
        rate = 0
    try:
        hours = float(input("Enter hours worked: "))
    except ValueError:
        print("Invalid hours. Setting to 0.")
        hours = 0

    with open(PROJECTS_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([project_id, client_id, project_name, description, start_date, end_date, status, rate, hours])
    print("Project added successfully!\n")

def view_projects():
    with open(PROJECTS_FILE, mode='r') as file:
        reader = csv.reader(file)
        projects = list(reader)[1:]
        if not projects:
            print("No projects found.\n")
            return
        print(f"{'ProjectID':<10}{'ClientID':<10}{'ProjectName':<20}{'Status':<10}{'Rate':<8}{'Hours'}")
        print("-"*70)
        for proj in projects:
            print(f"{proj[0]:<10}{proj[1]:<10}{proj[2]:<20}{proj[6]:<10}{proj[7]:<8}{proj[8]}")
        print("-"*70 + "\n")

def view_client_projects():
    client_id = input("Enter Client ID to view projects: ")
    with open(PROJECTS_FILE, mode='r') as file:
        reader = csv.reader(file)
        projects = [p for p in list(reader)[1:] if p[1] == client_id]
        if not projects:
            print("No projects for this client.\n")
            return
        print(f"{'ProjectID':<10}{'ProjectName':<20}{'Status':<10}{'Rate':<8}{'Hours'}")
        print("-"*60)
        for proj in projects:
            print(f"{proj[0]:<10}{proj[2]:<20}{proj[6]:<10}{proj[7]:<8}{proj[8]}")
        print("-"*60 + "\n")

def calculate_invoice():
    project_id = input("Enter Project ID to calculate invoice: ")
    with open(PROJECTS_FILE, mode='r') as file:
        reader = csv.reader(file)
        projects = [p for p in list(reader)[1:] if p[0] == project_id]
        if not projects:
            print("Project not found.\n")
            return
        proj = projects[0]
        total = float(proj[7]) * float(proj[8])
        print(f"Invoice for Project {proj[2]}: ${total:.2f}\n")

def main_menu():
    while True:
        print("Freelance Client & Project Manager")
        print("1. Add Client")
        print("2. View Clients")
        print("3. Add Project")
        print("4. View Projects")
        print("5. View Client Projects")
        print("6. Calculate Invoice")
        print("7. Exit")
        choice = input("Select an option: ")
        if choice == '1':
            add_client()
        elif choice == '2':
            view_clients()
        elif choice == '3':
            add_project()
        elif choice == '4':
            view_projects()
        elif choice == '5':
            view_client_projects()
        elif choice == '6':
            calculate_invoice()
        elif choice == '7':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main_menu()
