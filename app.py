from tdb.expr.repl import REPL
import tdb.spec as spec
import tdb

# TODO - install script, which gets this all downloaded into the ProgramFiles directory

# Testing configuration
conf = spec.load('./config/.tdb/conf.json')

def main() -> None:
  proj = tdb.Project(conf)
  for t in proj.tags:
    t.print()

if __name__ == '__main__':
    main()
