import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

df = pd.read_csv("youtube_comments.csv")

X_train, X_test, y_train, y_test = train_test_split(df["comment"], df["label"], test_size=0.2, random_state=42)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

pipeline.fit(X_train, y_train)

pipeline_score = pipeline.score(X_test, y_test)
print(f"Model Accuracy: {round(pipeline_score * 100, 2)}%")