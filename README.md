# Population Growth Prediction

This project predicts the population growth rate for a given year using a machine learning model.

## Team Members

- Nishanth PR
- Nishanth Kumar B S
- Rithin R
- Praveen NR

## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/your_username/your_repo_name.git
    ```

2. Navigate to the project directory:
    ```sh
    cd your_repo_name
    ```

3. Create a virtual environment and install dependencies:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```sh
    python app.py
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000/`.
2. Log in using the credentials:
    - Username: admin
    - Password: password
3. Enter a country, start year, and end year on the index page to get the predicted population growth rate and view the corresponding growth rate plot on the `plot.html` page.

## Model Training

The model is trained using historical population growth data. The training code can be found in `train_model.py`. To retrain the model:

1. Run the training script:
    ```sh
    python train_model.py
    ```

2. The trained model will be saved as `population_growth_model.pkl`.

## Contributing

Please feel free to fork this repository and submit pull requests.

## License

This project is licensed under the MIT License.
