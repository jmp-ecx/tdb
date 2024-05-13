from __future__ import annotations
from tdb.tui import TUI
import tdb.expr as expr

class REPL:
  def __init__(self) -> None:
    self.current_scope = ''

    self.tokenizer = expr.Tokenizer()
    self.parser    = expr.Parser()

  def read_line(self) -> None:
    line = TUI.get_str(self.current_scope)
    toks = self.tokenizer.tokenize(line)

    # Todo - parse

  def evaluate(self) -> None:
    pass
