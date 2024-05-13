from tdb.expr.repl import REPL
import tdb.spec as spec
import tdb

# TODO - install script, which gets this all downloaded into the ProgramFiles directory

# Load a default configuration
DEFAULT_CONFIG = spec.load('./config/default-config.json')

def main() -> None:
  repl = REPL()
  repl.read_line()

if __name__ == '__main__':
    main()
