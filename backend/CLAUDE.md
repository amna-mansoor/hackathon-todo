# Backend Architectural Guidelines (FastAPI)

This document outlines the architectural principles and conventions for the Python FastAPI backend application.

## Core Principles

1.  **API-First Design**: Define API contracts (endpoints, request/response models) before implementation.
2.  **FastAPI with Pydantic**: Utilize FastAPI's capabilities for rapid API development, validation, and serialization with Pydantic.
3.  **SQLModel for ORM**: Use SQLModel for defining database models and interacting with the Neon Serverless PostgreSQL database, leveraging its Pydantic-compatible features.
4.  **Dependency Injection**: Use FastAPI's dependency injection system for managing database sessions, authentication, and other common dependencies.
5.  **Modular Structure**: Organize code into logical modules (routers, schemas, models, core utilities).
6.  **JWT Authentication & Authorization**: Implement robust JWT-based authentication and authorization using `python-jose` to secure endpoints. Ensure tasks are strictly filtered by `user_id`.
7.  **Type Safety**: Strict type hinting across the entire codebase.
8.  **Error Handling**: Implement custom exception handlers for consistent API error responses (e.g., 400, 401, 403, 404).
9.  **Scalability**: Design for statelessness where possible and optimize database queries.
10. **Observability**: Implement logging for critical events and errors.

## Directory Structure

```
backend/
├── app/                    # FastAPI application root
│   ├── api/                # API routers
│   │   ├── routes/         # Contains endpoint definitions (e.g., auth.py, tasks.py)
│   │   └── deps.py         # FastAPI dependency injection functions
│   ├── core/               # Core application logic, configuration, utilities
│   │   ├── config.py       # Environment variables, application settings
│   │   ├── db.py           # Database engine, session management
│   │   └── security.py     # Password hashing, JWT token handling
│   ├── models/             # SQLModel database models (user.py, task.py)
│   ├── schemas/            # Pydantic models for request/response bodies (user.py, task.py)
│   └── main.py             # FastAPI application entry point
├── tests/                  # Backend tests (pytest)
│   ├── api/                # API endpoint tests
│   └── unit/               # Unit tests for core logic, security, models
├── .env.example            # Example environment variables
├── pyproject.toml          # Project dependencies (Poetry)
└── README.md
```

## Naming Conventions

-   Modules/Files: snake_case (e.g., `user.py`, `auth.py`)
-   Classes: PascalCase (e.g., `User`, `TaskCreate`)
-   Functions/Variables: snake_case
-   Constants: UPPER_SNAKE_CASE

## Data Flow

-   Requests -> Middleware (Auth) -> Router -> Dependency Injection -> Service Logic -> ORM -> Database.
-   Responses <- Database <- ORM <- Service Logic <- Router <- Middleware.

## Error Handling

-   Raise `HTTPException` for standard HTTP errors.
-   Implement custom exception handlers for application-specific errors.
-   Provide clear and consistent error messages in JSON format.
```
