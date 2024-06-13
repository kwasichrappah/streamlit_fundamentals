import joblib

def load_catboost_pipeline():
    pipeline = joblib.load("./models/CatBoost.joblib")
    return pipeline
cat_boost = load_catboost_pipeline()
print(cat_boost)