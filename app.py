from flask import Flask, render_template, redirect, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
import eveapi

# flask
app = Flask(__name__)
app.config.from_pyfile('config.cfg')

# flask-sqlalchemy
from shared import db
from models import *
db.app = app
db.init_app(app)

# eveapi
api = eveapi.EVEAPIConnection()

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/kill/<id>/report')
def report(id):
    return render_template('report.html', id=id)


@app.route('/kill/<id>')
def kill(id):
    return render_template('kill.html', id=id)


@app.route('/pilot/<name>')
def pilot(name):
    return render_template('pilot.html', name=name)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=1234)

# update code - needs to be converted to actual DB models instead of loose objects
# api = eveapi.EVEAPIConnection()
# auth = api.auth(keyID=3527924, vCode='S4khsQwmRRVt4MkGg3wHjQ8lxE0sjbTQaZFqeSd5qLOa4hdco7y2qQYn61Wt6Kb0')
# kills = []
# result = auth.corp.KillMails()
# for kill in result.kills:
    # k = Kill(date=kill.killTime)
    # kill.victim = Player(kill.victim.characterID, 'victim', kill.victim.characterName, kill.victim.corporationID,
        # kill.victim.corporationName, kill.victim.allianceID, kill.victim.allianceName,
        # kill.victim.damageTaken, kill.victim.shipTypeID, False)
    # attackers = []
    # for att in kill.attackers:
        # a = Player(att.characterID, 'attacker', att.characterName, att.corporationID,
            # att.corporationName, att.allianceID, att.allianceName,
            # att.damageDone, att.shipTypeID, att.finalBlow)
        # attackers.append(a)
    # k.attackers = attackers
    # kills.append(k)
