import sys
import joblib
import numpy as np

# Load model once
model = joblib.load("random_forest_model.pkl")

# ==============================
# Prediction Function (Shared)
# ==============================

def predict_power(features):
    features = np.array([features])
    prediction = model.predict(features)
    return round(prediction[0], 2)


# ==============================
# FLASK MODE
# ==============================

def run_flask():
    from flask import Flask, request, render_template

    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("index.html")

    @app.route("/predict", methods=["POST"])
    def predict():
        try:
            features = [float(x) for x in request.form.values()]
            prediction = predict_power(features)

            return render_template(
                "index.html",
                prediction_text=f"Predicted Power Generated: {prediction}"
            )
        except:
            return render_template(
                "index.html",
                prediction_text="Invalid input. Please enter numeric values."
            )

    app.run(debug=True)


# ==============================
# STREAMLIT MODE
# ==============================

def run_streamlit():
    import streamlit as st

    st.set_page_config(page_title="Solar Energy Prediction", layout="centered")

    st.title("☀ Solar Energy Prediction Dashboard")

    inputs = []
    fields = [
        "Distance to Solar Noon",
        "Temperature",
        "Wind Direction",
        "Wind Speed",
        "Sky Cover",
        "Visibility",
        "Humidity",
        "Average Wind Speed (Period)",
        "Average Pressure (Period)"
    ]

    for field in fields:
        value = st.number_input(field, value=0.0)
        inputs.append(value)

    if st.button("Predict Power"):
        prediction = predict_power(inputs)
        st.success(f"Predicted Power Generated: {prediction}")


# ==============================
# MAIN CONTROLLER
# ==============================

if __name__ == "__main__":

    if len(sys.argv) > 1:
        mode = sys.argv[1].lower()

        if mode == "flask":
            run_flask()

        elif mode == "streamlit":
            run_streamlit()

        else:
            print("Invalid argument. Use: flask or streamlit")

    else:
        print("Usage:")
        print("  python app.py flask")
        print("  streamlit run app.py streamlit")
