# Healthcare Management System

A Django REST Framework based backend system for healthcare management with PostgreSQL database.

## Features

- JWT Authentication
- Patient Management
- Doctor Management
- Patient-Doctor Mapping
- Secure API Endpoints
- PostgreSQL Database

## Tech Stack

- Django
- Django REST Framework
- PostgreSQL
- JWT Authentication

## API Endpoints

### Authentication
- `POST /api/auth/register/` - Register new user
- `POST /api/auth/login/` - Login user

### Patients
- `POST /api/patients/` - Add patient
- `GET /api/patients/` - List patients
- `GET /api/patients/<id>/` - Get patient details
- `PUT /api/patients/<id>/` - Update patient
- `DELETE /api/patients/<id>/` - Delete patient

### Doctors
- `POST /api/doctors/` - Add doctor
- `GET /api/doctors/` - List doctors
- `GET /api/doctors/<id>/` - Get doctor details
- `PUT /api/doctors/<id>/` - Update doctor
- `DELETE /api/doctors/<id>/` - Delete doctor

### Mappings
- `POST /api/mappings/` - Assign doctor to patient
- `GET /api/mappings/` - List all mappings
- `GET /api/mappings/<patient_id>/` - Get patient's doctors
- `DELETE /api/mappings/<id>/` - Remove mapping

## Setup Instructions

1. Clone the repository
```bash
git clone https://github.com/AbhinavRathor/Healthcare_Management.git
cd Healthcare_Management
```

2. Create virtual environment
```bash
python -m venv venv
```

3. Activate virtual environment
```bash
# Windows
.\venv\Scripts\activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Configure environment variables in `.env`:
```env
DB_NAME=healthcare_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_secret_key
DEBUG=True
```

6. Apply migrations
```bash
python manage.py migrate
```

7. Create superuser
```bash
python manage.py createsuperuser
```

8. Run server
```bash
python manage.py runserver
```