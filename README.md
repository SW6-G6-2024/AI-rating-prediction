# AI-rating-prediction
This microservice predicts the ratings of pistes based on the current weather/environmental conditions, using AI models

## How to use

To get a rating, you can use postman 

<b>POST TO</b> 
```html
http://localhost:1337/ratings/predict
```

<b>WITH THIS FORMAT</b>
```json
{
    "pisteList": [
        {"pisteId": 1},
        {"pisteId": 3},
        {"pisteId": 5},
    ],
    "weather": {
        "temperature": 7.8,
        "weatherCode": 2,
        "windSpeed": 9.407048617566698,
        "windDirection": 158,
        "snowfall": 0,
        "snowDepth": 68.12066453421069,
        "rain": 0,
        "visibility": 1859.8565326225944
    },
    "year": 2023,
    "month": 2,
    "day": 3,
    "hour": 7
}
```

# Return format

<i>Once pisteId are implemented to training data, "test" will be replaced with actual piste id</i> 😎

```json
[
  {
    "piste": "test",
    "rating": 1
  },
  {
    "piste": "test",
    "rating": 1
  },
  {
    "piste": "test",
    "rating": 1
  },
]
```

## How to run

It is recommended that unless you run in Docker, you should run this in a virtual environment.

Windows:

```
py -m venv .venv
```

Unix/Mac:
```
python3 -m venv .venv
```

You should now have a .venv folder.
Once you have that, run below command in terminal:

Windows:
```
.venv\Scripts\activate
```

Unix/Mac:
```
source .venv/bin/activate
```

Run following command in terminal, to download dependencies:
```
pip install -r requirements.txt
```

To run the server, use following command:
```
flask --app main --debug run 
```

## Adding new dependencies
To add dependencies, just install them with pip in your virtual environment. Once installed, inside your virtual environment, use below command to add dependencies to requirements.txt file.
```py
pip freeze > requirements.txt
```

## Dependencies
- <strong>Flask</strong> - Web framework for API endpoints
- <strong>PyTorch</strong> - Tensor used for training AI model
- <strong>NumPy</strong> - Fast scientific computing
- <strong>Pandas</strong> - Data analysis tool
- <strong>Seaborn</strong> - Data visualization tool
- <strong>Pytest</strong> - Testing library