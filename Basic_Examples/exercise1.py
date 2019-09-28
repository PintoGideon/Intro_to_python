class User:
    base_url = 'http://example.com/api'

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def query(cls, query_string):
        return cls.base_url+'?'+query_string

    @staticmethod
    def name():
        return 'Kevin Bacon'

    @property
    def full_name(self):
        return f"{self.first_name}{self.last_name}"


user = User('Keith', 'Thompson')
user.base_url
print(user.full_name)
