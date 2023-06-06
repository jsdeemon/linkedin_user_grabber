### Задача 

### Oшибки - как обойти гугл 429 - too many requests 
1 - подключаться к гуглу и парсить оттуда данные пользователей поключевым словам. 
https://practicaldatascience.co.uk/data-science/how-to-scrape-google-search-results-using-python

google query example 
site:linkedin.com/in/ "nodejs developer Russia"

https://www.google.com/search?q=site%3Alinkedin.com%2Fin%2F+%22nodejs+developer+Russia%22&oq=site%3Alinkedin.com%2Fin%2F+%22nodejs+developer+Russia%22&aqs=chrome..69i57j69i58.6166467j0j15&sourceid=chrome&ie=UTF-8

ПРАВИЛЬНЫЙ URL
https://www.google.com/search?q=site%3Alinkedin.com%2Fin%2F+%22python+developer+London

2 - Сохранять это в файл txt с линками польхователей

3 - Брать сохраненный файл с линками пользователей и с помощью либы linkauto отправлять им инвайты
linkauto 
https://github.com/stanvanrooy/linkauto 

### TKINTER COURSE 
https://www.geeksforgeeks.org/python-gui-tkinter/ 

https://www.geeksforgeeks.org/create-first-gui-application-using-python-tkinter/

For cryptography Fernet 
text encrypt and decrypt
https://cryptography.io/en/latest/fernet/


some interesting linkedin projects on github
https://github.com/agusticonesagago/custom_linkedin_messaging 

linkauto 
https://github.com/stanvanrooy/linkauto 



Fix issues with python 3.10 

# UBUNTU / DEBIAN
sudo apt-get install python3-tk

```bash
$ virtualenv venv
$ source venv/bin/activate 
$ pip install tk
``` 

Run the script
```bash
$ python fileName.py
```

