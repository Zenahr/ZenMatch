from pythonping import ping

def is_server_alive(public_ip_address):
    """Check if a game server is still alive. If not, return False. NOTE: this method is vague since it requires the client PC to be TURNED OFF to return False. This should be called periodically to remove all serverlist entries that have been dashboarded."""
    ping(public_ip_address,  verbose=True)