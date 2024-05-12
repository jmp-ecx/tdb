class Image:
  def __init__(self, path: str) -> None:
    self.path   = path
    self.f_type = path.split('.')[-1:][0]

  def __repr__(self) -> str:
    return f'{self.f_type} :: {self.path}'
