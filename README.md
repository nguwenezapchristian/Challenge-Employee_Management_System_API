# Employee Management System API (Development Documentation)

## Overview

The Employee Management System API is designed to handle essential tasks for managing employees, attendance, and attendance reporting. This Django-based API includes several key modules and features that support efficient employee and attendance tracking. During development, SQLite is used as the database backend for ease of setup and prototyping. 

### Key Features
- **Employee Management**: CRUD operations for employee profiles and details.
- **Attendance Management**: Tracking employee attendance with timestamped records.
- **Attendance Reporting**: Generating reports on attendance data.
- **API Documentation**: Detailed documentation of all endpoints.

### Pending Tasks
1. **Authentication**: Secure access and token-based authentication need to be completed.
2. **Email Notifications and Queue**: Implement automated email notifications for specific events.

### Project Structure

```plaintext
.
├── api
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   ├── models.py
│   ├── tests.py
│   ├── urls_ft
│   │   ├── attendance.py
│   │   ├── authentication.py
│   │   └── employees.py
│   ├── urls.py
│   └── views
│       ├── attendance
│       ├── authentication
│       └── employees
├── attendance
│   ├── models.py
│   ├── views.py
├── authentication
│   ├── serializers.py
│   ├── views.py
├── base
│   ├── permissions.py
│   ├── utils
│   │   ├── decorators.py
│   │   ├── exceptions.py
│   │   └── response_utils.py
├── core
│   ├── settings.py
│   ├── urls.py
├── employees
│   ├── serializers.py
│   ├── services
│   │   └── employee_service.py
│   ├── views.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

# API Documentation

## Base URL
```plaintext
http://127.0.0.1:8000/api/
```

---

### **Employee Management**

#### **GET** - List All Employees
- **URL**: `http://127.0.0.1:8000/api/employees/`
- **Description**: Retrieve a list of all employees.

---

#### **POST** - Create an Employee
- **URL**: `http://127.0.0.1:8000/api/employees/create/`
- **Description**: Create a new employee.
- **Request Body**:
    ```json
    {
      "name": "John Doe",
      "email": "johndoe@example.com",
      "phone_number": "+12345678901",
      "password": "securePassword123!",
      "confirm_password": "securePassword123!"
    }
    ```

---

#### **GET** - Retrieve an Employee
- **URL**: `http://127.0.0.1:8000/api/employees/EMP001`
- **Description**: Retrieve details of a specific employee by their ID.

---

#### **PUT** - Update Employee Data
- **URL**: `http://127.0.0.1:8000/api/employees/EMP001/update/`
- **Description**: Update the data of a specific employee.
- **Request Body**:
    ```json
    {
      "name": "Johnathan Doe"
    }
    ```

---

#### **DELETE** - Delete an Employee
- **URL**: `http://127.0.0.1:8000/api/employees/EMP001/delete/`
- **Description**: Delete a specific employee by their ID.

---

### **Attendance Management**

#### **POST** - Check-In
- **URL**: `http://127.0.0.1:8000/api/attendance/check-in/`
- **Description**: Record the time an employee arrives at the office.
- **Request Body**:
    ```json
    {
      "employee_id": "EMP001"
    }
    ```

---

#### **POST** - Check-Out
- **URL**: `http://127.0.0.1:8000/api/attendance/check-out/`
- **Description**: Record the time an employee leaves the office.
- **Request Body**:
    ```json
    {
      "employee_id": "EMP001"
    }
    ```

---

#### **GET** - View Attendance
- **URL**: `http://127.0.0.1:8000/api/attendance/view/`
- **Description**: Retrieve all attendance records for a specific employee, with optional filtering by date range.
- **Request Body**:
    ```json
    {
      "employee_id": "EMP001"
    }
    ```

---

#### **GET** - Attendance PDF Report
- **URL**: `http://127.0.0.1:8000/api/attendance/report/pdf/`
- **Description**: Generate and download the PDF version of the daily attendance report.

---

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

---

#### **POST** - Login
- **URL**: `http://127.0.0.1:8000/api/auth/login/`
- **Request Body**:
    ```json
    {
      "username": "admin3",
      "password": "Admin123!"
    }
    ```

---

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

### Pending Endpoint Details

#### 4. **Authentication**

- **Endpoint**: `POST /auth/login/`
- **Description**: Authenticates a user and returns a token.
- **Status**: **Pending** - Authentication logic and JWT token generation need to be finalized.

#### 5. **Email Notifications and Queue**

- **Functionality**: Implement automated emails for specific events, such as new employee registration or missed attendance alerts.
- **Status**: **Pending** - Email server configuration and notification trigger points need to be set up.
---

### Development Database

For this development phase, SQLite is used as the database backend (`db.sqlite3`). It provides simplicity and requires minimal setup, making it ideal for local testing and development.

### Testing

All endpoints related to Employee Management, Attendance Management, and Attendance Reporting have been tested using Postman and confirmed to be working as expected.