# Enterprise Task Architecture Pipeline

A production-ready repository showcasing a decoupled, full-stack microservice designed to demonstrate asynchronous backend routing, strict type-safety data validation, and relational persistence. For the complete template and configuration details, please refer to the referenced repository.

## 🏛️ System Architecture Layers

- **Layer 1: The Frontend Client (`templates/index.html`)** — Responsive HTML5 UI using Bootstrap v5.3 and asynchronous `fetch()` API calls.
- **Layer 2: The Validation Gateway (`main.py` & `schemas.py`)** — Driven by **FastAPI** and **Pydantic schemas** for type safety.
- **Layer 3: The Relational Persistence Layer (`database.py` & `models.py`)** — Uses **SQLAlchemy ORM** with **SQLite (`tasks.db`)**.

## 🚀 Core Technical Stack

- FastAPI, Pydantic, SQLAlchemy, SQLite, Jinja2, Bootstrap v5.3.

## 💻 Local Workspace Installation

Clone, install requirements, and run via Uvicorn. Full setup instructions are available in.
