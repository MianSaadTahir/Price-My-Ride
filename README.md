# Price My Ride

An AI-powered used car price prediction system built using a deep learning model. It estimates the market price of used cars based on various features such as mileage, fuel type, brand, transmission, and condition. The project uses a fully cleaned and preprocessed dataset and is implemented using TensorFlow and Scikit-learn. This research project also includes a formal **IEEE-style research paper** that discusses the methodology, model architecture, evaluation metrics, results and conclusions in detail.

## Table of Contents
- [Features](#features)
- [Model Architecture](#model-architecture)
- [Poster](#poster)
- [Screenshots](#screenshots)
- [Usage](#usage)
- [Documentation](#documentation)
- [Technologies Used](#technologies-used)
- [Research Paper](#research-paper)
- [Contributing](#contributing)

## Features
- **Data Cleaning & Preprocessing**: Cleaned columns such as `milage`, `price`, and handled missing values.
- **Label Encoding**: Converted categorical variables to numerical format for model training.
- **Model Architecture**: Deep Neural Network (DNN) with three hidden layers using ReLU activation.
- **Evaluation Metrics**: Included RMSE and R² metrics using Keras backend for better evaluation.
- **Visualizations**: Tracked and plotted training loss, MAE, MSE, and RMSE over epochs.
- **Model Saving**: Final model exported as `used_car_price_model.keras`.

## Model Architecture
- **Input Layer**: Accepts features such as mileage, fuel type, transmission, etc.
- **Hidden Layers**:
  - Dense(128, ReLU)
  - Dense(64, ReLU)
  - Dense(32, ReLU)
- **Output Layer**: Dense(1) for regression output
- **Optimizer**: Adam  
- **Loss Function**: Mean Absolute Error (MAE)  
- **Metrics**: MAE, MSE, RMSE, R²

## Poster
<img src="assets/poster.PNG" alt="Screenshot" width="75%">

## Screenshots
<img src="assets/ui.jpeg" alt="Screenshot" width="75%">

## Usage
1. Clone the repository
   `git clone https://github.com/miansaadtahir/Price-My-Ride.git`
2. Navigate to the project directory
   `cd PriceMyRide\app`
3. Create and activate virtual environment <br>
   `python -m venv venv` <br>
   `venv\Scripts\activate`
4. Install dependencies
   `pip install -r requirements.txt`
5. Run the application inside project directory terminal
   `python app.py`
6. Open the local address shown in the terminal `(e.g., http://127.0.0.1:5000)` in your browser to start using the app.

## Documentation
For a detailed overview of the project, refer to the [Documentation](./documentation) in the repository.

## Technologies Used
- Python
- Flask
- TensorFlow & Keras
- Scikit-learn
- Pandas
- NumPy 
- Matplotlib

## Research Paper
This project is accompanied by a complete IEEE-style research paper, which includes:
- Problem statement, literature review
- Methodology, data preprocessing, model design and evaluation
- Results and conclusion along with references

## Contributing
Contributions, issues, and feature requests are welcome!  
Feel free to check out the [issues page](https://github.com/miansaadtahir/Price-My-Ride/issues) for more information.
