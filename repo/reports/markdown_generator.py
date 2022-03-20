class MarkdownGenerator():
  
  @classmethod
  def build(cls, repos):
    items = ' '.join(
                    f'**ID:** {repo.id} **Name:** {repo.id} **Stars:** {repo.id}\n' \
                    for repo in repos
                    )
    return f'## REPOS\n\n{items}'