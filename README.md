# Comment Analyzer Datathon 2023 Project

## Authors
- [Imanol Armando González Solís](https://github.com/imanolgzz)
- [Marco Antonio Lució Sosa](https://github.com/marcoolucio17)
- [Pedro Gabriel Sanchez Valdez](https://github.com/Pedrosan26)
- [José Miguel Guerrero Jiménez](https://github.com/WarriorMind04)

## Overview
This program was build using Pandas, TextBlob and Profanity_Checker libraries to perform sentiment analysis and detect inappropriate comments in a set of customer reviews for VivaAerobus. The goal was to delete inappropriate or abusive comments, determine overall customer satisfaction and obtain the main complaints of customers in order to improve in these areas. This project was done in a 24-hour data science marathon on May 6-7th , 2023 and for confidentiality reasons the code was modified to work with sample databases created by us.

## *dataCleaner.py*

This code performs the following tasks:

1. Imports the necessary libraries: `pandas`, `TextBlob`, and `Profanity`.
2. Defines the necessary variables, such as the database file path, sheet name, rate column, and column to analyze.
3. Defines a function called `cleanData` to clean the data.
4. Reads the Excel file using `pd.read_excel`.
5. Separates the comments into three groups based on the rating.
6. Drops unnecessary columns from each group, keeping only the column to analyze.
7. Calls the `cleanData` function on each group to clean the comments.
8. Writes the cleaned data into different sheets in a new Excel file called 'cleanDatabase.xlsx'.

## *topicExtraction.py*

This code performs the following tasks:

1. Import the libraries pandas, numpy, sklearn, and textblob.
2. Declare the path of the file `dataToExtractTopic.xlsx`.
3. Set the constants `n_features`, `n_top_words`, and `n_components`.
4. Define the testing documents as a list of sentences.
5. Define the topics as a list of category names.
6. Initialize the TfidfVectorizer with specified parameters and transform the testing documents.
7. Fit the NMF model to the TF-IDF matrix.
8. Define a function `get_relevant_topic` to get the most relevant topic for a given text.
9. Read the database file `dataToExtractTopic.xlsx` into a DataFrame.
10. Iterate over each text in the database and determine the relevant topic using the `get_relevant_topic` function.
11. Create a new DataFrame with columns "Columns" and "Topic" to store the text and its corresponding topic.
12. Save the DataFrame to an Excel file named "topicCategorization.xlsx".


## *subjectivityAnalysis.py*
The code performs sentiment analysis on a dataset using the TextBlob library, Naive Bayes classifier, and MaxEnt classifier. Here's a breakdown of the steps:

1. Import the necessary libraries: `TextBlob`, `NaiveBayesClassifier`, `MaxEntClassifier`, and `pandas`.
2. Define the training data for the sentiment analysis model.
3. Declare the path to the database file.
4. Create the Naive Bayes classifier using the training data.
5. Create the MaxEnt classifier using the training data.
6. Prepare lists to store sentences, responses, probabilities, and intensities.
7. Read the database file into a pandas dataframe.
8. Iterate over the sentences in the database.
9. Append each sentence to the list of sentences to check.
10. Classify the text using the Naive Bayes classifier from TextBlob.
11. Append the classified sentiment to the list of responses.
12. Calculate the probability of the sentiment using the MaxEnt classifier.
13. Append the probability to the list of probabilities.
14. Print the sentiment classification and probability for each sentence.
15. Create a pandas dataframe with the results.
16. Write the dataframe to an Excel file named "subjectivityAnalysis.xlsx".
