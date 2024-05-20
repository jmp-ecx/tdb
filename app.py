import sys
import os

import tdb
import tdb.tui as tui
import tdb.spec as spec

# TODO - this should be stored externally in a config file (lmao)
DEFAULT_CONFIG_LOC = './config/default-config.json'

def exit_application(status:int=0) -> None:
  sys.exit(status)

def new_project() -> tdb.Project:
  default = spec.load(DEFAULT_CONFIG_LOC)
  default['project-name'] = tui.get_str('Project Name')
  default['project-directory'] = os.getcwd()

  os.mkdir(f'{os.getcwd()}\\.tdb')
  spec.save(f'{os.getcwd()}\\.tdb\\tags.json', {})

  res = tdb.Project(default)
  return res

START_PROMPT = \
  'What action would you like to do?\n' + \
  ' 1. Create new project\n'            + \
  ' 2. Load existing project\n'         + \
  ' 3. Quit application\n'

start_input = 0
while True:
  start_input = tui.get_int(START_PROMPT)
  if start_input in [1, 2, 3]: break

proj = None
if start_input == 1:
  proj = new_project()
  proj.save()
elif start_input == 2:
  pass
else:
  exit_application()

# TODO - search for images with tags
ACTION_PROMPT = \
  'What would you like to do?\n' + \
  ' 1. Create new tag\n'         + \
  ' 2. Add tag to image\n'       + \
  ' 3. Quit application\n'

while True:
  uin = 0
  while True:
    uin = tui.get_int(ACTION_PROMPT)
    if uin in [1, 2, 3]: break

  if uin == 1:
    pass
  elif uin == 2:
    pass
  else:
    proj.save()
    exit_application()
