
---

### Backend `README.md`:

# Travel Itinerary App - Backend

### Dependencies

To get started with the backend, make sure you have the following dependencies installed:

- **FastAPI**: For building APIs
- **Uvicorn**: ASGI server for FastAPI
- **Requests**: To make HTTP requests to external APIs
- **python-dotenv**: To load environment variables
- **CORS Middleware**: For cross-origin resource sharing (CORS)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/API-Avengers/backend.git
   cd backend

2. **Create a virtual environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`

3.  **Install dependencies**:

   ```pip install fastapi uvicorn requests python-dotenv```

4. **Create .env file**:

   ```GEMINI_API_KEY=your-gemini-api-key```

5. **Run the FastAPI server**:

   ```uvicorn main:app --reload```
