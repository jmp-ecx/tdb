from __future__ import annotations

class Tag:
  def __init__(self, name: str) -> None:
    self.name = name

    self.children: list[Tag] = []

  @staticmethod
  def gen(name: str, source: dict[str,dict]) -> Tag:
    if source.keys() == {}.keys():
      return Tag(name)

    t = Tag(name)

    for k, v in source.items():
      t.add_child(Tag.gen(k, v))

    return t

  def add_child(self, c: Tag) -> Tag:
    self.children.append(c)
    return self

  def print(self, indent:int=0) -> None:
    print(f'{' '*indent}{self.name}')
    for c in self.children:
      c.print(indent+1)

  def repr(self) -> str:
    return self.name
