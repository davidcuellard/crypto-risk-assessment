# Backend - FastAPI Application

## Component Description

This directory contains the backend application built with FastAPI. It serves the machine learning model predictions via a RESTful API and provides endpoints for historical data used in visualizations.

## Prerequisites

- **Python** 3.11.x
- **Virtual Environment** (recommended)
- **Docker** (optional, if using containerization)

## Installation and Setup

### 1. Navigate to the Backend Directory

```bash
cd backend
```

### 2. Create and Activate a Virtual Environment
On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the FastAPI Server
```bash
uvicorn api:app --reload
```

- The server will start at http://127.0.0.1:8000

### 5. Test the API

- Access the interactive API documentation at http://127.0.0.1:8000/docs

## API Documentation
### Endpoints
- GET /

  - Description: Root endpoint.
  - Response: Welcome message.

- POST /predict
  - Description: Predicts the risk level based on input data.
  - Request Body:

  ```json
  {
    "volatility": float,
    "liquidity": float,
    "momentum": float,
    "avg_sentiment": float
  }
  ```

  - response:

  ```json
  {
    "risk_level": "High Risk" or "Low Risk",
    "prediction": 1 or 0
  }
  ```

- GET /historical-data

  - Description: Returns historical data including dates, prices, and risk scores.
  - Response:

  ```json
    [
    {
      "date": "YYYY-MM-DD",
      "price": float,
      "risk_score": 0 or 1
    },
    ...
  ]
  ```

## Deployment
### Using Docker

1. Build the Docker Image

```bash
docker build -t yourusername/backend:latest .
```

2. Run the Docker Container

```bash
docker run -p 8000:8000 yourusername/backend:latest
```

