# Enterprise Task Architecture Pipeline

### 👋 Welcome to my portfolio!

Thank you for visiting. This production-ready repository showcases a decoupled, full-stack microservice designed to demonstrate asynchronous backend routing, strict server-side type-safety validation, and relational database persistence.

It represents my transition from academic coding to building structured, secure backend architectures optimized for the modern web.

## 📱 User Interface Preview

![Application Interface](templates/screenshot.png)

---

## 🏛️ System Architecture Layers

The system is designed utilizing a clean, three-layer architectural pattern to isolate concerns and enforce robust data streams:

- **Layer 1: The Frontend Client (`templates/index.html`)**
  Built using responsive HTML5, CSS3, and the Bootstrap 5 UI framework. It leverages native JavaScript event interceptors and the asynchronous `fetch()` API to package client state data into raw JSON payloads, transferring data quietly over network threads to ensure smooth user flow without global page refreshes.

- **Layer 2: The Validation Gateway (`main.py` & `schemas.py`)**
  Powered by **FastAPI** running on an asynchronous ASGI server configuration. Outfitted with robust **Pydantic schemas** (`TaskCreate`) that intercept incoming JSON data strings at the API threshold. It enforces strict runtime type verification and sanitizes input fields, dropping malformed or empty requests before they can touch down into internal service layers.

- **Layer 3: The Relational Persistence Layer (`database.py` & `models.py`)**
  Implements the **SQLAlchemy Object-Relational Mapper (ORM)** to abstract data transactions. Instead of hardcoding raw, vulnerable SQL text strings, SQLAlchemy reads declarative Python class models and automatically translates them into structured relational tables inside a local **SQLite database (`tasks.db`)**, ensuring permanent data persistence and safety against SQL injections.

---

## 🚀 Core Technical Stack

- **Backend Engine:** FastAPI (Asynchronous Python ASGI Web Framework)
- **Data Validation:** Pydantic Core v2 (Strict type-checking gateways)
- **ORM Manager:** SQLAlchemy (Object-Relational Mapping engine)
- **Database Layer:** SQLite (Relational SQL transactional database file)
- **Template Pipeline:** Jinja2 (Context-safe server-side web rendering)
- **Frontend Presentation:** HTML5, Modern CSS Layouts, Bootstrap v5.3.0, Asynchronous Client JavaScript

---

## 💻 Local Workspace Installation & Execution

Follow these steps to deploy, run, and audit this system locally within your development environment:

1. **Clone the repository architecture:**

   ```bash
   git clone https://github.com
   cd task-manager-fastapi
   ```

2. **Establish runtime environment dependencies:**

   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic jinja2
   ```

3. **Initialize the local live-reload execution engine:**

   ```bash
   python -m uvicorn main:app --reload
   ```

4. **Access the operational layers:**
   - **Interactive User Interface Layer:** [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - **Automated Swagger REST API Documentation Dashboard:** [http://127.0.0](http://127.0.0)
