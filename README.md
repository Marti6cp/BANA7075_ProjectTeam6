# Amazon E-Commerce Product Demand Forecasting 
BANA 7075 - Final Project - Team 6 
## Description
This project uses machine learning to forecast monthly product demand for Amazon e-commerce data, where demand is the number of purchase transactions per product, per month. The goal is to help the Amazon inventory teams make better restocking decisions and reduce stockouts and excess inventory. 
## Pipeline 
The table below shows the tools used at each stage of the pipeline.

| Stage | Tool |
|-------|------|
| Data ingestion | KaggleHub |
| Data validation | Great Expectations |
| Data and code versioning | DVC and GitHub |
| Model training | Linear Regression, Random Forest, and XGBoost |
| Experiment tracking | MLflow |
| Model comparison | MAE, RMSE, and R² |
| Deployment | FastAPI prediction with Streamlit interface |


## Team Members 
Tayo Akinyeke, William Eades, Christopher Martinez, Yosef Othman, and Matthew True

## Instructions to Run the Prediction App

### Requirements

- Python 3.13, standard 64-bit installation
- A local clone of this repository

The repository includes the trained model and fitted preprocessor.
Retraining, Colab, and AWS credentials are not required to run predictions.

### First-Time Setup (in Windows PowerShell)

Open a terminal in the repository folder and run:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

### Start the App

Start FastAPI in one terminal:

```powershell
.\.venv\Scripts\python.exe -m uvicorn fastAPI_setup:app --reload
```

Leave that terminal running. Open a second terminal in the same folder and start Streamlit:

```powershell
.\.venv\Scripts\python.exe -m streamlit run Streamlit_app.py
```

Open http://127.0.0.1:8501 in your browser.

### Make Predictions

1. Download the sample inputs from the Streamlit page or use
   `sample_prediction_inputs.csv` from the repository.
2. Upload the CSV.
3. Click **Predict demand**.
4. Review the predictions and download the results.

Predicted demand represents the estimated number of purchases per
product-month. Decimal predictions are expected for regression models.

### Required Files

Keep the below files in the same folder as `fastAPI_setup.py` and `Streamlit_app.py`:

- `model_preprocessor.joblib`
- `demand_model.ubj`
- `model_features.json`

`sample_prediction_inputs.csv` provides example inputs.
`sample_predictions.csv` provides example output.

### Stop and Restart

Press **Ctrl+C** in each terminal to stop the services.

For later sessions, reuse the existing `.venv` and run the two startup
commands. Package installation and model training do not need to be repeated.

### Training Dependencies

`requirements.txt` covers the prediction app only. The training notebook
also uses KaggleHub, Great Expectations, DVC, MLflow, and plotting packages.
Training and exporting a new model is a separate workflow.