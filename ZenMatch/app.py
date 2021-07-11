from flask import Flask, Response, jsonify, request, redirect, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass # https://stackoverflow.com/a/57732785/12675239
import apis

app = Flask(__name__)

# Modules/Blueprints
dev = Blueprint('dev', __name__)

app.register_blueprint(dev)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['JSON_SORT_KEYS']                 = False
app.config['DEBUG']                          = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['FLASK_ENV']                      = 'development'

db = SQLAlchemy(app)

@dataclass
class Server(db.Model): 
    id              : int
    name            : str
    active_players  : int
    max_players     : int
    region          : str
    public_ip       : str
    description     : str

    id             = db.Column(db.Integer, primary_key=True)
    name           = db.Column(db.String(60)) # TODO: replace length with config var
    active_players = db.Column(db.Integer)
    max_players    = db.Column(db.Integer)
    region         = db.Column(db.String(60))
    public_ip      = db.Column(db.String(45))
    description    = db.Column(db.String(200)) # TODO: replace length with config var
    # self.is_full

@app.route('/list', methods=['GET'])
def list_all_servers():
    """list all servers
    """
    return jsonify(Server.query.all())

@app.route('/add', methods=['GET'])
def add_new_server():
    name           = request.args.get('name')
    active_players = request.args.get('active_players')
    max_players    = request.args.get('max_players')
    region         = request.args.get('region')
    public_ip      = request.args.get('public_ip')
    description    = request.args.get('description')
    new_server     = Server(
                            name           = name          ,
                            active_players = active_players,
                            max_players    = max_players   ,
                            region         = region        ,
                            public_ip      = public_ip     ,
                            description    = description   
                            )
    db.session.add(new_server)
    db.session.commit()
    return jsonify({'message': 'Server has been added to the list.'})

@app.route('/remove', methods=['DELETE']) # TODO: make sure to use UUID to ensure only the owner can remove servers.
def remove_server():
    Server.query.filter_by(id=request.args.get('id')).delete()
    db.session.commit()
    return redirect(url_for('list_all_servers'))


@dev.route('/public_ip')
def get_public_ip():
    return apis.get_public_ip()

if __name__ == '__main__':
    app.run()