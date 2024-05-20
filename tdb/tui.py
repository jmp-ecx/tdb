def get_int(prompt:str='') -> int:
  """Prompts the user to enter an integer.

  :param prompt: The prompt to ask (can be left empty)
  :return: The input provided
  """
  if prompt != '':
    print(prompt)
  value = input('int > ')
  try:
    return int(value)
  except TypeError as e:
    print('Input an int please!')
    return get_int(prompt)

def get_float(prompt:str='') -> float:
  """Prompts the user to enter a floating point number.

  :param prompt: The prompt to ask (can be left empty)
  :return: The input provided
  """
  if prompt != '':
    print(prompt)
  value = input('float > ')
  try:
    return float(value)
  except TypeError as e:
    print('Input a float please!')
    return get_float(prompt)

def get_str(prompt:str='', inline:bool=True) -> str:
  """Prompts the user to enter a string.

  :param prompt: The prompt to ask (can be left empty)
  :param inline: If you want the prompt to appear on the same line as the carat.
  :return: The input provided
  """
  if prompt != '':
    print(prompt, end=('' if inline else '\n'))
  return input(' > ')
