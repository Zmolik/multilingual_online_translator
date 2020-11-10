# multilingual_online_translator
An app that translates a word you type and gives you usage examples based on the context.  

Based on the input from command line the app makes a request to the web ( https://context.reverso.net/translation/ ) and prints translation with example in context.
It saves the translation into a text file.  

Supported languages: ['Arabic', 'German', 'English', 'Spanish', 'French', 'Hebrew', 'Japanese', 'Dutch', 'Polish', 'Portuguese', 'Romanian', 'Russian', 'Turkish']  
Also possible to translate to 'all'. 
   
Learning outcomes:   
I've learned to work with loops and conditions, files, pip, packages, requests and handle the data with BeautifulSoup libraries.
 
  
**Example**    
Input:    
*python translator.py english german hello*  
  
Output:

*German Translations:  
hallo  *  
  
*German example:  
Finally got a personalized hello from Earl.  
Ich habe endlich ein personifiziertes hallo von Earl bekommen.  *



This program is based on project from hyperskill.org: https://hyperskill.org/projects/99?track=2   
