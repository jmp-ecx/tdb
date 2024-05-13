from __future__ import annotations
from enum import Enum, auto

"""
Examples:

project new tdb-test-project
project load D:\\images\\tdb-project

file add ideas\\list.txt
# the -- indicates a list parameter
# --p = parents
tag new Idea --p Project Planning
"""

class CmdGroup(Enum):
  none    = auto()
  project = auto()
  tag     = auto()
  file    = auto()

class CmdOp(Enum):
  none = auto()
  new  = auto()
  load = auto()

class Expression:
  def __init__(self, command: CmdGroup, op: CmdOp) -> None:
    self.cmd = command
    self.op  = op

class Parser:
  @staticmethod
  def parse(cmd: str) -> Expression:
    cmd_list = cmd.split()

    idx = 0
    kwd = cmd_list[idx]
    idx += 1

    match kwd:
      case 'project':
        op = cmd_list[idx]
        idx += 1
      case 'tag':
        op = cmd_list[idx]
        idx += 1
      case _:
        return Expression(CmdGroup.none, CmdOp.none)
