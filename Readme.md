# AI OPERATIONS ASSISTANT

## Overview

AI Operations Assistant is a multi-agent system that understands natural language requests, converts them into a structured execution plan, calls real external tools, and produces a clear end-to-end response through a web interface.

The system demonstrates:
- Multi-agent reasoning
- Use of an LLM with structured outputs
- Real third-party API integration
- Modular architecture
- A working application that runs locally in one command

---

## Architecture

The system follows a three-agent pipeline:

User Input  
→ Planner Agent  
→ Executor Agent  
→ Verifier Agent  
→ Final Response  

### Planner Agent (agents/planner.py)

The Planner takes the user’s natural language request and uses an LLM to generate a structured JSON plan. This plan defines which tools should be used and in what order.

### Executor Agent (agents/executor.py)

The Executor reads the planner output and calls the corresponding tools. It collects the results from each tool and returns them in a structured format.

It integrates:
- GitHub tool to fetch repository information  
- OpenWeather tool to fetch live weather data  

### Verifier Agent (agents/verifier.py)

The Verifier takes the raw tool outputs and converts them into a clean, structured, and readable response for the user. It ensures:
- Clear headings  
- Proper formatting  
- Professional tone  
- No internal system references  

---

## Integrated APIs

This project integrates two real third-party APIs as required.

### GitHub Search API  
Used to fetch top repositories based on user queries, including:
- Repository name  
- Star count  
- GitHub URL  
- Description  

### OpenWeather API  
Used to fetch real-time weather information for any city, including:
- Temperature  
- Humidity  
- Weather condition  

---

## Setup Instructions to Run Locally

### Step 1: Clone the repository

## Step 2: Install dependencies
Create a `.env` file in the root directory with:

OPENWEATHER_API_KEY=your_openweather_api_key
HUGGINGFACE_API_KEY=your_huggingface_api_key


A sample template is provided in `.env.example`.

### Step 4: Start the local LLM

Run the local model using Ollama:

ollama run phi3


### Step 5: Run the application

Start the FastAPI server:

uvicorn main:app --reload


Open your browser and go to:

http://127.0.0.1:8000


---

## Example Prompts to Test the System

Try these in the web interface:

1. Find top 2 AI repositories and weather in Bangalore  
2. Find top 3 machine learning repositories and weather in Mumbai  
3. Find top Python automation repository and weather in Chennai  
4. Show top cybersecurity repositories and weather in Delhi  
5. Find best AI research repositories and weather in Hyderabad  

---

## Known Limitations and Tradeoffs

### Latency  
Responses may take 5 to 15 seconds due to local LLM processing and real API calls.

### Rate Limits  
The GitHub API may throttle requests if used excessively.

### Stateless Design  
Each request is processed independently with no conversation memory.

### Local Model Constraints  
The local model (phi3) is smaller than cloud-based models like GPT-4.




