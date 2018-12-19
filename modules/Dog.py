from ../class_prototypes import Actor

class Dog(Actor):
  def __init__(self, **kwargs):
    super(Dog, self).__init__()

    self.name = 'dog'
    self.species = 'dog'

    if kwargs:
      for key, value in kwargs.items():
        setattr(self, key, value)

    self.hp_current = self.hp_maximum
