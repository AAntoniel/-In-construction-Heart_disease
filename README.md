# Heart Disease Risk Assessment Tool

## About the project

This project is for **educational purposes** only and is intended to serve as an initial screening tool for patients 
at risk of heart disease. It does **not** replace a professional medical diagnosis.

Unlike traditional Data Science approaches (isolated notebooks), this project was architected as a distributed 
application, decoupling the Backend from the Frontend. This ensures scalability,
facilitates maintenance, and allows the model to be consumed by multiple platforms, such as Web and Mobile.

---

## System Architecture

The system follows a Microservices architecture, where the Machine Learning model is served via a RESTful API.

1.  **Backend (FastAPI):** Responsible for loading the trained model, validating input data via Pydantic, and performing 
prediction.
2.  **Frontend (Streamlit):** An intuitive and user-friendly interface designed for the users to 
input their data and visualize risk assessments in real-time.
3.  **Data Exchange:** The Frontend transmits JSON payloads via HTTP requests to the API, receiving 
the calculated risk probability as a response.

---

## Tech Stack

* **Programming Language:** Python
* **Machine Learning:** Scikit-Learn, Pandas, Feature-Engine
* **API / Backend:** FastAPI, Uvicorn, Pydantic
* **Frontend:** Streamlit, Requests

---

## Project Structure

```text
├── backend/
│   ├── main.py                         # API Implementation (FastAPI)
│   ├── model.pkl                       # Serialized Model (Pipeline + Classifier)
│
├── frontend/
│   ├── app.py                          # User Interface (Streamlit)
│
├── notebooks/ 
│   ├── portfolio_heart_disease.py      # Exploratory Data Analysis (EDA) & Model Training
├── requirements.txt                    # Project dependencies
└── README.md                           # Project documentation