from flask import Flask, Response, jsonify, request, redirect, url_for
from model import servers, remove_server_by_id

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"


@app.route('/list', methods=['GET'])
def list_all_servers():
    """list all servers
    """
    return jsonify(servers)

@app.route('/add', methods=['GET'])
def add_new_server():
    new_server_id  = servers[-1]['id']+1
    name           = request.args.get('name')
    active_players = request.args.get('active_players')
    max_players    = request.args.get('max_players')
    region         = request.args.get('region')
    public_ip      = request.args.get('public_ip')
    description    = request.args.get('description')
    new_server     = Server(new_server_id, name, active_players, max_players, region, public_ip, description).serialize()
    servers.append(new_server)
    return jsonify({'message': 'Server has been added to the list.'})

@app.route('/remove', methods=['DELETE']) # TODO: make sure to use UUID to ensure only the owner can remove servers.
def remove_server():
    remove_server_by_id(request.args.get('id'))
    return redirect(url_for('list_all_servers'))
        

if __name__ == '__main__':
    app.run()