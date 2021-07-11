from flask import Flask, Response, jsonify

app = Flask(__name__)

class Server():
    def __init__(self, id=1, name='my server', active_players=0, max_players=4, region='EU', public_ip='153.97.25.107', description=None): # TODO: remove defaults.
        self.id             = id
        self.name           = name
        self.active_players = active_players
        self.max_players    = max_players
        self.region         = region
        self.public_ip      = public_ip
        self.description    = description
        # self.is_full

    def serialize(self):
        return dict(
        id             = self.id,
        name           = self.name,
        active_players = self.active_players,
        max_players    = self.max_players,
        region         = self.region,
        public_ip      = self.public_ip,
        description    = self.description
        )

example_server1 = Server(1, 'example server 1', 2, 8, 'EU', '153.97.25.107').serialize()
example_server2 = Server(2, 'example server 2', 4, 8, 'EU', '153.97.25.107').serialize()
example_server3 = Server(3, 'example server 3', 8, 8, 'EU', '153.97.25.107').serialize()

servers = [
    example_server1,
    example_server2,
    example_server3,
]

@app.route('/list', methods=['GET'])
def list_all_servers():
    """list all servers
    """
    return jsonify(servers)

@app.route('/add', methods=['GET'])
def add_new_server():
    new_server_id = servers[-1]['id']+1
    new_server = Server(new_server_id).serialize()
    servers.append(new_server)
    return jsonify({'message': 'Server has been added to the list.'})


if __name__ == '__main__':
    app.run()