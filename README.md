# Employee Management API (V1)

## Overview

The Employee Management System API is designed to handle essential tasks for managing employees, attendance, and attendance reporting. This Django-based API includes several key modules and features that support efficient employee and attendance tracking. During development, SQLite is used as the database backend for ease of setup and prototyping, If you want to use Postgres, make sure to make PRODUCTION = True in .env file.

**API IS NOW LIVE!!!!! CHECK IT OUT [HERE](https://nguweneza.tech)**

## Table of Contents
1. [Environment Setup](#environment-setup)
2. [Installation](#installation)
3. [Running Migrations](#running-migrations)
4. [Running Redis and Celery](#running-redis-and-celery)
5. [API Documentation](#api-documentation)
    - [Swagger API Documentation](#swagger-documentation)
    - [Employee Management](#employee-management)
    - [Attendance Management](#attendance-management)
    - [Attendance Report](#attendance-report)
    - [Authentication](#authentication)

---

## **Environment Setup**

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Create a .env File**:
- In the project’s root directory, create a new file named .env.

- Add the following variables to configure your environment:
```bash
# Database Configuration
POSTGRES_DATABASE=your_database_name
POSTGRES_HOST=your_database_host
POSTGRES_PASSWORD=your_database_password
POSTGRES_USER=your_database_user

# Production Environment
PRODUCTION=True

# Security Key
SECRET_KEY=your_django_secret_key

# Email Configuration
POSTMARK_API_TOKEN=your_postmark_api_token
DEFAULT_FROM_EMAIL=your_default_sender_email
```

---

## **Installation**

1. **Install Project Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Running Migrations**

1. **Apply Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

2. **Create a Superuser (optional)**:
   - For access to the admin dashboard and testing purposes.
   ```bash
   python manage.py createsuperuser
   ```

3. **Run the Server**:
   ```bash
   python manage.py runserver
   ```

---

## **Running Redis and Celery**

### Step 1: Start Redis Server
To enable message queues for email notifications, Redis must be running as the broker for Celery. Start the Redis server with:
   ```bash
   redis-server
   ```

### Step 2: Start Celery Worker
With Redis running, start the Celery worker for the application:
   ```bash
   celery -A core worker --loglevel=info
   ```
This command initiates the Celery worker, which will process email notification tasks and other background jobs.

---

## **API Documentation**

### **Swagger Documentation**

Click [here](https://app.swaggerhub.com/apis-docs/NGUWENEZACC982/employee_management_system_api/1#/default/post_api_employees_create_) to go to the documentation.

Or Use the following documentation with a live API via https://nguweneza.tech/

### **Employee Management**

#### **GET** - List All Employees
- **URL**: `http://127.0.0.1:8000/api/employees/`
- **Description**: Retrieve a list of all employees.

#### **POST** - Create an Employee
- **URL**: `http://127.0.0.1:8000/api/employees/create/`
- **Description**: Create a new employee.
- **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "johndoe@example.com",
      "phone_number": "+12345678901",
      "password": "securePassword123!"
    }
    ```

#### **GET** - Retrieve an Employee
- **URL**: `http://127.0.0.1:8000/api/employees/EMP001/`
- **Description**: Retrieve details of a specific employee by their ID.

#### **PUT** - Update Employee Data
- **URL**: `http://127.0.0.1:8000/api/employees/EMP001/update/`
- **Description**: Update the data of a specific employee.
- **Request Body**:
    ```json
    {
      "name": "Johnathan Doe"
    }
    ```

#### **DELETE** - Delete an Employee
- **URL**: `http://127.0.0.1:8000/api/employees/EMP001/delete/`
- **Description**: Delete a specific employee by their ID.

---

### **Attendance Management**

#### **POST** - Check-In
- **URL**: `http://127.0.0.1:8000/api/attendance/check-in/EMP004/`
- **Description**: Record the time an employee arrives at the office and sends the email notifying them.

#### **POST** - Check-Out
- **URL**: `http://127.0.0.1:8000/api/attendance/check-out/EMP004/`
- **Description**: Record the time an employee leaves the office and sends the email notifying them.

#### **GET** - View Attendance
- **URL**: `http://127.0.0.1:8000/api/attendance/view/EMP001/`
- **Description**: Retrieve all attendance records for a specific employee, with optional filtering by date range.

---

### **Attendance Report**

#### **GET** - Attendance PDF Report
- **URL**: `http://127.0.0.1:8000/api/attendance/report/pdf/`
- **Description**: Generate and download the PDF version of the daily attendance report.

#### **GET** - Attendance Excel Report
- **URL**: `http://127.0.0.1:8000/api/attendance/report/excel/`
- **Description**: Generate and download the Excel version of the daily attendance report.

---

### **Authentication**

#### **POST** - Register
- **URL**: `http://127.0.0.1:8000/api/auth/register/`
- **Request Body**:
    ```json
    {
      "username": "admin3",
      "email": "admin3@example.com",
      "password": "Admin123!",
      "role": "admin"
    }
    ```

#### **POST** - Login
- **URL**: `http://127.0.0.1:8000/api/auth/login/`
- **Request Body**:
    ```json
    {
      "username": "admin3",
      "password": "Admin123!"
    }
    ```

#### **POST** - Logout
- **URL**: `http://127.0.0.1:8000/api/auth/logout/`
- **Authorization Header**: Provide the access token got from Login in Authorization using Bearer Token

#### **POST** - Forgot Password
- **URL**: `http://127.0.0.1:8000/api/auth/forgot-password/`
- **Request Body**:
    ```json
    {
      "email": "pierre@nguweneza.tech"
    }
    ```
- **Description**: After sending the request, the email is sent with the link to reset the password.

#### **POST** - Reset Password
- **URL**: `http://127.0.0.1:8000/api/auth/reset-password/c3da51f2-0d74-4033-acf0-6f8fb746188b/`
- **Request Body**:
    ```json
    {
      "new_password": "Admin123!!"
    }
    ```
- **Description**: Receive an email containing the link to reset the password.

---