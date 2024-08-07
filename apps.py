from django.apps import AppConfig
import pickle


class PredictorConfig(AppConfig):
    name = 'stockmarket'
    path = r'/Users/dhruvrao/reliancemarket.sav'
    with open(path, 'rb') as pickled:
        model = pickle.load(pickled)