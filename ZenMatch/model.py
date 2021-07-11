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

def get_servers_count():
    count = len(servers)
    print(count)
    return count

def get_server_by_id(id):
    for server in servers:
        if server['id'] == id:
            return server
        else:
            return None

def get_server_index_by_id(id):
    for server in servers:
        if server['id'] == id:
            return servers.index(server)

def remove_server_by_id(id):
    index = get_server_index_by_id(id)
    if (index):
        servers.pop(index)
        return True # if True then this means the ID has been found and the entry has been removed successfully.
    else:
        return False

get_servers_count()
remove_server_by_id(2)
get_servers_count()