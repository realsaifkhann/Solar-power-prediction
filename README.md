Solar Power Generation Prediction 🌞

📌 Project Overview
This project predicts solar power generation using environmental and weather-related features. The goal was to build a regression model capable of accurately estimating power output based on factors such as temperature, wind speed, sky cover, and distance to solar noon.

---

🔍 Problem Statement
Given weather and environmental conditions, predict the amount of solar power generated. This helps in energy planning, grid management, and production forecasting.

---

🛠 Project Workflow
1. Data Preprocessing (handling missing values, train-test split, scaling)
2. Exploratory Data Analysis (EDA)
3. Baseline Model – Linear Regression
4. Decision Tree Regressor
5. Random Forest Regressor
6. Cross-Validation
7. Feature Importance

---

📊 Model Performance

| Model               | R² Score |
|---------------------|----------|
| Linear Regression   | 0.62     |
| Decision Tree       | 0.81     |
| Random Forest       | 0.88     |

Random Forest performed best due to its ability to capture nonlinear relationships and reduce overfitting through ensemble learning.

---

📈 Key Insights

- Distance to solar noon was the most important feature.
- The relationship between solar power and distance to solar noon is nonlinear.
- Decision Tree showed overfitting (Training R² = 1.0).
- Random Forest improved generalization and stability.
- Cross-validation ensured model robustness.

---

🧠 Concepts Applied

- Bias–Variance Tradeoff
- Overfitting & Underfitting
- Cross-Validation
- Ensemble Learning (Bagging)
- Hyperparameter Tuning

---

💻 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

---

🚀 Conclusion

Random Forest Regressor achieved the best performance (R² = 0.88) and demonstrated strong generalization ability. This project highlights the importance of model selection, bias-variance tradeoff, and proper validation techniques in regression problems.
