data_dev_config = [
    '0.0.0.0',
    '5432',
    'my-username',
    'my-password',
    'db_name'
]

class Config():
    def __init__(self, host, port, username, password, db_name):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.db_name = db_name

dev_config = Config(*data_dev_config)
