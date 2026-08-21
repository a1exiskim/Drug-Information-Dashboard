# Drug Information Dashboard

## Project Overview

This is a Python application that retrieves drug information from the OpenFDA API, stores cleaned data in PostgreSQL, and exposes the data through a FastAPI backend.

The project is being built to learn:

- REST APIs
- ETL/data pipelines
- Data transformation
- PostgreSQL/database integration
- FastAPI
- Pydantic
- Automated testing
- Frontend development
- Full-stack application architecture

## Existing Backend Architecture

The backend follows this general flow:

User/Frontend
→ FastAPI
→ Pipeline
→ PostgreSQL lookup
→ OpenFDA API fallback
→ Transform
→ PostgreSQL load
→ FastAPI response
→ Frontend

### `api.py`

Responsible for communicating with OpenFDA.

- Uses `requests`
- Accepts a drug name
- Retrieves raw OpenFDA JSON
- Uses a request timeout
- Handles HTTP status codes
- Converts an OpenFDA 404 into `None`
- Re-raises unexpected HTTP errors

Do not call OpenFDA directly from the frontend.

### `transform.py`

Responsible for transforming raw OpenFDA data into the application's cleaned drug structure.

The cleaned structure contains:

- `drug_name`
- `generic_name`
- `manufacturer`
- `purpose`
- `warnings`
- `dosage_and_administration`
- `active_ingredient`

OpenFDA frequently represents fields as lists. The transformation layer converts these into the format expected by the application.

### `db.py`

Responsible for PostgreSQL interaction.

- Establishes database connections
- Retrieves drugs
- Inserts cleaned drugs
- Uses psycopg
- Uses cursor context managers
- Uses transaction context managers

Database logic should remain in this module rather than being placed in frontend code or FastAPI route handlers.

### `pipeline.py`

Contains the application's core drug retrieval workflow.

`find_or_fetch_drug()` follows this logic:

1. Search PostgreSQL for the requested drug.
2. If found, return the stored drug.
3. If not found, request the drug from OpenFDA.
4. If OpenFDA returns no drug, return `None`.
5. Transform the raw API response.
6. Store the cleaned drug in PostgreSQL.
7. Return the cleaned drug.

The pipeline should not contain HTTP-specific response handling.

### `main.py`

Contains the FastAPI application and API routes.

Current endpoint:

`GET /drugs/{drug_name}`

Responsibilities:

- Receive HTTP requests
- Manage request-level database connection lifetime
- Call the pipeline
- Convert a missing drug into HTTP 404
- Return the API response

Do not place database queries, OpenFDA requests, or transformation logic directly inside route handlers.

### Pydantic Response Model

The API uses a Pydantic response model to define the API contract.

The response fields are:

- `drug_name: str`
- `generic_name: str`
- `manufacturer: str`
- `purpose: str`
- `warnings: str`
- `dosage_and_administration: str`
- `active_ingredient: str`

The frontend should treat this response structure as the backend API contract.

## Testing

The project uses pytest.

Tests currently cover:

- Transformation logic
- Missing/empty API fields
- PostgreSQL loading
- PostgreSQL retrieval
- Database misses
- API mocking
- Pipeline behaviour
- FastAPI endpoint behaviour
- Response validation

Run the test suite after making backend changes:

`pytest`

Do not break existing tests without explaining why.

## Frontend

The frontend will be developed separately from the backend.

Preferred technology:

- React
- Vite

The frontend communicates exclusively with the FastAPI backend.

The frontend must NOT:

- Access PostgreSQL directly
- Call OpenFDA directly
- Contain database logic
- Contain OpenFDA API logic
- Reimplement the backend pipeline

Frontend flow:

React
→ FastAPI
→ JSON response
→ React UI

## Frontend Design

The application should have a modern medical/data-product aesthetic. Keep it clean and minimal.

Design principles:

- Clean
- Modern
- Professional
- Strong information hierarchy
- Generous whitespace
- Subtle borders
- Rounded cards
- Minimal visual clutter
- Easy-to-read long-form drug information

Avoid making the application look like a generic admin dashboard or hospital website.

### Page hierarchy

The drug information page should prioritize:

1. Drug name
2. Generic name and manufacturer
3. Purpose and active ingredient
4. Dosage and administration
5. Warnings

Warnings should be visually distinct but should not make the entire interface overly red or alarming.

## Frontend States

The frontend must explicitly handle:

### Empty

No search has been performed.

Display a prompt encouraging the user to search for a drug.

### Loading

A request is currently being made.

The UI should communicate that the application is searching and prevent accidental duplicate submissions.

### Success

The backend returns HTTP 200.

Display the drug information.

### Not Found

The backend returns HTTP 404.

Display a clear "Drug not found" message and allow the user to search again.

### Server/API Error

The backend returns an unexpected error.

Display a generic error message and allow the user to retry.

### Search Interaction

The search bar should:

- Allow drug name input
- Support clicking a search button
- Support pressing Enter
- Remain available after a search
- Prevent duplicate requests while loading

## Development Guidelines

Before making significant architectural changes:

1. Explain the proposed change.
2. Explain why it is useful.
3. Preserve the existing backend architecture unless explicitly asked to change it.
4. Prefer small, understandable changes over unnecessary abstractions. Remember this is a beginner data engineering project.
5. Keep frontend and backend responsibilities separated.
6. Do not add dependencies unless they provide a clear benefit.
7. Run existing tests after backend changes.

When implementing frontend features, prioritize maintainability and clear component boundaries over excessive abstraction.

Do not rewrite working code simply for stylistic reasons.