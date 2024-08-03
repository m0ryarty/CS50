import os
import json
import requests
import ast

from cs50 import SQL

from bs4 import BeautifulSoup


from flask import Flask, redirect, render_template, request, session
from flask_session import Session
from flask_cors import CORS, cross_origin

from googleapiclient.discovery import build
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.debug = True
app.config['CORS_HEADERS'] = 'Content-Type'

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

youTubeApiKey = os.getenv('APIYT')

youtube = build('youtube', 'v3', developerKey=youTubeApiKey)

yt_results = []
ug_results = []

def catch_yt(song): 
    # get the video urls from youtube
    yt_results = []            
    yt_request = youtube.search().list(
        part="snippet",
        maxResults=8,
        q=song).execute()

    

    for item in yt_request['items']:
        yt_results.append({
            "id": item["id"]["videoId"],
            "title": item["snippet"]["title"],
            "thumbnail": item["snippet"]["thumbnails"]["default"]["url"]
            })
    return yt_results


def catch_ug(song):
    ug_results = []
    ug_song = song.replace(' ', '%20')
                
    ug_url = 'https://www.ultimate-guitar.com/search.php?search_type=title&value={ug_song}'.format(ug_song=ug_song)

            
    headers = {'User-Agent' : 'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; bingbot/2.0; +[4](http://www.bing.com/bingbot.htm%29) Chrome/116.0.1938.76 Safari/537.36'}

    ug_page = requests.get(ug_url, headers=headers)

                
                # get the lyrics and chords with bs4
                    

    soup = BeautifulSoup(ug_page.content, 'html.parser') 
    result = soup.find('div', class_ = "js-store")

                

    soup_json = result['data-content']
    meu_dicionario = json.loads(soup_json)
    result_url = meu_dicionario['store']['page']['data']['results']                   

    ug_results = []
    for item in result_url:
        if int(item['tab_url'].find('chord')) != -1:
            ug_results.append({
                "ug_tab": item["tab_url"],
                "ug_artist": item["artist_name"],                    
                "ug_song_name": item["song_name"],
                "ug_songId": item["id"],
            })
    return ug_results

def yt_data_choice(yt_results_obj, yt_choice):
    yt_obj = ast.literal_eval(yt_results_obj)  

    for yt_item in yt_obj:
        if yt_item['id'] == yt_choice:
            yt_data = yt_item
    return yt_data

def ug_data_choice(ug_results_obj, ug_choice):
    ug_obj = ast.literal_eval(ug_results_obj)  

    for ug_item in ug_obj:
        if ug_item['ug_tab'] == ug_choice:
            ug_data = ug_item
    return ug_data

db = SQL("sqlite:///play-along.db")

@app.route("/", methods=['GET', 'POST'])
@cross_origin()
def index():
    
    if request.method == 'POST':

        session.clear()
    # get the song to play along
        
        song = request.form.get('song')
                        
        if not song:
            return redirect('/')       
        
        session['song'] = song
        
    else:
        songs = db.execute("SELECT * FROM playalong ORDER BY artist")

        
        return render_template('index.html', songs=songs)
    
    return redirect('/results') 
    
    
    
    
@app.route("/results", methods=['GET', 'POST'])
@cross_origin()
def results():
    
    
    if request.method == 'POST':
        yt_choice = request.form.get('yt_radio')
        ug_choice = request.form.get('ug_radio')        

        if not yt_choice or not ug_choice: 
            return redirect('/results')
        
        yt_results_obj = request.form.get('yt_results_obj')     
        ug_results_obj = request.form.get('ug_results_obj')

                
        yt_data = yt_data_choice(yt_results_obj, yt_choice) 
        ug_data = ug_data_choice(ug_results_obj, ug_choice)

        
                    
        song_data = {**yt_data, **ug_data}

        

        
            
        session['yt_choice'] = yt_choice
        session['ug_choice'] = ug_choice
        session['song_data'] = song_data



        return redirect('/songs')
        
    else:
        yt_results = []
        ug_results = []
        try:
            
            q_song = session['song']
             
            if not q_song:
                
                return redirect('/')         
            
            
            
            if not yt_results:
                yt_results = catch_yt(q_song)
                

            if not ug_results:
                ug_results = catch_ug(q_song)                
                
            

            return render_template('results.html', yt_results=yt_results, ug_results=ug_results)
        except:
            return render_template('index.html')
    
        

@app.route("/songs", methods=['GET', 'POST'])
@cross_origin()
def songs():

    yt_choice = session['yt_choice']   
    ug_choice = session['ug_choice']
    song_data = session['song_data']

    

    if request.method == 'POST':

        db.execute("INSERT INTO playalong(ytId, title, tab, tabId, song, artist, thumbnail) VALUES(?, ?, ?, ?, ?, ?, ?)", song_data['id'], song_data['title'], song_data['ug_tab'], song_data['ug_songId'], song_data['ug_song_name'], song_data['ug_artist'], song_data['thumbnail'])

        
        return redirect('/')   
    
    else:
        return render_template('songs.html', ug_choice=ug_choice, yt_choice=yt_choice, song_data=song_data)
        
    
  