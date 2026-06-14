# FastAPI Travel Planner

A FastAPI-based travel planning application that allows users to create and manage trips with detailed itineraries.

## Tech Stack

- **Framework**: FastAPI
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: JWT (JSON Web Tokens)
- **Password Hashing**: Argon2
- **Migrations**: Alembic
- **AI Integration**: Anthropic Claude API for dynamic itinerary generation

## Project Structure

```
fastapi-exercise/
├── alembic.ini                 # Alembic configuration for database migrations
├── main.py                     # Application entry point
├── pyproject.toml              # Project dependencies and metadata
├── README.md                   # Documentation
│
├── controllers/                # API route handlers
│   ├── __init__.py
│   ├── auth.py                # Authentication routes (register, login)
│   ├── user_routes.py         # User management routes
│   ├── trip.py                # Trip CRUD routes
│   └── itinerary.py           # Itinerary routes
│
├── models/                     # SQLModel database models
│   ├── __init__.py
│   ├── user.py                # User model
│   ├── trip.py                # Trip model
│   └── itinerary.py           # Itinerary model
│
├── schemas/                    # Pydantic request/response schemas
│   ├── __init__.py
│   ├── user.py                # User request/response schemas
│   ├── trips.py               # Trip request/response schemas
│   └── itinerary.py           # Itinerary request/response schemas
│
├── services/                   # Business logic layer
│   ├── __init__.py
│   ├── auth.py                # Authentication service
│   ├── user_service.py        # User business logic
│   ├── trip_service.py        # Trip business logic
│   └── itinerary_service.py   # Itinerary business logic
│
├── core/                       # Core application configuration
│   ├── __init__.py
│   ├── auth.py                # JWT token creation/validation
│   ├── config.py              # Application configuration
│   ├── db.py                  # Database connection and session management
│   └── deps.py                # Dependency injection utilities
│
└── migrations/                 # Database migration scripts (Alembic)
    ├── env.py
    ├── script.py.mako
    ├── README
    └── versions/
        └── e7681a94b5d6_initial_migration.py
```

## Entities

### User
**Purpose**: Represents a user account in the system.

**Attributes**:
- `id` (int): Primary key
- `email` (str): Unique email address for authentication
- `hashed_password` (str): Securely hashed password

**Relationships**:
- Has many `Trip` entries

---

### Trip
**Purpose**: Represents a travel plan created by a user.

**Attributes**:
- `id` (int): Primary key
- `destination` (str): Travel destination
- `days` (int): Duration of the trip in days
- `budget` (int): Budget allocated for the trip
- `trip_style` (str): Style/type of travel (e.g., adventure, relaxation, cultural)
- `user_id` (int): Foreign key referencing the User who created the trip

**Relationships**:
- Belongs to one `User`
- Has many `Itinerary` entries (planned, actual, alternative routes, etc.)

---

### Itinerary
**Purpose**: Stores detailed day-by-day plans for a trip.

**Attributes**:
- `id` (int): Primary key
- `trip_id` (int): Foreign key referencing the Trip
- `days` (List[dict]): JSON array containing detailed plans for each day

**Relationships**:
- Belongs to one `Trip`
- Multiple itineraries can exist per trip (planned, actual, alternatives, etc.)

---

## API Endpoints

### Authentication

#### Register User
**POST** `/auth/register`

Creates a new user account.

**Request Body**:
```json
{
  "username": "string",
  "password": "string"
}
```

**Response**: `UserResponse` with created user details

---

#### Login
**POST** `/auth/login`

Authenticates a user and returns a JWT token.

**Request Body** (Form Data):
```
email: string
password: string
```

**Response**:
```json
{
  "access_token": "string",
  "token_type": "bearer"
}
```

---

### Users

#### Get All Users
**GET** `/users`

Retrieves a list of all users in the system.

**Response**: `List[UserResponse]`

---

#### Get Current User
**GET** `/users/me`

Retrieves information about the currently authenticated user.

**Authentication**: Required (Bearer Token)

