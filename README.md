**🏠 House Price Prediction**

A machine learning project that predicts house prices based on property features using Linear Regression and provides an interactive Streamlit web application.

**📌 Project Overview**
The goal of this project is to build a regression model that estimates the price of a house from features such as area, number of bedrooms, bathrooms, stories, parking, location-related features, and furnishing status.

**🛠️ Technologies Used**
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Linear Regression
Joblib
Streamlit

**🔄 Project Workflow**
Load the housing dataset
Explore the data
Check and handle missing values
Convert categorical features into numerical features
Split the data into training and testing sets
Train a Linear Regression model
Evaluate the model using MAE, RMSE, and R² score
Save the trained model as model.pkl
Build an interactive Streamlit application

**_📁 Project Structure**
House-Price-Prediction/
│
├── data/
│   └── Housing.csv
│
├── notebooks/
│   └── House_Price_Prediction.ipynb
│
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
└── .gitignore

**🚀 How to Run**
1. Install dependencies
pip install -r requirements.txt
2. Run the Streamlit application
python -m streamlit run app.py
The application will open in your browser.

**📊 Model Evaluation**
The model is evaluated using:

MAE (Mean Absolute Error)

RMSE (Root Mean Squared Error)

R² Score

These metrics help measure how accurately the model predicts house prices.

**💡 Key Learning Outcomes**
Data cleaning and preprocessing

Exploratory Data Analysis

Categorical variable encoding

Regression modeling

Model evaluation

Model serialization with Joblib

Building an ML web application with Streamlit

Preparing an ML project for GitHub

**🔮 Future Improvements**
Compare Linear Regression with Random Forest and other regression algorithms

Perform hyperparameter tuning

Add more advanced feature engineering

Improve the Streamlit interface

Deploy the application online

**👩‍💻 Author**
Bhumika G S
