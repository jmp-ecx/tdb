from __future__ import annotations
from enum import Enum, auto

"""
Examples:

project new tdb-test-project
project load D:\\images\\tdb-project

# -img  = image project 
# -code = code project
project new tdb-ex -img -code

file add ideas\\list.txt
# the -- indicates a list parameter
# --p = parents
tag new Idea --p Project Planning
"""

class TkType(Enum):
  """Different types of token."""
  none = auto()

  project = auto()
  file    = auto()
  tag     = auto()

  list_arg = auto() # --<Something> <arg> ...
  solo_arg = auto() # -<Something>

  add  = auto()
  new  = auto()
  load = auto()

  num  = auto()
  iden = auto()

  eof = auto()

class Tokenizer:
  def __init__(self) -> None:
    self.idx = 0

  def tokenize(self, expr: str):
    tokens = []
    s = ''

    while self.idx < len(expr):
      c = expr[self.idx]

      if c in '1234567890':
        tokens.append(self.__gen_number(expr))
      if c == '-':
        self.__gen_tag(expr)

      self.idx += 1

  def __gen_tag(self, expr: str):
    s_idx = self.idx
    solo = True
    c = ''
    self.idx += 1

    tag = ''

    if expr[self.idx] == '-':
      solo = False
      self.idx += 1

    while c not in ' \t\n':
      c = expr[self.idx]
      tag += c

    return {
      'type' : TkType.solo_arg if solo else TkType.list_arg,
      'idx'  : s_idx,
      'value': tag,
    }

  def __gen_number(self, expr: str) -> dict:
    s_idx = self.idx
    c = expr[self.idx]
    dot = 0

    n_str = c

    while c in '12347890.':
      c = expr[self.idx]

      if c == '.':
        dot += 1
        if dot > 1:
          break
      n_str += c
      self.idx += 1

    return {
      'type' : TkType.num,
      'idx'  : s_idx,
      'value': float(n_str) if dot else int(n_str),
    }

class Parser:
  pass
