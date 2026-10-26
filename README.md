# Enterprise Task Architecture Pipeline

A high-performance, fully decoupled full-stack task execution microservice engineered using modern asynchronous Python backend frameworks, strict server-side type-safety gateways, and relational database persistence.

## 📱 User Interface Preview

![Application Interface](templates/screenshot.png)

---

## 🏛️ System Architecture Layers

The system is designed utilizing a clean, three-layer architectural pattern to isolate concerns and enforce robust data streams:

- **Layer 1: The Frontend Client (`templates/index.html`)**
  Built using responsive HTML5, CSS3, and the Bootstrap 5 UI framework. It leverages native JavaScript and the asynchronous `fetch()` API to package user state data into raw JSON payloads, transferring data quietly over network threads to prevent global page refreshes.

- **Layer 2: The Validation Gateway (`main.py` & `schemas.py`)**
  Powered by FastAPI running on an asynchronous ASGI server configuration. Outfitted with robust Pydantic schemas that intercept data payloads at the API threshold to enforce strict runtime type verification.

- **Layer 3: The Relational Persistence Layer (`database.py` & `models.py`)**
  Implements the SQLAlchemy Object-Relational Mapper (ORM) to abstract data transactions, automatically mapping declarative Python class models directly to structured tables inside an SQLite transactional database.

---

## 🚀 Core Technical Stack

- **Backend Framework:** FastAPI (Asynchronous Python ASGI Web Framework)
- **Data Validation:** Pydantic Core v2 (Strict type-checking)
- **ORM Manager:** SQLAlchemy (Object-Relational Mapping engine)
- **Database Management:** SQLite (Relational SQL database file)
- **Template Engine:** Jinja2 (Context-safe server-side rendering pipelines)
- **Frontend Components:** HTML5, Modern CSS Layouts, Bootstrap v5.3.0, Asynchronous Client JS

---

## 💻 Local Workspace Installation & Execution

Follow these steps to deploy and audit this system locally within your development environment:

1. **Clone the repository architecture:**

   ```bash
   git clone https://github.com
   cd task-manager-fastapi
   ```

2. **Establish runtime global dependencies:**

   ```bash
   pip install fastapi uvicorn sqlalchemy pydantic jinja2
   ```

3. **Initialize the local live-reload execution engine:**

   ```bash
   python -m uvicorn main:app --reload
   ```

4. **Access the operational layers:**
   - Interactive UI Environment: http://127.0.0.1:8000
   - Automated Swagger REST API Documentation Dashboard: http://127.0.0
