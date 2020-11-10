# multilingual_online_translator
An app that translates the word you type and gives you usage examples based on the context.  
  
This app is based on a project at hyperskill.org: https://hyperskill.org/projects/99?track=2  

Based on the input from commandline the app makes a request to the web ( https://context.reverso.net/translation/ ) and prints translation with example in context.
It saves the translation into a text file.  

Supported languages: ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']  
Also possible to translate to 'all'. 
   
Learning outcomes:   
You will learn to work with loops and conditions, files, pip and packages. You’ll be talking to the web with requests and handle the data with BeautifulSoup libraries.

  
 
  
  
# Example    
**Input:**  
> python translator.py english german hello  
**Output:**    
german Translations:  
hallo  
  
german Example:  
Finally got a personalized hello from Earl.  
Ich habe endlich ein personifiziertes hallo von Earl bekommen.  
