from __future__ import annotations

# TODO - Multi-level tag inheritance n stuff
class Tag:
  def __init__(self) -> None:
    self.name: str = ""
    self.parents: list[Tag] = []
