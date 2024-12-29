import numpy as np
import joblib
import os
from django.conf import settings


models_folder_path = os.path.join(os.path.dirname(__file__), 'trained_models')
models_folder_path = models_folder_path.replace('\\', '/')
loaded_model = joblib.load(models_folder_path+"/cb_model_grid.joblib")

brokerage = {
            "Other":0,
            "RE/MAX CROSSROADS REALTY INC., BROKERAGE":1,
            "CHESTNUT PARK REAL ESTATE LIMITED, BROKERAGE":2,
            "HOMELIFE LANDMARK REALTY INC., BROKERAGE":3,
            "HOMELIFE NEW WORLD REALTY INC., BROKERAGE":4,
            "CENTURY 21 LEADING EDGE REALTY INC., BROKERAGE":5,
            "RE/MAX REALTRON REALTY INC., BROKERAGE":6,
            "ROYAL LEPAGE SIGNATURE REALTY, BROKERAGE":7,
            "ROYAL LEPAGE/J & D DIVISION, BROKERAGE":8,
            "ROYAL LEPAGE TERREQUITY REALTY, BROKERAGE":9,
            "RE/MAX HALLMARK REALTY LTD., BROKERAGE":10,
            "FOREST HILL REAL ESTATE INC., BROKERAGE":11,
            "RE/MAX WEST REALTY INC., BROKERAGE":12,
            "RIGHT AT HOME REALTY INC., BROKERAGE":13,
            "HARVEY KALLES REAL ESTATE LTD., BROKERAGE":14,
            "ROYAL LEPAGE REAL ESTATE SERVICES LTD., BROKERAGE":15,
            "KELLER WILLIAMS REFERRED URBAN REALTY, BROKERAGE":16,
            "REAL ESTATE HOMEWARD, BROKERAGE":17,
            "ROYAL LEPAGE YOUR COMMUNITY REALTY, BROKERAGE":18,
            "RE/MAX PREMIER INC., BROKERAGE":19,
            "RE/MAX ULTIMATE REALTY INC., BROKERAGE":20,
            "RE/MAX PROFESSIONALS INC., BROKERAGE":21
          }
community = {
        "Bendale":0,
        "Niagara":1,
        "South Riverdale":2,
        "Malvern":3,
        "Annex":4,
        "Waterfront Communities C1":5,
        "Mimico":6,
        "Other":7,
        "Rosedale-Moore Park":8,
        "Mount Olive-Silverstone-Jamestown":9,
        "L'Amoreaux":10,
        "Willowdale West":11,
        "Willowdale East":12,
        "West Humber-Clairville":13,
        "Church-Yonge Corridor":14,
        "Islington-City Centre West":15,
        "Mount Pleasant West":16,
        "Agincourt South-Malvern West":17,
        "Bay Street Corridor":18,
        "Flemingdon Park":19,
        "Woburn":20,
        "Bayview Village":21,
        "Newtonbrook East":22,
        "Banbury-Don Mills":23,
        "Dorset Park":24,
        "Moss Park":25
      }

type = {
   "Condo Apt":0,
   "Condo Townhouse":1,
   "Other":2,
   "Detached":3,
   "Semi-Detached":4,
   "Att/Row/Twnhouse":5
}
style = {
   "Apartment":0,
   "Loft":1,
   "2-Storey":2,
   "Other":3,
   "Stacked Townhse":4,
   "Bungalow":5,
   "2 1/2 Storey":6,
   "3-Storey":7,
   "Bungalow-Raised":8,
   "Multi-Level":9,
   "1 1/2 Storey":10
}


def predict_property(features, brokerage_map = brokerage,
                      community_map = community, type_map = type, 
                      style_map = style, model = loaded_model):
    # Encode categorical features
    features['community'] = community_map.get(features['community'], community_map['Other'])
    features['brokerage'] = brokerage_map.get(features['brokerage'], brokerage_map['Other'])
    features['type'] = type_map.get(features['type'], type_map['Other'])
    features['style'] = style_map.get(features['style'], style_map['Other'])

    # Arrange features in the required sequence
    feature_order = ['lotdepth', 'community', 'washrooms', 'brokerage', 'sqft', 'lotfront', 
                     'type', 'kitchens_plus', 'style', 'rooms_plus', 'rooms', 'garage_spaces', 'parking_spaces']
    
    input_features = np.array([features[feature] for feature in feature_order]).reshape(1, -1)

    # Make prediction
    prediction = model.predict(input_features)
    return prediction[0]
