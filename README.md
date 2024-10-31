# Employee Management API (V1)

## Overview

The Employee Management System API is designed to handle essential tasks for managing employees, attendance, and attendance reporting. This Django-based API includes several key modules and features that support efficient employee and attendance tracking. During development, SQLite is used as the database backend for ease of setup and prototyping.

## Table of Contents
1. [Environment Setup](#environment-setup)
2. [Installation](#installation)
3. [Running Migrations](#running-migrations)
4. [API Documentation](#api-documentation)
    - [Employee Management](#employee-management)
    - [Attendance Management](#attendance-management)
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

## **API Documentation**

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
- **URL**: `http://127.0.0.1:8000/api/attendance/check-in/EMP001/`
- **Description**: Record the time an employee arrives at the office.

#### **POST** - Check-Out
- **URL**: `http://127.0.0.1:8000/api/attendance/check-out/EMP001/`
- **Description**: Record the time an employee leaves the office.

#### **GET** - View Attendance
- **URL**: `http://127.0.0.1:8000/api/attendance/view/EMP001/`
- **Description**: Retrieve all attendance records for a specific employee, with optional filtering by date range.

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
- **Request Body**:
    ```json
    {
      "username": "admin3",
      "password": "Admin123!"
    }
    ```

---

## **Pending Tasks**

1. **Authentication**: Implement full authentication flows, including JWT or session management.
2. **Email Notifications with Queues**: Set up email notifications for employee actions (e.g., registration, attendance checks).
