from flask import Flask, render_template, request
import requests

# Initialize the Flask application
app = Flask(__name__)

# TheMealDB API endpoint for searching by ingredient
API_BASE_URL = "https://www.themealdb.com/api/json/v1/1/filter.php"


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        ingredient = request.form.get("ingredient")
        if ingredient:
            try:
                response = requests.get(API_BASE_URL, params={"i": ingredient})
                response.raise_for_status()

                data = response.json()

                recipes = data.get("meals") or []
                if not recipes:
                    message = f"No recipes found with '{ingredient}'. Please try another ingredient."
                    return render_template("index.html", message=message)

                return render_template("index.html", recipes=recipes)
            except requests.exceptions.RequestException as e:
                error_message = (
                    "Could not connect to the recipe service. Please try again later."
                )
                return render_template("index.html", message=error_message)
    return render_template("index.html", recipes=None)


if __name__ == "__main__":
    app.run(debug=True)
