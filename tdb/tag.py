from __future__ import annotations

class Tag:
  """A code representation of a tag.
  The class itself is really just a wrapper for a name and children (it could be
  represented with a dict), but it also adds functionality for saving and loading
  tags.

  Once I don't have a deadline for the code, I'll look into more advanced tagging
  systems, but for now, a simple nested tag system works ok.
  """
  def __init__(self, name: str) -> None:
    self.name = name

    self.children: list[Tag] = []

  @staticmethod
  def gen(name: str, source: dict[str,dict]) -> Tag:
    """Creates a tag hierarchy from a dictionary

    :param name: The name of the tag.
    :param source: The dictionary of sub-tags. should look like **{'tag-name': {'tag-name': ...}, ...}**.
    :return: The root tag.
    """

    # If the tag doesn't have any children, just return the tag.
    if source.keys() == {}.keys():
      return Tag(name)

    # If the tag has children, create it
    t = Tag(name)
    # Then find the children and add them to the tag.
    for k, v in source.items():
      t.add_child(Tag.gen(k, v))

    return t # Return the tag.

  def add_child(self, c: Tag) -> Tag:
    """Adds a child tag to the tree

    :param c: The child tag to attach.
    :return: Self.
    """
    self.children.append(c)
    return self

  def print(self, indent:int=0) -> None:
    """Prints a string representation of the tag & sub-tags.

    :param indent: The level of indentation to print at. (Should usually be 0).
    """
    print(f'{' '*indent}{self}')
    for c in self.children:
      c.print(indent+1) # For every child tag, print with 1 level more of indent

  def __repr__(self) -> str:
    """A simple string representation of just this tag.

    :return: The name of the tag.
    """
    return self.name
