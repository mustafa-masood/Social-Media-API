# FastAPI Python API Development

This repository contains the source code for a comprehensive Python API development project using **FastAPI**. The project is part of a course that covers the fundamentals of API design, including **routes**, **serialization/deserialization**, **schema validation**, **models**, and much more. It also covers setting up a **PostgreSQL database**, integrating **JWT authentication**, building a **CI/CD pipeline** using **GitHub Actions**, and deploying to **Heroku** and **Docker**.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Technologies Used](#technologies-used)
5. [Features](#features)
6. [Course Breakdown](#course-breakdown)
7. [CI/CD Pipeline](#cicd-pipeline)
8. [Contributing](#contributing)
9. [License](#license)

---

## Project Overview

This project provides a step-by-step guide to building a Python API with **FastAPI**. The course covers various concepts like routing, handling HTTP requests, using **Pydantic** for schema validation, implementing CRUD operations, and interacting with a **PostgreSQL** database.

Additionally, the course walks you through integrating **JWT authentication** for securing routes, setting up a **CI/CD pipeline** using **GitHub Actions**, and deploying the application to **Heroku** and **Docker**.

By the end of this course, you will have built a full-fledged API capable of handling user registration, login with JWT tokens, interacting with a PostgreSQL database, and testing the application with **pytest**.

---

## Installation

To get started with this project locally, follow these steps:

### Requirements

- Python 3.8+
- PostgreSQL
- Docker (optional for deployment)
- Git
- Virtual environment tool (e.g., `venv` or `virtualenv`)

### Step 1: Clone the repository

```bash
git clone https://github.com/Sanjeev-Thiyagaraj/fastapi-python-api.git
cd fastapi-python-api
```

### Step 2: Create a virtual environment

#### On Mac/Linux:

```bash
python3 -m venv env
source env/bin/activate
```

#### On Windows:

```bash
python -m venv env
.\env\Scripts\activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set up the database

Follow the steps in the project to set up **PostgreSQL** and create your database schemas. You will also need to install **PgAdmin** for easier management of your database.

```bash
# Example to setup Postgres:
sudo apt-get install postgresql postgresql-contrib
```

---

## Usage

To run the FastAPI application locally:

1. Set up your database and environment variables (e.g., database URL, secret keys for JWT).
2. Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

You can now access the API at `http://127.0.0.1:8000`.

For testing the endpoints, use **Postman** or any API testing tool. The project includes predefined Postman collections for testing common operations.

---

## Technologies Used

- **FastAPI**: Fast web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **PostgreSQL**: Open-source relational database for storing data.
- **SQLAlchemy**: ORM for interacting with the database.
- **Pydantic**: Data validation and parsing library for Python.
- **JWT**: JSON Web Tokens for securing routes and user authentication.
- **pytest**: Testing framework for Python.
- **GitHub Actions**: CI/CD pipeline for automatic testing and deployment.
- **Docker**: For containerization of the application.
- **Heroku**: Cloud platform for deploying the app.

---

## Features

- **CRUD Operations**: Create, Read, Update, and Delete operations with SQLAlchemy and FastAPI.
- **Authentication**: JWT-based user authentication and login flow.
- **PostgreSQL Integration**: Storing and retrieving data from a PostgreSQL database.
- **Schema Validation**: Validating incoming and outgoing data using Pydantic models.
- **Database Migrations**: Use of Alembic to handle database schema migrations.
- **Testing**: Automated tests using pytest, with fixtures for database setup and teardown.
- **CI/CD Pipeline**: Continuous Integration and Deployment using GitHub Actions.
- **Deployment**: Deployment on **Heroku**, **Docker**, and **Ubuntu VM**.
- **Security**: Securing routes and user data with JWT authentication and HTTPS.

---

## Course Breakdown

Here’s an overview of the course content:

1. **API Basics**: Learn about path operations, HTTP requests, schema validation with Pydantic, and CRUD operations.
2. **Database**: Connect to PostgreSQL, write SQL queries, and integrate with SQLAlchemy for ORM.
3. **User Management**: Implement user registration, password hashing, and token generation using JWT.
4. **Security**: Secure routes and user data, protect routes, and handle expired tokens.
5. **Deployment**: Deploy to Heroku, set up PostgreSQL on Heroku, and configure GitHub actions for CI/CD.
6. **Testing**: Write automated tests with pytest and use fixtures to interact with the database.
7. **Docker**: Dockerize the application, including PostgreSQL and FastAPI containers.

---

## CI/CD Pipeline

This project uses **GitHub Actions** to implement Continuous Integration and Continuous Deployment (CI/CD). Upon pushing code to the repository, the CI/CD pipeline automatically runs tests, checks code quality, and deploys the app to Heroku or Docker.

---

## Contributing

Contributions to this project are welcome! If you find any issues or want to suggest improvements, feel free to fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Sanjeev Thiyagarajan**: For providing this incredible course on Python API development using FastAPI.
- **FastAPI Documentation**: https://fastapi.tiangolo.com/
- **PostgreSQL Documentation**: https://www.postgresql.org/docs/
```
