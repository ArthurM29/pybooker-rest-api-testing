from models.BaseModel import BaseModel


class AuthenticationModel(BaseModel):
    def __init__(self,
                 username="admin",
                 password="password123"
                 ):
        self.username = username
        self.password = password
        super().__init__()
