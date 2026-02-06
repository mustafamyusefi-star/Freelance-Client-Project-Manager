Freelance Client & Project Manager
Description

This Python application is designed for freelancers to manage their clients, projects, and invoicing. It stores client and project information in CSV files and allows you to:

Add and view clients

Add and view projects

View projects by client

Calculate invoices based on hourly rate and hours worked

The tool is lightweight, easy to use, and perfect for freelance Python developers who want to keep track of their work efficiently.

Features

Client management (ID, name, email, phone)

Project management (project name, description, start/end dates, status, rate, hours worked)

View all clients or projects in a clean table format

Filter projects by client

Automatically calculate invoices

How to Use

Run the Python script:

python freelance_manager.py


Select an option from the menu:

Add Client

View Clients

Add Project

View Projects

View Client Projects

Calculate Invoice

Exit

Follow the prompts to enter client or project information.

File Structure

clients.csv – stores client information

projects.csv – stores project information

Requirements

Python 3.x

No external libraries are required; the program uses Python's built-in csv and datetime modules.

Example
Select an option: 1
Enter Client ID: C001
Enter Client Name: John Doe
Enter Client Email: john@example.com
Enter Client Phone: 1234567890
Client added successfully!

License

This project is open source and free to use.
