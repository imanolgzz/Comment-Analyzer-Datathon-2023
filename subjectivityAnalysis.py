from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier, MaxEntClassifier
import pandas as pd

# Training data for the model
train = [
   ('I love this airplane company', 'positive'),
   ('This is an amazing place!', 'positive'),    
   ('I feel very good about this trip', 'positive'),
   ('I do not like this plane', 'negative'),
   ('I am tired of this stuff.', 'negative'),
   ("I can't deal with this", 'negative'),
   ("The pilot was terrible", "negative"),
   ("I'm happy", "positive"),
   ("I'm not happy", "negative"),
   ("Terrible activity", "negative"), 
   ("Greatest", "negative"),
   ("bad trip", "negative"),
   ("terrible trip", "negative"), 
   ("would not come again", "negative"),
   ("Great, just change the AC", "positive"), 
   ("Overall good experience", "positive"), 
   ("The app was terrible", "negative"), 
   ("I can't pay through the app, please fix it", "positive"), 
   ("Please fix the app", "negative"), 
   ("I loved the mobile application!", "positive"), 
   ("the app did not take my cards, improve", "negative"), 
   ("hated the service", "negative"),
   ("I despise the application", "negative"), 
   ("It charged me more than it should", "negative"),
   ("It is totally unfair", "negative"), 
   ("Abusive", "negative"), 
   ("Makes me angry", "negative"),
   ("A robbery", "negative"), 
   ("Error", "negative"), 
   ("It keeps making errors", "negative"), 
   ("Because of the error I have to pay more", "negative"),
   ("Paid extra charges", "negative")
]

# Declare the paths
databasePath = "dataToAnalize.xlsx"

# Create the Naive Bayes clasifier
cl = NaiveBayesClassifier(train)

# Create the MaxEnt clasifier
probClassifier = MaxEntClassifier(train)

sentencesToCheck = []
responses = []
probabilityKeeper = []
intensity=[]

# Convert the file to a dataframe
db = pd.read_excel(databasePath)

# Iterarate over the charged 
for s in range(len(db)):
    sentencesToCheck.append(db.iloc[s,0])
    text = db.iloc[s,0]
    
    # Clasify the text using the Naive Bayes clasifier
    blobbedText = TextBlob(text, classifier=cl)
    responses.append(str(blobbedText.classify()))
    
    # Calculate the probability using the MaxEnt clasifier
    prob = probClassifier.prob_classify(text)
    trueStat = prob.prob(str(blobbedText.classify()))
    probabilityKeeper.append(trueStat)
    
    # Imprimir la clasificación y la probabilidad
    print(str(blobbedText.classify()), " | ", trueStat)
    intensity.append(trueStat)

# Create a dataframe with the results
df_output = pd.DataFrame()
df_output["Columns"] = sentencesToCheck
df_output["Sentiment"] = responses
df_output["Intensity"]= intensity

# Output
with pd.ExcelWriter("subjectivityAnalysis.xlsx") as writer:
    df_output.to_excel(writer, index=False)