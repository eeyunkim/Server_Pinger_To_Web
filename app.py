from flask import Flask, render_template
from mcstatus import JavaServer

app = Flask(__name__)

@app.route('/')
def home():
    server = JavaServer.lookup("211.209.34.112:25565")

    try:
        status = server.status()
        online_users = status.players.online
    except Exception as e:
        online_users = None

    try:
        latency = server.ping()
    except Exception as e:
        latency = None

    try:
        query = server.query()
        online_usernames = query.players.names
    except Exception as e:
        online_usernames = None

    return render_template('index.html', online_users=online_users, latency=latency, online_usernames=online_usernames)

if __name__ == '__main__':
    app.run(debug=True)
