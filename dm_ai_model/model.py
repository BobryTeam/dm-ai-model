import pandas as pd
import joblib

from trend_data import TrendData

class DecisionModuleModel:
    def __init__(self, model_file: str):
        self.model = joblib.load(model_file)

    def analyze(self, trend: TrendData):
        x = pd.DataFrame({
            'cpu': [trend.cpu_load],
            'memory': [trend.ram_load],
            'traffic': [trend.net_load],
        })
        prediction = self.model.predict(x)
        return prediction[0]
