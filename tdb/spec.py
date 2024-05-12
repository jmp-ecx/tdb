import json

def load(path: str) -> dict:
  """Loads the given JSON config file, as a python dict.

  :param path: The path of the config file
  :return: The configuration, as a dictionary
  """
  with open(path, 'r', encoding='UTF-8') as f:
    txt = f.read()         # Read the file
    return json.loads(txt) # Convert to JSON and return TODO - error handling

def save(path: str, config: dict):
  """Saves the configuration in the file specified.

  :param path: The path of the file to save to
  :param config: The configuration to save
  :return:
  """
  with open(path, 'w', encoding='UTF-8') as f:
    f.write(json.dumps(config, indent=2)) # TODO - Error Handling

def validate(config: dict, spec: dict) -> bool:
  """Validates the configuration passed in

  It's fairly simple, so don't expect it to make sure that numbers
  are in the correct range or whatever, but it gets the job done (I hope).


  :param config: The configuration to validate
  :param spec: The specification to validate against
  :return: True if the config is valid, else False
  """

  # Make sure that the two dictionaries have the same keys.
  if config.keys() != spec.keys(): return False

  for k in spec.keys():
    # If the item is another dictionary, recurse through to validate that too
    if type(spec[k]) is dict and type(config[k]) is dict:
      res = validate(config[k], spec[k])
      if not res:
        # If they aren't the same, return false
        return False
    elif type(spec[k]) is not type(config[k]):
      # If the types of the two configs are different, return false
      return False

  # The two dictionaries are the same, so return true
  return True
