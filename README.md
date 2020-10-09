# WordFrequency

## Goal
Code to return word frequencies while eliminating all punctuations at the end of the word.

## Extra Features
- Creating a wordcloud (Again, while eliminating punctuations
- Print frequencies (dict) in a redable format

## Understanding Functions
### \_\_init\_\_
Description: Constructor with 2 arguments\
\
Parameters:\
**file_name**: Name of the text file. Default is "text.txt"\
**punc**: String conrtaining all the punctuations (or other charecters) to be eliminated while counting frequencies (**Note**: No changes will be made to the text file). Default is ".,;:\"\'-_1234567890"\
\
Returns: None

### count
Description: Conunts frequencies of words irrespective of upper or lower case while eliminating all punctuations (from punc) at the end of each word and stores it in a dictionary\
\
Parameters: None\
\
Returns: Dictionary of all word frequencies

### top_words
Description: Returns top n number of words, including ties\
\
Parameters:\
**num**: The number of words you want function to return\
\
Returns: Dictionary contining top n frequencies and words, including ties

### pretty
Description: Prints given dictionary in a readable format\
\
Parameters:\
**my_dict**: The dictionary you want to print in a readable format\
\
Returns: None

### word_cloud
Description: Prints a wordcloud of words formed in count function (After eliminating given punctuations)\
\
Parameters:\
**stopwords**: list of words (strings) you dont want to include in the wordcloud. Default is []\
\
Returns: None
