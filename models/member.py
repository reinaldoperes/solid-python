from models.user import User


class Member(User):
  
  def __init__(self, username, email):
    super().__init__(username, email)
    
  @staticmethod
  def members():
    return ['user 1', 'user 2', 'user 3']