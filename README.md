# UK-House-Price-Predictor

## Introduction
This is a cutting-edge real estate application designed to simplify and enhance your property decisions. Tailored for Toronto, UK, this app leverages advanced machine learning algorithms to predict accurate house prices based on various factors like property type, style, location, and amenities. Whether you're a buyer, seller, or investor, Worthify provides actionable insights to help you make informed decisions with confidence.

With a user-friendly interface, real-time predictions, and comprehensive property data, this app is your tool for navigating the real estate market efficiently and effectively.

## Model Development Process
In our project to predict house prices in Toronto, we followed a systematic approach to evaluate and optimize the performance of various machine learning models. Below is a detailed explanation of the process and results obtained at each stage:

### 1. Baseline Model: XGBoost
**Model Overview:** We started with the XGBoost algorithm, a robust gradient boosting model known for its high performance in structured data tasks.

**Performance:**
- Accuracy: 64%
- Mean Absolute Error (MAE): 19%

**Insights:** The baseline results provided a strong foundation, highlighting the need for feature optimization to improve accuracy and reduce error.

### 2. Feature Selection Using Recursive Feature Elimination (RFE)
**Methodology:** RFE was applied to identify the most significant features from the dataset. Out of the 25 initial features, 14 were selected based on their contribution to the model's predictive performance.

**Performance After RFE:**
- Accuracy: Slight improvement to 65%
- MAE: Increased slightly to 20%

**Insights:** Feature reduction streamlined the model, but further refinement was needed to improve prediction accuracy and minimize error.

### 3. Support Vector Regression (SVR)
**Model Overview:** SVR was tested to evaluate its performance on the dataset, particularly its ability to handle non-linear relationships.

**Performance:**
- MAE: 0.63

**Insights:** While SVR demonstrated promising results, it was not chosen as the final model due to its relatively higher error compared to other techniques.

### 4. K-Nearest Neighbors (KNN)
**Model Overview:** KNN was implemented to assess its performance on predicting house prices by considering the similarity between neighboring data points.

**Performance:**
- MAE: 0.31

**Insights:** KNN performed reasonably well; however, it was sensitive to the choice of hyperparameters and did not outperform the final model.

### 5. Final Model: CatBoost
**Model Overview:** CatBoost was selected as the final model due to its ability to handle categorical features efficiently and deliver high performance with minimal parameter tuning.

**Performance:**
- MAE: 0.20

**Insights:** CatBoost achieved the lowest error among all tested models, making it the most suitable choice for our house price prediction task.

## Installation Instructions

### Prerequisites
Ensure you have the following installed on your system:
- Python (version 3.9 or above)
- pip (Python package manager)
- Virtualenv (optional but recommended)

### Installation and Setup

#### 1. Clone the Repository
```bash
git clone https://github.com/syedalir1234/
cd UK_HOUSE_PRICE_PREDICTION
```

#### 2. Create and Activate a Virtual Environment
**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

#### 4. Run the Development Server
Start the server with:
```bash
python manage.py runserver
```

Visit the application at: [http://127.0.0.1:8000/index](http://127.0.0.1:8000/index) and get the prediction of house price.

## Usage Guide
Using this app is simple and intuitive:
1. **Select a Property Type:** Choose the type of property (e.g., Detached, Condo, Bungalow) you’re interested in.
2. **Input Key Details:** Enter essential details like the style, size, location, and amenities.
3. **View Predictions:** Instantly receive an accurate price prediction for your chosen property.

## Results
This app delivers detailed results complemented by interactive visuals:
- **Price Predictions:** Displayed in clear numerical values with a breakdown of influencing factors.

