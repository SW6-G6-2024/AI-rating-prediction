# AI-rating-prediction
This microservice predicts the ratings of pistes based on the current weather/environmental conditions, using AI models

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