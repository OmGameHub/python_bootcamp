import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st


df = pd.read_csv("book_recommendations.csv")
df["title"] = df["title"].str.strip()
df["description"] = df["description"].fillna("")

vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["description"])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
indices = pd.Series(df.index, index=df["title"].str.lower()).drop_duplicates()

def get_recommendations(title, df, cosine_sim, indices):
    title = title.lower().strip()
    if title not in indices:
        return f"{title} not found in the dataset."

    idx = indices[title]
    if isinstance(idx, pd.Series):
        idx = idx.iloc[0]

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    book_indices = [i[0] for i in sim_scores]
    return df[["title", "author"]].iloc[book_indices]

st.title("Book Recommendations")
st.write("Enter a book title to get recommendations based on similar books:")

select_book = st.text_input("Book Title:")
if select_book:
    recommended_books = get_recommendations(select_book, df, cosine_sim, indices)

    if isinstance(recommended_books, str):
        st.error(recommended_books)
    else:
        st.write("Recommendations:")
        st.table(recommended_books)
