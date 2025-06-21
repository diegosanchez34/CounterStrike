# Counter Strike Match Predictor

This project is a web application that uses machine learning to predict the outcome of a Counter Strike match based on in-game statistics.

## Technologies Used

- **Python 3**
- **Django 4.2.7**: Web framework for building the application.
- **scikit-learn**: For building and running machine learning models.
- **joblib**: For model serialization.
- **numpy** and **pandas**: For data manipulation and preprocessing.
- **Bootstrap 5**: For responsive frontend design.
- **django-crispy-forms** and **django-bootstrap-v5**: For enhanced form rendering.
- **Pillow**: For image processing (if needed).

## Objective

The main goal of this project is to provide a user-friendly interface where users can input match statistics and receive a prediction (Victory or Defeat) for a Counter Strike match using trained machine learning models.

## How to Run

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/CounterStrike.git
   cd CounterStrike
   ```

2. **Create and activate a virtual environment (recommended):**

   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**

   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**

   ```sh
   python manage.py runserver
   ```

6. **Open your browser and go to:**
   ```
   http://127.0.0.1:8000/
   ```

## Notes

- Make sure the machine learning model files (`scaler.pkl`, `logreg.pkl`, `tree_clf.pkl`, `rf_clf_model_compressed.pkl.gz`, `meta_clf.pkl`, `scalerRF.pkl`, `rfc_model_compressed.pkl.gz`) are present in the `CS/modelos/` directory.
- You can customize the frontend in the `CS/templates/` directory.

---

Feel free to contribute or open issues for improvements!