**Response**:
```json
{
  "current_user": "string"
}
```

---

### Trips

#### Get All User Trips
**GET** `/trips`

Retrieves all trips for the currently authenticated user.

**Authentication**: Required (Bearer Token)

**Response**: `List[TripResponse]`

---

#### Create Trip
**POST** `/trips`

Creates a new trip for the authenticated user. Triggers a background task to confirm the booking.

**Authentication**: Required (Bearer Token)

**Request Body**:
```json
{
  "destination": "string",
  "days": "integer",
  "budget": "integer",
  "trip_style": "string"
}
```

**Query Parameters**:
- `user_id` (int): ID of the user creating the trip

**Response**: Created `Trip` object

---

#### Get Trip by ID
**GET** `/trips/{trip_id}`

Retrieves details of a specific trip.

**Authentication**: Required (Bearer Token)

**Path Parameters**:
- `trip_id` (int): ID of the trip

**Response**: `TripResponse`

---

#### Update Trip
**PATCH** `/trips/{trip_id}`

Updates an existing trip's details.

**Authentication**: Required (Bearer Token)

**Path Parameters**:
- `trip_id` (int): ID of the trip to update

**Request Body** (All fields optional):
```json
{
  "destination": "string",
  "days": "integer",
  "budget": "integer",
  "trip_style": "string"
}
```

**Response**: Updated `TripResponse`

---

#### Delete Trip
**DELETE** `/trips/{trip_id}`

Deletes a trip and its associated itineraries.

**Authentication**: Required (Bearer Token)

**Path Parameters**:
- `trip_id` (int): ID of the trip to delete

**Response**: Confirmation message

---

### Itinerary

#### Generate AI Itinerary
**POST** `/itinerary/{trip_id}`

Dynamically generates a detailed day-by-day itinerary using llm (anthropic) based on the trip's destination, duration, budget, and travel style. The generated itinerary is automatically saved to the database.

**Authentication**: Required (Bearer Token)

**Path Parameters**:
- `trip_id` (int): ID of the trip to generate an itinerary for

**Response**: Created `ItineraryResponse` object with AI-generated day-by-day plans

---

#### Get Itinerary by Trip
**GET** `/itinerary/{trip_id}`

Retrieves the itinerary for a specific trip.

**Authentication**: Required (Bearer Token)

**Path Parameters**:
- `trip_id` (int): ID of the trip

**Response**: `Itinerary` object with day-by-day details

---

## Installation & Setup

### Prerequisites
- Python 3.10 or higher
- pip or uv package manager

### Steps

1. **Clone the Repository** (if applicable):
```bash
git clone <repository-url>
cd fastapi-exercise
```

2. **Create Virtual Environment** (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Dependencies**:
```bash
pip install -e .
```

4. **Initialize Database**:
```bash
alembic upgrade head
```

5. **Run Application**:

**Option A - Using uvicorn directly**:
```bash
uvicorn main:app --reload
```

**Option B - Using Python**:
```bash
python -m uvicorn main:app --reload
```

The `--reload` flag enables auto-reload on code changes (development mode).

### Access the Application

Once running, the API will be available at:
- **API Base URL**: `http://localhost:8000`
- **Swagger UI (Interactive Docs)**: `http://localhost:8000/docs`
- **ReDoc (API Documentation)**: `http://localhost:8000/redoc`

---

## Authentication Flow

1. User registers with username and password via `/auth/register`
2. User logs in via `/auth/login` to receive a JWT token
3. Include the token in subsequent requests as: `Authorization: Bearer <token>`
4. The application verifies the token before processing protected endpoints

---

## Database Schema

```
User (1) ──→ (Many) Trips ──→ (Many) Itineraries
```

**Relationships**:
- **Users → Trips** (One-to-Many): Each user can create multiple trips
- **Trips → Itineraries** (One-to-Many): Each trip can have multiple itineraries (planned vs actual and alternatives)
- **Users → Itineraries** (One-to-Many, indirectly): Each user has multiple itineraries through their trips
