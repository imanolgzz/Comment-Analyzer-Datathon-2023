import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
from textblob import TextBlob as tb

# Declare the paths
databasePath = "dataToExtractTopic.xlsx"

# Declare constants for checking
n_features = 10000
n_top_words = 20
n_components = 2

testingDocuments = ["expensive cheap double charge extra charge documented baggage credit cards", "quality trip boring happy disgusted again terrible journey content hate dislike rude like love"]

# Extracting topics from the data
# We are going to declare two topics to categorize each one
topics = ["price", "experience"]


# Initialize the vectorizer and transform the testing documents
tfidf_vectorizer = TfidfVectorizer(max_df=0.95, min_df=0.01, max_features=n_features, stop_words='english', ngram_range=(1, 2))
tfidf = tfidf_vectorizer.fit_transform(testingDocuments)

n_components = min(n_components, n_features)

# Fit the NMF model to the TF-IDF matrix
nmf = NMF(n_components=n_components, init='nndsvd', max_iter=100000).fit(tfidf)

# Function to get the most relevant topic for a given text
def get_relevant_topic(model, vectorizer, topics, text):
    v_text = vectorizer.transform([text])
    topic_scores = model.transform(v_text)
    most_relevant_topic_idx = np.argmax(topic_scores)
    most_relevant_topic = topics[most_relevant_topic_idx]
    return most_relevant_topic


# Convert the file to a dataframe
db = pd.read_excel(databasePath)

# Aquí se debe cambiar por una lista vacía
iterated = []
blob = []

# Iteration of the database
for i in range(0, len(db)):
    text = db.iloc[i,0]
    iterated.append(text)
    relevant_topic = get_relevant_topic(nmf, tfidf_vectorizer, topics, text)
    # print(f"Sentence: {text} | Relevant Topic: {relevant_topic}")
    blob.append(relevant_topic)

df_output = pd.DataFrame()
df_output["Columns"] = iterated
df_output["Topic"] = blob

with pd.ExcelWriter("topicCategorization.xlsx") as writer:
    df_output.to_excel(writer, index = False)