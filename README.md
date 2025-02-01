# Operations Schedule Manager
Operations Schedule Manager is a Django web application designed for scheduling surgeries, managing patient and doctor information, operating rooms, and surgical plans.

## Key Features
Patient Management: Add, edit, delete, and view patient information.

Doctor Management: Maintain a list of doctors and their departments.

Surgery Scheduling: Manage surgery schedules including times, names, and rooms.

Operating Room Management: Track available operating rooms.

Authentication and Authorization: User access system extended to store doctor information.

Administrative Panel: Utilize Django's admin system for efficient model and data management.

## Technologies Used
Programming Language: Python 3.x

Web Framework: Django 3.x or higher

Database: SQLite (default), with optional support for PostgreSQL or MySQL

Frontend: HTML, CSS (optional Bootstrap)

Authentication: Extended user model based on AbstractUser

## Installation and Setup
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
python manage.py loaddata initial_data.json
```
# Demo
https://operations-schedule-manager.onrender.com
login: user

password: user12345

