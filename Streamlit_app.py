from pathlib import Path
import json
import pandas as pd
import requests
import streamlit as st

folder = Path(__file__).resolve().parent

st.set_page_config(page_title="Demand Prediction")
st.title("Ecommerce Demand Prediction")

feature_file = folder / "model_features.json"

if not feature_file.exists():
    st.error("Run ModelOps first to create model_features.json.")
    st.stop()

features = json.loads(feature_file.read_text())

sample_file = folder / "sample_prediction_inputs.csv"

if sample_file.exists():
    st.download_button("Download sample inputs",
        data=sample_file.read_bytes(),
        file_name="sample_prediction_inputs.csv",
        mime="text/csv",)

uploaded_file = st.file_uploader("Upload prediction inputs", type="csv")

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
    except (ValueError, pd.errors.ParserError) as error:
        st.error(f"Cannot read CSV: {error}")
        st.stop()

    missing = [column for column in features if column not in data.columns]

    if missing:
        st.error(f"Missing columns: {', '.join(missing)}")
        st.stop()

    if data.empty or data[features].isna().any().any():
        st.error("Upload nonempty data with no missing feature values.")
        st.stop()

    st.dataframe(data, use_container_width=True)

    if st.button("Predict demand"):
        records = json.loads(data[features].to_json(orient="records"))

        try:
            response = requests.post("http://127.0.0.1:8000/predict",
                json={"records": records},
                timeout=60)
            response.raise_for_status()
            results = data.copy()
            results["predicted_demand"] = response.json()["predictions"]
            st.dataframe(results, use_container_width=True)
            st.download_button("Download predictions",
                data=results.to_csv(index=False).encode("utf-8"),
                file_name="predictions.csv",
                mime="text/csv",)
        except (requests.RequestException, ValueError, KeyError) as error:
            st.error(f"Prediction failed. Check that FastAPI is running: {error}")