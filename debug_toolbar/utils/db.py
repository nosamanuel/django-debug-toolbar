try:
    from django.db import connections
except ImportError:
    # Wrap the default DB connection for pre-1.2 releases
    from django.db import connection
    class ConnectionWrapper(object):
        _connections = {'default': connection}
    connections = ConnectionWrapper()
