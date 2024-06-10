# Play Together

#### Video Demo: <URL HERE>

#### Description:

Sometimes I have fun playing my guitar accompanying my favorite artists. For this I look for the songs on YouTube and the chords, in general, on the ultimate guitar.
For this I imagined "Play Toghether". Make these searches easier and save them for other times.

Playing together is simple. You provide the name of the song and artist, the application searches YouTube and Ultimete Guitar. The result is some suggestions for videos and lyrics and chords. Those selected must be saved for other days of fun with the guitar.

For everything to work you will need:

Flask (pip install Flask)
CS50 (pip install cs50)
BeautifulSoup (pip install beautifulsoup4)
Flask-Session (pip install Flask-Session)
flask-cors (pip install -U flask-cors)
Google client (pip install google-api-python-client)
dotenv (pip install python-dotenv)

create a sqlite db with the following:
CREATE TABLE playalong (id INTEGER PRIMARY KEY NOT NULL, ytId TEXT NOT NULL, title TEXT NOT NULL, tab TEXT NOT NULL, tabId TEXT NOT NULL)

Acquire the Google api: this will help:
https://developers.google.com/youtube

Need to create an .env file with the following content:
APIYT= your Google API

> [!WARNING]
> This is only for academic purposes. Is the final project for CS50x.
> You should use with discretion.
