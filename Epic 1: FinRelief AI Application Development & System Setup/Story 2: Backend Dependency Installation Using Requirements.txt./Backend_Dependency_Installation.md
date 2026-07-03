# Backend Dependency Installation Using Requirements.txt

## Objective

The FinRelief AI backend requires several Python libraries to support API development, database connectivity, authentication, AI integration, and environment configuration. These dependencies are managed using a `requirements.txt` file to ensure consistent installation across development environments.

## Key Dependencies

The following packages are included in the project:

- fastapi
- uvicorn
- sqlalchemy
- python-jose
- werkzeug
- python-dotenv
- psycopg2-binary
- google-generativeai

## Installation

After activating the virtual environment, install all required dependencies using:

```bash
pip install -r requirements.txt
```

## Purpose of Each Dependency

| Dependency | Purpose |
|------------|---------|
| fastapi | Builds high-performance REST APIs |
| uvicorn | ASGI server for running FastAPI applications |
| sqlalchemy | Object Relational Mapper (ORM) for database operations |
| python-jose | JWT token generation and authentication |
| werkzeug | Password hashing and security utilities |
| python-dotenv | Loads environment variables from `.env` files |
| psycopg2-binary | PostgreSQL database connectivity |
| google-generativeai | Integration with Google Gemini AI services |

## Benefits

- Ensures all developers use the same package versions.
- Simplifies project setup.
- Improves dependency management.
- Supports reproducible development environments.

## Conclusion

Using `requirements.txt` provides a standardized method for installing all backend dependencies required for the FinRelief AI platform, enabling a consistent and reliable development environment.
