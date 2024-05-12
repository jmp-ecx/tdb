import tdb.spec
import tdb.image as img
import os

class Project:
  def __init__(self, conf: dict) -> None:
    self.cwd          = conf['project_directory']
    self.ignore_dirs  = conf['ignores']['ignore_dirs']
    self.ignore_files = conf['ignores']['ignore_files']
    self.filetypes    = conf['filetypes']

    self.project_files: list[img.Image] = []

    self.__parse_dir(self.cwd)

  def __parse_dir(self, _dir: str) -> None:
    for itm in os.listdir(_dir):
      i = os.path.join(_dir, itm)
      if os.path.isfile(i):
        if itm.split('.')[-1:][0] in self.filetypes:
          self.project_files.append(img.Image(i))
      elif os.path.isdir(i):
        self.__parse_dir(i)

  def set_path(self, path: str) -> None:
    """Sets the root directory of the tdb.

    :param path: The new path of the tdb
    :return:
    """
    self.cwd = path

  def cfg(self) -> dict:
    """Returns the configuration of the current tdb

    :return: Returns a python dict containing the tdb config.
    """
    return {
      'project_directory': self.cwd,
      'filetypes'        : self.filetypes,
      'ignores':           {
        'ignore_dirs':  self.ignore_dirs,
        'ignore_files': self.ignore_files,
      },
    }

  def save(self) -> bool:
    """Saves the tdb configuration.

    :return: The status of the operation (True if success, else False)
    """
    if not os.path.isdir(f'{self.cwd}/.tdb'):
      os.mkdir(f'{self.cwd}/.tdb')

    try:
      # TODO - make .tbd directory
      spec.save(f'{self.cwd}/.tdb/conf.json', self.cfg())
    except Exception as e:
      print(e)
      return False

    return True

  def __repr__(self) -> str:
    return f'tbd :: {self.cwd}'
