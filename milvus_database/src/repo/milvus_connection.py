from pymilvus import connections

class MilvusDBConnection(object):

    def __init__(self, alias="default"):
        host = "localhost"
        port = 19530

        self.alias = alias
        self.host = host
        self.port = port
        self.connection = None
    
    def _build(self):
        self.connection = connections.connect(
            alias = self.alias,
            host = self.host,
            port = self.port
        )
    
    def get_connection(self):
        if self.connection is None:
            raise RuntimeError("Start the database connection!")
        return self.connection
    
    def start(self):
        self._build()
    
    def stop(self):
        if self.connection is not None:
            self.connection.disconnect()
