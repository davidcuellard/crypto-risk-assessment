# Cryptocurrency Risk Assessment Project

## Overview

This project is a comprehensive application designed to assess the risk of cryptocurrencies using machine learning models. It includes a FastAPI backend that serves the ML model predictions and a React frontend for user interaction and data visualization.

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Project Structure

project_root/
├── backend/
├── data/
├── frontend/
├── ml_models/
└── README.md

- **backend/**: Contains the FastAPI application serving the ML model predictions.
- **data/**: Includes datasets and scripts for data processing.
- **frontend/**: Contains the React application for the user interface and visualizations.
- **ml_models/**: Includes scripts and models for training and evaluating the machine learning models.

## Prerequisites

- **Docker** (for containerization)
- **Docker Compose** (optional, for running multiple containers)
- **Node.js** v20.x
- **Python** 3.11.x
- **npm** (comes with Node.js)
- **pip** (comes with Python)

## Installation

1. **Clone the Repository**

```bash
git clone https://github.com/davidcuellard/crypto-risk-assessment.git
```

2. Navigate to the Project Directory

```bash
cd crypto-risk-assessment
```

3.
```bash
docker-compose up --build
```

- Note: Ensure Docker and Docker Compose are installed and running on your system.

## Usage
- Access the Frontend Application
  Open your web browser and navigate to http://localhost:3000.

- Interact with the Application

  - Use the risk assessment form to input data and get risk predictions.
  - View visualizations of risk scores and cryptocurrency prices over time.


## License
[MIT](https://choosealicense.com/licenses/mit/)