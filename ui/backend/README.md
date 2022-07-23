# Rule Validation Tool Backend

This folder contains the backend. Backend is responsible for the following things:
- Converting RulePad string into Java code
- Persisting the confirmed changes related to rule validation to the database
- Logging the users in
- Providing rules to validate for each user

## Technology used
- Python/FastAPI for the backend
- Antlr4 for parsing RulePad grammar
- sqlalchemy for SQL and ORM purposes
- MySQL for the database
