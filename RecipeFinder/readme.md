# Project I: Interactive Recipe Finder 🍲

This is a Flask-based web application that helps users discover new recipes based on ingredients they have available. It connects to a recipe database API to fetch recipes and presents them in an engaging and easy-to-navigate format.

---

## Features

- **Ingredient-Based Search**: Users can enter a primary ingredient to find related recipes.
- **Dynamic Recipe Cards**: Fetched recipes are displayed in a clean, responsive grid layout.
- **External Linking**: Each recipe card links directly to the source website for full instructions.
- **User-Friendly Interface**: A simple and intuitive design for a smooth user experience.

---

## Technologies & API

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, Jinja2
- **API Integration**: `requests` library
- **API Used**: [TheMealDB API](https://www.themealdb.com/api.php)

---

## How to Run

1.  **Navigate to this project directory.**
    ```bash
    cd "RecipeFinder"
    ```
2.  **Create and activate a virtual environment and install dependencies** (see parent README for instructions).

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the application:**

    ```bash
    python app.py
    ```

4.  **Open your web browser** and go to `http://127.0.0.1:5000`.
