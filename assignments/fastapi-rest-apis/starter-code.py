"""
Building REST APIs with FastAPI - Starter Code

This is a starter template for building a REST API using FastAPI.
Follow the tasks in the assignment to implement the required endpoints.
"""

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from typing import List, Optional

# Initialize the FastAPI application
app = FastAPI(
    title="Item Management API",
    description="A simple REST API for managing items",
    version="1.0.0"
)

# ============================================================================
# Data Models (Pydantic)
# ============================================================================
# TODO: Define your Pydantic models here for data validation
# Example structure:
# class ItemBase(BaseModel):
#     name: str
#     description: str
#
# class Item(ItemBase):
#     id: int


# ============================================================================
# In-Memory Data Storage
# ============================================================================
# TODO: Create a simple in-memory list to store items
# items_db = []
# next_id = 1


# ============================================================================
# API Endpoints - Task 1: GET Endpoints
# ============================================================================
# TODO: Implement GET /items endpoint
# TODO: Implement GET /items/{item_id} endpoint


# ============================================================================
# API Endpoints - Task 2: POST and DELETE Endpoints
# ============================================================================
# TODO: Implement POST /items endpoint
# TODO: Implement DELETE /items/{item_id} endpoint


# ============================================================================
# API Endpoints - Task 3: Query Parameters and Advanced Routing
# ============================================================================
# TODO: Implement GET /items with query parameters (skip, limit)
# TODO: Implement GET /search?query={search_term} endpoint
# TODO: Implement PUT /items/{item_id} endpoint


# ============================================================================
# API Endpoints - Task 4: Root Endpoint (Stretch Goal)
# ============================================================================
# TODO: Implement GET / endpoint with API documentation


# ============================================================================
# Run the Application
# ============================================================================
if __name__ == "__main__":
    # To run this application, use:
    # uvicorn starter_code:app --reload
    #
    # Then visit http://127.0.0.1:8000/docs to see the interactive API documentation
    pass
