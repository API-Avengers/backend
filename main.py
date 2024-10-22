import logging
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import google.generativeai as genai  # Import the Google Generative AI library for interacting with Gemini
import os
# Load environment variables from .env
load_dotenv()

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Load API Key from environment variables
google_api_key = os.getenv("GEMINI_API_KEY")

# Set up Google Generative AI client
genai.configure(api_key=google_api_key)  # Use the API key for authentication

# Logging setup
logging.basicConfig(level=logging.INFO)

# Data Model for Trip Details
class TripDetails(BaseModel):
    destination: str
    days: int
    budget: str
    trip_type: str

# POST endpoint to create itinerary using Google Gemini API
@app.post("/create-itinerary/")
async def create_itinerary(trip: TripDetails):
    try:
        # Logging the trip details for debugging
        logging.info(f"Trip Details: {trip}")

        # Construct the prompt for the Gemini AI model
        prompt = (
            f"Please create a detailed itinerary for a {trip.trip_type} trip to {trip.destination} "
            f"for {trip.days} days with a {trip.budget} budget. Include points of interest, "
            "restaurants, and activities for each day."
        )

        # Define generation configuration
        generation_config = genai.types.GenerationConfig(
            candidate_count=1,           # Generate only one candidate output
            max_output_tokens=500,        # Max tokens (control output length)
            temperature=1.0               # Temperature controls randomness/creativity
        )

        # Initialize the generative model
        model = genai.GenerativeModel("gemini-1.5-flash")

        # Generate content using the Gemini model
        response = model.generate_content(prompt, generation_config=generation_config)

        # Log the generated response from Google AI
        logging.info(f"Google Gemini AI Response: {response.text}")

        # Return the generated itinerary in the response
        return {"itinerary": response.text}

    except Exception as e:
        # Log any exceptions that occur during the process
        logging.error(f"Exception during Google AI API call: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate itinerary")
