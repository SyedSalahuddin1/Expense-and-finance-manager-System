**Expense & Finance Management API**

A backend REST API built with Python and FastAPI to manage accounts and expenses using clean architecture and object-oriented design principles.

**Tech Stack**
- Python 3.13
- FastAPI
- Pydantic
- Pytest
- Docker
- Gunicorn + Uvicorn
- Render (Deployment)

**Key Concepts & Architecture**
- Object-Oriented Programming (Encapsulation, Inheritance, Polymorphism)
- SOLID Principles
- Clean Architecture (Domain, Services, Repositories, API layers)
- Dependency Injection
- Request & Response Validation
- RESTful API Design

**Features**
- Create and retrieve accounts (Savings, Credit)
- Apply expenses to accounts
- Automatic input validation using Pydantic
- Proper HTTP error handling
- In-memory repository pattern
- Fully tested API endpoints
- Dockerized for production
- Deployed as a public API with Swagger docs

**Testing**
- API tests using Pytest and FastAPI TestClient
- Unit tests for core business logic

**Deployment**
- Containerized using Docker
- Production server with Gunicorn and Uvicorn workers
- Deployed on Render

**Run Locally**
bash
uvicorn api.app:app --reload

**Run Locally**
docker build -t expense-manager-api .
docker run -p 8000:8000 expense-manager-api

