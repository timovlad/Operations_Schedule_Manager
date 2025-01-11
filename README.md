Operations Schedule Manager
Project Description
Operations Schedule Manager is a Django-based web application designed to manage the scheduling of surgeries in a medical facility. The project provides an intuitive interface for administering information about patients, doctors, operating rooms, and surgical planning.

Key Features
Patient Management: Add, edit, delete, and view patient information, including department, attending physician, room number, and scheduled surgery.

Doctor Management: Maintain a list of doctors and their departmental affiliations.

Surgery Scheduling: Create and manage surgery schedules with specified times, surgery names, and assigned operating rooms.

Operating Room Management: Keep track of available operating rooms.

Authentication and Authorization: User access system utilizing Django's standard user model, extended to store doctor information.

Administrative Panel: Leverage Django's built-in admin system to manage models and data efficiently.

Technologies Used
Programming Language: Python 3.x

Web Framework: Django 3.x or higher

Database: SQLite (default), with the option to use other databases like PostgreSQL or MySQL

Frontend: HTML, CSS (optionally using Bootstrap or other frameworks for styling)

Authentication: Extended user model based on AbstractUser

Installation and Setup
Prerequisites
Python 3.x

Pip (Python package manager)

Virtual Environment (recommended)

Step-by-Step Guide
Clone the Repository

bash
git clone https://github.com/timovlad/Operations_Schedule_Manager.git
Navigate to the Project Directory

bash
cd Operations_Schedule_Manager
Create and Activate a Virtual Environment

Create a virtual environment:

bash
python -m venv venv
Activate the virtual environment:

On Windows:

bash
venv\Scripts\activate
On Unix/Linux/MacOS:

bash
source venv/bin/activate
Install Dependencies

bash
pip install -r requirements.txt
If requirements.txt is not available, install Django manually:

bash
pip install django
Apply Database Migrations

bash
python manage.py migrate
Create a Superuser

For accessing the administrative panel, create a superuser:

bash
python manage.py createsuperuser
Follow the prompts in the console.

Run the Development Server

bash
python manage.py runserver
Access the Application

Open your browser and navigate to http://127.0.0.1:8000/

Usage
Authentication
Login: Use the superuser credentials or create a new user via the administrative panel.

Admin Panel: Accessible at http://127.0.0.1:8000/admin/

Main Sections
Home Page: Contains a welcome message or general information.

Patient List: View all patients, their attending doctors, departments, and surgery information.

Add/Edit Patients: Forms for entering or modifying patient data.

Surgery List: View scheduled surgeries with details.

Add/Edit Surgeries: Forms for scheduling a new surgery or editing an existing one.

Navigation
Use the navigation menu to move between different sections of the application.

Actions are available only to authenticated users.

Project Structure
models.py: Contains data models:

Department — hospital departments.

Doctor — extended user model for doctors, linked to departments.

OperatingRoom — operating rooms.

Surgery — information about scheduled surgeries.

Patient — patient information linked to doctors and surgeries.

views.py: Defines views to handle requests and return appropriate responses using templates.

forms.py: PatientForm and SurgeryForm for validating and processing patient and surgery data.

templates/: HTML templates for rendering the user interface.

urls.py: URL routing to map URLs to their corresponding views.

static/: Static files (CSS, JavaScript, images) for the frontend.

Requirements
Python: 3.x

Django: 3.x or higher

Additional Packages: Listed in requirements.txt (if available)

Testing
To run tests (if implemented), use the command:

bash
python manage.py test
Add details about tests if necessary.

License
This project is licensed under the MIT License. For more details, see the LICENSE file.

Contributing
We welcome contributions from the community! If you'd like to contribute:

Fork the repository.

Create a new branch for your feature or fix.

Submit a pull request with a description of your changes.