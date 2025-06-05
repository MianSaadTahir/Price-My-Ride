from flask import Flask, request, render_template
import pandas as pd
import joblib
import tensorflow as tf
from tensorflow.keras import backend as K


def rmse(y_true, y_pred):
    return K.sqrt(K.mean(K.square(y_pred - y_true)))


def r2_score(y_true, y_pred):
    SS_res = K.sum(K.square(y_true - y_pred))
    SS_tot = K.sum(K.square(y_true - K.mean(y_true)))
    return 1 - SS_res / (SS_tot + K.epsilon())


# Load model and columns
model = tf.keras.models.load_model(
    'used_car_price_model.keras',
    custom_objects={'rmse': rmse, 'r2_score': r2_score}
)
column_order = joblib.load('columns.pkl')

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get inputs from form
        brand = request.form['brand']
        fuel_type = request.form['fuel_type']
        transmission = request.form['transmission']
        ext_col = request.form['ext_col']
        int_col = request.form['int_col']
        clean_title = request.form['clean_title']
        year = int(request.form['year'])
        milage = float(request.form['milage'])

        # Prepare one-hot input dictionary
        input_data = {
            f'brand_{brand}': 1,
            f'fuel_type_{fuel_type}': 1,
            f'transmission_{transmission}': 1,
            f'ext_col_{ext_col}': 1,
            f'int_col_{int_col}': 1,
            f'clean_title_{clean_title}': 1,
            'year': year,
            'milage': milage
        }

        # Create DataFrame with zeros for missing columns
        input_df = pd.DataFrame([input_data])
        input_df = input_df.reindex(columns=column_order, fill_value=0)

        # Predict
        pred_price = model.predict(input_df)[0][0]

        return render_template('index.html', prediction_text=f"Estimated Price: ${pred_price:,.2f}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")


if __name__ == "__main__":
    app.run(debug=True)
