class Thing(object):
  def __init__(self, **kwargs):
    super(Thing, self).__init__()

    self.name = 'thing'
    self.description = 'a thing'

    if kwargs:
      for key, value in kwargs.items():
        setattr(self, key, value)

  def printProperties(self):
    print('{} properties:'.format(self))
    for attr in dir(self):
      if not str(attr).startswith('__'):
        if 'method' not in str(getattr(self, attr)):
          print('  {} = {}'.format(attr, getattr(self, attr)))
