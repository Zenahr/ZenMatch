from app import db, Server

example_server1 = Server(
name           = 'example server 1',
active_players = 2,
max_players    = 4,
region         = 'EU',
public_ip      = '153.97.25.107',
description    = ''
)

# db.session.add(example_server1)
# db.session.commit()

def reset_serverlist():
    db.session.query(Server).delete()
    db.session.commit()

db.create_all()

# def get_servers_count():
#     count = len(servers)
#     print(count)
#     return count

# def get_server_by_id(id):
#     for server in servers:
#         if server['id'] == id:
#             return server
#         else:
#             return None

# def get_server_index_by_id(id):
#     for server in servers:
#         if server['id'] == id:
#             return servers.index(server)

# def remove_server_by_id(id):
#     index = get_server_index_by_id(id)
#     if (index):
#         servers.pop(index)
#         return True # if True then this means the ID has been found and the entry has been removed successfully.
#     else:
#         return False