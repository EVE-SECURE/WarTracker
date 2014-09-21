from flask import Flask, render_template, redirect, url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
import eveapi

# flask
app = Flask(__name__)
app.config.from_pyfile('config.cfg')

# flask-sqlalchemy
from shared import db
from models improt *
db.app = app
db.init_app(app)

# eveapi
api = eveapi.EVEAPIConnection()

@app.route('/')
def index():
    return 'Index page'

@app.route('kill/<id>/battle')
def battle(id):
    return 'Battle report for kill #{}'.format(id)

@app.route('kill/<id>')
def kill(id):
    return 'Kill page for kill #{}'.format(id)

@app.route('pilot/<name>')
def pilot(id):
    return 'Pilot page for pilot named {}'.format(name)

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
