class User():
  
  def __init__(self, username, email):
    self._username = username
    self._email = email
    
  @staticmethod
  def members():
    return ['user 1', 'user 2', 'user 3']