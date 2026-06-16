# FastAPI CRUD Posts API

A simple REST API built with **FastAPI** that demonstrates CRUD (Create, Read, Update, Delete) operations on posts using in-memory storage.

## Features

* Create a post
* Get all posts
* Get a single post by ID
* Get the latest post
* Update a post
* Delete a post
* Automatic request validation using Pydantic
* Proper HTTP status codes and error handling

## Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn

## Project Structure

```text
app/
├── __init__.py
└── main.py
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install fastapi uvicorn
```

## Running the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive documentation:

* Swagger UI: http://127.0.0.1:8000/docs
* ReDoc: http://127.0.0.1:8000/redoc

---

## API Endpoints

### Get All Posts

```http
GET /posts
```

Response:

```json
{
  "data": [...]
}
```

### Create a Post

```http
POST /posts
```

Request Body:

```json
{
  "title": "My First Post",
  "content": "Hello FastAPI!",
  "published": true,
  "rating": 5
}
```

### Get Latest Post

```http
GET /posts/latest
```

### Get Post by ID

```http
GET /posts/{id}
```

Example:

```http
GET /posts/1
```

### Update a Post

```http
PUT /posts/{id}
```

Example:

```http
PUT /posts/1
```

Request Body:

```json
{
  "title": "Updated Title",
  "content": "Updated Content",
  "published": true,
  "rating": 4
}
```

### Delete a Post

```http
DELETE /posts/{id}
```

Returns:

```http
204 No Content
```

## Example Post Model

```json
{
  "title": "Sample Post",
  "content": "This is a sample post.",
  "published": true,
  "rating": 5
}
```

## Error Handling

The API returns appropriate HTTP exceptions:

* 404 Not Found – When a post does not exist
* 201 Created – When a new post is successfully created
* 204 No Content – When a post is successfully deleted

## Notes

* Data is stored in memory and will be lost when the server restarts.
* This project is intended for learning FastAPI fundamentals and CRUD operations.

## Author

Built while learning FastAPI and REST API development.
