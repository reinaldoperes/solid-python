from models.developer import Developer


class Member(Developer):
  
  def __init__(self, username, email):
    super().__init__(username, email)
    
  @staticmethod
  def members():
    return ['user 1', 'user 2', 'user 3']
  
  def work(self):
    return 'Coding ....'