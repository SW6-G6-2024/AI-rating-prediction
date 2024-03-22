from output_formatter import output_formatter
from xgboost import XGBClassifier

def get_predicted_ratings(data):
  # load the model
  xgb_model = XGBClassifier()
  xgb_model.load_model('src/saved_models/xgb_model.json')

  # Maybe some sanitizing?

  # make predictions
  xgb_model.predict(data)

  # exported model here
  return output_formatter(data)