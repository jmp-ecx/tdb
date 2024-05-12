import copy
import os

from tdb import spec
import tdb
from tdb.tui import TUI

# TODO - install script, which gets this all downloaded into the ProgramFiles directory

# Load a default configuration
DEFAULT_CONFIG = spec.load('D:/Projects/TagDB/config/default.json')

STARTUP_DIALOG = 'Do you want to load a tdb or create a new one?\n' \
                 ' 1. New Project\n' \
                 ' 2. Load Project'

def load_project() -> tdb.Project:
  path = TUI.get_str('Enter the path to the tdb directory.')
  return tdb.Project(spec.load(f'{path}/.tbd/conf.json'))

def new_project()  -> tdb.Project:
  cfg = copy.copy(DEFAULT_CONFIG)
  cfg['project_directory'] = os.getcwd()
  return tdb.Project(cfg)

def main() -> None:
  project: tdb.Project = tdb.Project(DEFAULT_CONFIG)
  while True:
    match TUI.get_int(STARTUP_DIALOG):
      case 1:
        project = new_project() # TODO
        break
      case 2:
        project = load_project() # TODO
        break
      case _:
        print('Please enter either 1 or 2.')
        continue

  project.save()

if __name__ == '__main__':
    main()
