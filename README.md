
# 💰 Health Insurance Premium Prediction

A Streamlit web app to **predict your annual health insurance cost** based on personal, lifestyle, and medical factors.

---

## 🚀 Features

- 📊 User-friendly Streamlit interface
- 🧠 Powered by pre-trained ML models
- 🛠️ Feature engineering: normalized medical risk score, categorical encoding
- 🔍 Real-time prediction of insurance premium
- 📓 Includes Jupyter notebooks to reproduce training

---

## 📸 Screenshots

<!-- Add screenshots here -->

![App Screenshot 1](path/to/screenshot1.png)  
![App Screenshot 2](path/to/screenshot2.png)  

---

## 📦 Project Structure

```
Health_Premium_Prediction/
├── artifacts/                           # Contains trained models & scalers
├── jupyter_notebooks/                   # Jupyter notebooks used for training & experimentation
│   ├── helper.ipynb
│   ├── premium_prediction.ipynb
│   ├── premium_prediction_rest.ipynb
│   ├── premium_prediction_rest_with_gr.ipynb
│   ├── premium_prediction_young.ipynb
│   ├── premium_prediction_young_with_gr.ipynb
├── main.py                              # Streamlit web app
├── prediction_helper.py                 # Data preprocessing & prediction logic
├── requirements.txt                     # Python dependencies
└── README.md                            # Project overview
```

---

## 🏃‍♂️ Running the App

### 1️⃣ Clone the repo

```bash
git clone https://github.com/SomeshJoshi-96/Health_Premium_Prediction.git
cd Health_Premium_Prediction
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit app

```bash
streamlit run main.py
```

---

## ⚙️ How It Works

1. **User fills out the form** in the web interface.
2. The app:
   - Encodes categorical inputs.
   - Computes a normalized medical risk score.
   - Scales numerical inputs.
3. Selects the appropriate ML model (`young` or `rest`) based on age.
4. Outputs the predicted **annual premium**.

---

## 📘 Notebooks

The `jupyter_notebooks/` folder includes training & experimentation notebooks:

- `helper.ipynb`: Utility functions.
- `premium_prediction.ipynb`: Overall training pipeline.
- `premium_prediction_rest.ipynb`: Model for users aged > 25.
- `premium_prediction_young.ipynb`: Model for users aged ≤ 25.
- `*_with_gr.ipynb`: Variants incorporating genetical risk.

---

## 🎓 Model Training

- Models trained externally in provided notebooks.
- Separate models used for:
  - Users aged ≤ 25 → `model_young`
  - Users aged > 25 → `model_rest`

---

## 🛠️ Technologies Used

- 🐍 Python
- 📊 Streamlit
- 🤖 Scikit-learn
- Pandas, NumPy
- Jupyter notebooks
- Joblib

---

## ✍️ Author

- **Somesh Joshi** — [GitHub](https://github.com/SomeshJoshi-96)

---

## 🚧 Future Improvements

- Add automated model training pipeline.
- Improve UI/UX with visual explanations.
- Deploy on Streamlit Cloud / HuggingFace Spaces.
- Add CI/CD for testing new models.

