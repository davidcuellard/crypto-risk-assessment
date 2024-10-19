# Frontend - React Application

## Component Description

This directory contains the frontend application built with React. It provides a user interface for interacting with the risk assessment model and visualizing data.

## Prerequisites

- **Node.js** v20.x
- **npm** (comes with Node.js)
- **Docker** (optional, if using containerization)

## Installation and Setup

### 1. Navigate to the Frontend Directory

```bash
cd frontend
```

2. Install Dependencies
```bash
npm install
```

3. Configure Environment Variables

- Create a .env file in the /frontend/ directory:

  ```env
  REACT_APP_API_BASE_URL=http://localhost:8000
  ```

  - Adjust the REACT_APP_API_BASE_URL if your backend is hosted elsewhere.

4. Run the React Application

```bash
npm start
```

- The application will start at http://localhost:3000.

## Configuration
- API Base URL

  - Ensure the REACT_APP_API_BASE_URL environment variable points to the backend API.
  - This is used in the application to make API requests.

## Deployment
### Using Docker
1. Build the Docker Image

``` bash
docker build -t yourusername/frontend:latest .
```

2. Run the Docker Container

``` bash
docker run -p 3000:3000 yourusername/frontend:latest
```

### Building for Production
- Create a production build:

```bash
npm run build
```

- Serve the build files using a static server or deploy to a hosting service.

## Notes
- Ensure that the backend API is running and accessible.
- Adjust the chart and form components as needed for additional features.