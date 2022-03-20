class HTMLGenerator():
  
  @classmethod
  def build(cls, repos):
    items = ' '.join(
                    f'<strong>ID: </strong>{repo.id} <strong>Name: </strong>{repo.id} <strong>Stars: </strong>{repo.id}\n' \
                    for repo in repos
                    )
    return f'<p>{items}</p>'