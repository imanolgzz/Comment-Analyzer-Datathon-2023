import pandas as pd
from textblob import TextBlob
from better_profanity import Profanity

# Input
dataBasePath = "exampleData.xlsx" # The database should be in the same directory as this file to work as expected
sheetName = "comments"
rateColumn = "rating"
columnToAnalize = "message"

# Function to clean the data
def cleanData(inputDataFrame):
    outputDataFrame = []
    # Create the profanity tester
    profanityTester = Profanity()

    for i in range(len(inputDataFrame)):
        text = str(inputDataFrame.iloc[i,0])
        textLength = len(text.split())
        if textLength < 3:  # Validates if the comment has at least 3 words to be considered in the output
            continue

        textBlobText = TextBlob(text) # Create the TextBlob object to work with it

        # The try except is used to avoid errors when the text is not in spanish as expected with the datasets
        try:
            translatedText = textBlobText.translate(from_lang = "es", to="eng") # Translate the text to english
        except:
            continue

        # Check if the text has profanity
        profanity =  profanityTester.contains_profanity(translatedText)

        # If the text has profanity, it is not considered in the output
        if profanity == False:
            outputDataFrame.append(str(translatedText))
        else:
            continue
    return outputDataFrame

# Read the file
dataBase = pd.read_excel(dataBasePath, sheet_name= sheetName)

# Separate the comments in tree groups according to the rate
grade0_3 = dataBase(dataBase[rateColumn].isin(range(4)))
grade4_7 = dataBase(dataBase[rateColumn].isin(range(4,8)))
grade8_10 = dataBase(dataBase[rateColumn].isin(range(8,11)))

# Drop every column except the one to analize
grade0_3 = grade0_3.drop(columns=grade0_3.columns.difference([columnToAnalize]))
grade4_7 = grade4_7.drop(columns=grade4_7.columns.difference([columnToAnalize]))
grade8_10 = grade8_10.drop(columns=grade8_10.columns.difference([columnToAnalize]))

# Write the output of the tree groups in different sheets in the same file
grade0_3_output = pd.DataFrame(cleanData(grade0_3), columns=['text'])
grade4_7_output = pd.DataFrame(cleanData(grade4_7), columns=['text'])
grade8_10_output = pd.DataFrame(cleanData(grade8_10), columns=['text'])

with pd.ExcelWriter('cleanDatabase.xlsx') as writer:
    grade0_3_output.to_excel(writer, sheet_name='0-3')
    grade4_7_output.to_excel(writer, sheet_name='4-7')
    grade8_10_output.to_excel(writer, sheet_name='8-10')