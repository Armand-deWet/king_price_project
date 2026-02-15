# Porcupine Union Enterprise AI Team Interview Task

## Project Overview

This repository contains the solution for the Porcupine Union Enterprise AI Team interview task. The objective is to develop a machine learning model to predict the number of annual public destruction events caused by superheroes based on their credit information.

**Context:**
You are a data scientist at a Marvel Universe insurance company, "Public Destruction Liability Insurance". The goal is to assess risk for new superhero clients.

## Repository Structure

The project is organized as follows:

- **`fastapi_api/`**: Contains the production-ready FastAPI application and the trained regression model.
  - `main.py`: The entry point for the REST API.
  - `src/`: Source code for routes and model logic.
  - `superhero_model.joblib`: serialized model.
- **`model_development/`**: Contains Jupyter notebooks used for Exploratory Data Analysis (EDA), model development, and hyperparameter tuning.
- **`report/`**: Contains the final report (PDF) detailing the experimental procedure, results, and deployment strategy.
- **`streamlit_app.py`**: A Streamlit web application that provides a user-friendly UI for interacting with the prediction model.
- **`requirements.txt`**: List of Python dependencies required to run the project.

## Setup & Installation

1.  **Clone the repository** (or unzip the project file):
    ```bash
    git clone <repository_url>
    cd <repository_name>
    ```
    *Note: If you have received this project as a zipped file, unzip it and navigate to the unzipped folder.*

2.  **Create and activate a virtual environment** (recommended):
    ```bash
    python -m venv .venv
    # Windows
    .venv\Scripts\activate
    # macOS/Linux
    source .venv/bin/activate
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### 1. Run the FastAPI Application
The REST API allows you to send requests and get predictions programmatically.

To start the server:
```bash
python fastapi_api/main.py
```


### 2. Run the Streamlit App (UI)
The Streamlit app provides an interactive interface to explore the model predictions.

To launch the app:
```bash
python -m streamlit run streamlit_app.py
```
This will verify installation and open the app in your default web browser.

### 3. Model Development
To view the analysis and training process, navigate to the `model_development` directory and open the Jupyter notebook(s):
```bash
jupyter notebook model_development/
```

## Task Details
- **Data Source**: `superhero_events_db.duckdb` (DuckDB database).
- **Goal**: Predict `annual_public_destruction_events` using `CreditInfo`.
- **Note**: The Streamlit application was developed as an extra feature to demonstrate commitment to providing a complete solution.

## Contact
**Candidate**: Armand de Wet | armand.dewet40@gmail.com
**Date**: 2026-02-11

