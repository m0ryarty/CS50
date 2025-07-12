# Play Together

#### Video Demo: <URL HERE>

#### Description:

Sometimes I have fun playing my guitar accompanying my favorite artists. For this I look for the songs on YouTube and the chords, in general, on the ultimate guitar.
For this I imagined "Play Toghether". Make these searches easier and save them for other times.

Playing together is simple. You provide the name of the song and artist, the application searches YouTube and Ultimate Guitar. The result is some suggestions for videos and lyrics and chords. Those selected must be saved for other days of fun with the guitar.

On the first page you'l need to provide the name of the song or select one of songs saved previously.

Make sure you provide the correct name of the song as well as the artist. The search will return better items.
The results will have 4 YouTube videos and a variable number of pages of lyrics and chords from Ultimate Guitar.
Select a pair and check if they meet your expectations. If this is not the case, return to the results page and try a new pair.
When satisfactory, save the result. This result will appear in a list on the main page (index) and in this case it will not be necessary to do a new search, just click on "play".
Now just pick up your guitar and play your favorite song with your favorite artist.

In this project, in addition to using the technologies I learned during the course, I looked for others, such as beautifulsoup, the GOOGLE API.
Some challenges appeared, as I tried selenium first, but some problems led me to prefer beatifulsoup.
The software architecture was also something that made me learn more about Flask, especially when it comes to passing arguments from one route to another.
As for the design, I preferred something cleaner, using mainly Bootstrap.
I tried to avoid having too many distractions on the screen and allow the user to know exactly what to do at each step. Very complex graphic design tends to be distracting and often creates doubts about what to do and when to do it.
Furthermore, it can make the experience tedious with pages that take a long time to open or be ready for use.
Excessive dynamics on the page can confuse more than help.
Therefore, I believe that the design should be only what is necessary.
Anyway, the application is simple in its use and purpose, however, it meant an increase in knowledge for me.
BeautifulSoup was chosen to better understand how to search and process existing data on internet pages. The use of scraping in data analysis has been used for some time, but is continually developing and capable of resolving issues related to the search for qualified information in both the public and private sectors.

Learning to search for information using an API, such as GOOGLE, is also increasingly used as information spread across the internet can be gathered to meet certain interests. It is often necessary to filter them, gather them and treat them within a certain scope.

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

It is easy to create the API, but you must make sure that it is the API that allows you to retrieve data from YouTube


Need to create an .env file with the following content:
APIYT= your Google API

> [!WARNING]
> This is only for academic purposes. Is the final project for CS50x.
> You should use with discretion.
