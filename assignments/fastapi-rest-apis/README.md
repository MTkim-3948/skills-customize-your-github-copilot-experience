# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build scalable and modern REST APIs using the FastAPI framework. You'll create endpoints that handle HTTP requests, manage data with request/response models, and implement proper error handling.

## 📝 Tasks

### 🛠️ Task 1: Create Basic GET Endpoints

#### Description
Start by building a simple FastAPI application with multiple GET endpoints. You'll create endpoints that return both static data and data based on path parameters.

#### Requirements
Your completed program should:

- Initialize a FastAPI application
- Create a GET endpoint `/items` that returns a list of all items with their IDs and names
- Create a GET endpoint `/items/{item_id}` that returns a specific item by its ID
- Use appropriate HTTP status codes (200 for success)
- Include basic documentation using docstrings in your endpoint functions

### 🛠️ Task 2: Add POST Endpoints for Creating Resources

#### Description
Expand your API to accept data from clients. You'll create POST endpoints that accept JSON data and store items in your application.

#### Requirements
Your completed program should:

- Create a POST endpoint `/items` that accepts a new item (with name and description)
- Store the new item in an in-memory list with an auto-generated ID
- Return the created item with its ID and a 201 Created status code
- Validate that the required fields are provided
- Create a DELETE endpoint `/items/{item_id}` to remove items from the list

### 🛠️ Task 3: Implement Query Parameters and Advanced Routing

#### Description
Build more sophisticated endpoints that filter and retrieve data based on multiple parameters. This task focuses on query parameters and path parameters working together.

#### Requirements
Your completed program should:

- Create a GET endpoint `/items` that supports optional query parameters (e.g., `skip` and `limit`) for pagination
- Create a GET endpoint `/search` that accepts a `query` parameter to search items by name
- Create a PUT endpoint `/items/{item_id}` to update an existing item
- Ensure all endpoints properly document their parameters and return values
- Test your endpoints using a tool like curl or Postman

### 🛠️ Task 4: Add Error Handling and Data Validation (Stretch Goal)

#### Description
Improve your API's robustness by adding data validation using Pydantic models and comprehensive error handling for edge cases.

#### Requirements
Your completed program should:

- Define Pydantic models for your Item (with fields: id, name, description)
- Implement error handling to return 404 Not Found when an item doesn't exist
- Validate that item names are not empty and descriptions are reasonable length
- Return 400 Bad Request with descriptive error messages for invalid inputs
- Add proper type hints to all function parameters and return values
- Create a root endpoint `/` that returns API documentation information
