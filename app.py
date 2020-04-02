from flask import Flask, render_template, redirect
import requests
import os

app = Flask(__name__)

client_id = os.environ['SPOTIFY_CLIENT_ID']


@app.route("/")
@app.route("/home")
def home():
	return "<h1>Home</h1>"

@app.route("/authorize")
def authorize():
	return render_template('index.html')

@app.route("/sp_redir")
def sp_redir():

	redirect_uri = "http://localhost:5000/organize"
	scope = "user-library-read playlist-modify-public playlist-read-private playlist-modify-private"

	params = {
	"client_id" : client_id,
	"response_type" : "code",
	"redirect_uri" : redirect_uri,
	"scope": scope
	}
	return redirect(requests.get("https://accounts.spotify.com/authorize", params=params).url)

@app.route("/organize")
def organize():
	return "<h1>Organize</h1>"


# Flask automatically runs when we run this file using python
if __name__ == '__main__':
	app.run(debug=True)