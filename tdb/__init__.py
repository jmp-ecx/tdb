import tdb.spec
import tdb.image as img
import tdb.tag as tag
import os

class Project:
  def __init__(self, conf: dict) -> None:
    self.name         = conf['project-name']
    self.cwd          = conf['project-directory']
    self.ignore_dirs  = conf['ignores']['ignore-dirs']
    self.ignore_files = conf['ignores']['ignore-files']
    self.filetypes    = conf['filetypes']

    self.project_files: list[img.Image] = []
    self.tags: list[tag.Tag] = []

    self.__parse_dir(self.cwd)
    self.__get_tags()

  def __parse_dir(self, _dir: str) -> None:
    """ Recursively iterates through all subdirectories, finding all files of the types specified.

    :param _dir: The directory to search through.
    :return:
    """

    # Iterate through teh directory
    for itm in os.listdir(_dir):
      i = os.path.join(_dir, itm) # Get the path of the item
      if os.path.isfile(i): # Check if the path is a file or folder
        if itm.split('.')[-1:][0] in self.filetypes: # If it's a file, check if it has the correct filetype.
          self.project_files.append(img.Image(i)) # If it does, add it to the list of project files.
      elif os.path.isdir(i):
        self.__parse_dir(i) # If it's a directory, recurse 1 layer deeper.

  def __get_tags(self) -> None:
    d = spec.load(f'{self.cwd}/.tdb/tags.json')
    print(d)
    for k, v in d.items():
      self.tags.append(tag.Tag.gen(k, v))

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
      'project-name'     : self.name,
      'project-directory': self.cwd,
      'filetypes'        : self.filetypes,
      'ignores':           {
        'ignore-dirs':  self.ignore_dirs,
        'ignore-files': self.ignore_files,
      },
    }

  def save(self) -> bool:
    """Saves the tdb configuration.

    :return: The status of the operation (True if success, else False)
    """
    if not os.path.isdir(f'{self.cwd}/.tdb'):
      os.mkdir(f'{self.cwd}/.tdb') # If the .tbd dir doesn't exist, make it.

    try:
      spec.save(f'{self.cwd}/.tdb/conf.json', self.cfg()) # Save the config file.
    except Exception as e:
      print(e) # If for some reason, it doesnt work, print the error and return false
      return False

    return True # If the save operation worked, return true

  def __repr__(self) -> str:
    """ Super basic repr method

    :return: The root dir of the project
    """
    return f'tbd :: {self.cwd}'
