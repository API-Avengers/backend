import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import logging
import os
from dotenv import load_dotenv

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

gemini_api_key = os.getenv("GEMINI_API_KEY")

# Logging setup
logging.basicConfig(level=logging.INFO)

# Data Model
class TripDetails(BaseModel):
    destination: str
    days: int
    budget: str
    trip_type: str

# POST endpoint to create itinerary
@app.post("/create-itinerary/")
async def create_itinerary(trip: TripDetails):
    try:
        # Logging the trip details for debugging
        logging.info(f"Received trip details: {trip}")

        # Replace with the correct Gemini API URL
        gemini_api_url = "https://api.gemini.com/itinerary"

        # Example API call to Gemini (replace URL and headers with correct info)
        gemini_response = requests.post(
            gemini_api_url, 
            json={
                "destination": trip.destination,
                "days": trip.days,
                "budget": trip.budget,
                "trip_type": trip.trip_type
            },
            headers={
                "Authorization": f"Bearer {gemini_api_key}"  # Replace with actual key
            }
        )

        # Check if the response is successful
        if gemini_response.status_code != 200:
            logging.error(f"Failed to get response from Gemini: {gemini_response.text}")
            raise HTTPException(status_code=500, detail="Error communicating with Gemini API")
        
        gemini_data = gemini_response.json()

        # Log the data received from Gemini API for debugging
        logging.info(f"Gemini API Response: {gemini_data}")

        # Process the response and return the itinerary
        return {
            "itinerary": gemini_data.get("itinerary", "No itinerary found")
        }

    except requests.exceptions.RequestException as e:
        logging.error(f"Request to Gemini API failed: {e}")
        raise HTTPException(status_code=500, detail="Failed to reach Gemini API")
    
    except Exception as e:
        logging.error(f"Failed to process itinerary: {e}")
        raise HTTPException(status_code=500, detail="Failed to generate itinerary")
