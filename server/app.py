from flask import Flask, jsonify, redirect, request, session, make_response,session,redirect
from flask_cors import CORS
import requests

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# help from https://github.com/spotify/web-api-auth-examples/blob/master/authorization_code/app.js
# and https://stackoverflow.com/questions/57580411/storing-spotify-token-in-flask-session-using-spotipy

CLI_ID = '8398ae55696141a3a7f887552605af0d'
CLI_SEC = 'ca7adba9cc4d4f759eeff68538055afe'

# Make sure you add this to Redirect URIs in the setting of the application dashboard
# REDIRECT_URI = "https%3A%2F%2F127.0.0.1:5000%2Fcallback"
REDIRECT_URI = "http://127.0.0.1:5000/callback"

SCOPE = 'playlist-modify-private,playlist-modify-public,user-top-read'

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# authorization-code-flow Step 1. Have your application request authorization; 
# the user logs in and authorizes access
@app.route("/login")
def verify():
    auth_url = f'https://accounts.spotify.com/authorize?client_id={CLI_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={SCOPE}&show_dialog=true'
    print(auth_url)
    return redirect(auth_url)

# authorization-code-flow Step 2.
# Have your application request refresh and access tokens;
# Spotify returns access and refresh tokens
@app.route("/callback")
def callback():
    session.clear()
    code = request.args.get('code')

    auth_token_url = f"https://accounts.spotify.com/api/token"
    res = requests.post(auth_token_url, data={
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":REDIRECT_URI,
        "client_id":CLI_ID,
        "client_secret":CLI_SEC
        })

    res_body = res.json()
    print(res.json())
    session["toke"] = res_body.get("access_token")
    print(session["toke"])

    return redirect("/")

if __name__ == '__main__':
    app.run()