#!/usr/bin/env python3


from types import SimpleNamespace
from pprint import pprint
import inspect
from time import sleep
import yaml
import glob
from threading import Thread
import pickle
import os
import sys
import argparse
import importlib



core_class_modules = [ core_class_module for core_class_module in glob.glob('modules/core/class/*') ]
for core_class_module in core_class_modules:
  module = importlib.import_module(core_class_module)

  globals().update(
  {n: getattr(module, n) for n in module.__all__} if hasattr(module, '__all__')
  else
  {k: v for (k, v) in module.__dict__.items() if not k.startswith('_')}
  )

print(globals())


class Meta(type):
  #def __new__(mcs, name, bases, namespace, **kwargs):
  #  new_cls = super(Meta, mcs
  def __call__(self, *args, **kwargs):
    obj = super(Meta, self).__call__(*args, **kwargs)
    argspec = inspect.getargspec(obj.__init__)
    defaults = dict(zip(argspec.args[-len(argspec.defaults):], argspec.defaults))
    defaults.update(kwargs)
    for key, value in defaults.items():
      setattr(obj, key, value)
    return obj


'''
# Every in-game (non-meta) 'thing' is a thing
class Thing(object):
  def __init__(self, **kwargs):
    super(Thing, self).__init__()

    #if 'name' in kwargs:
    #  self.name = name
    #else:
    #  self.name = self.__class__.__name__.lower()

    self.name = 'thing'

    #for key, value in kwargs:
    #  setattr(self, key, value)
    #if kwargs:
    #  self.update(kwargs)
    if kwargs:
      for key, value in kwargs.items():
        setattr(self, key, value)

  def setOverrides(self, kwargs=None):
    if kwargs:
      for key, value in kwargs.items():
        setattr(self, key, value)

  def printProperties(self):
    print('{} properties:'.format(self))
    for attr in dir(self):
      if not str(attr).startswith('__'):
        if 'method' not in str(getattr(self, attr)):
          print('  {} = {}'.format(attr, getattr(self, attr)))
'''

# Living things are Actors
class Actor(Thing):
  def __init__(self, **kwargs):
    super(Actor, self).__init__()

    self.vitality = 1
    self.hp_current = self.hp_maximum
    self.species = 'unknown'

    if kwargs:
      for key, value in kwargs.items():
        setattr(self, key, value)
    
    self.hp_current = self.hp_maximum

  @property
  def hp_maximum(self):
    return self.vitality

  #@property
  #def hp(self):
  #  hp = SimpleNamespace()
  #  hp.current = self.hp_current
  #  hp.maximum = self.hp_maximum
  #  return hp

class Human(Actor):
  def __init__(self, **kwargs):
    super(Human, self).__init__()

    self.name = 'human'
    self.vitality = 10
    self.species = 'homo sapien'

    #self.setOverrides(kwargs)
    #if kwargs:
    #  self.update(kwargs)
    if kwargs:
      for key, value in kwargs.items():
        setattr(self, key, value)

    self.hp_current = self.hp_maximum

  

class Snake(Actor):
  def __init__(self, **kwargs):
    super(Snake, self).__init__()

    self.name = 'snake'
    self.species = 'snake'

    #for key, value in kwargs.items():
    #  setattr(self, key, value)
    #if kwargs:
    #self.setOverrides(kwargs)
    #if kwargs:
    #  self.update(kwargs)
    if kwargs:
      for key, value in kwargs.items():
        setattr(self, key, value)
      
    self.hp_current = self.hp_maximum


class Anaconda(Snake):
  def __init__(self, **kwargs):
    super(Anaconda, self).__init__()

    self.name = 'anaconda'
    self.vitality = 2

    if kwargs:
      for key, vaue in kwargs.items():
        setattr(self, key, value)
    
    self.hp_current = self.hp_maximum


class Bear(Actor):
  def __init__(self, **kwargs):
    super(Bear, self).__init__()

    self.name = 'bear'
    self.vitality = 15
    self.species = 'bear'

    if kwargs:
      for key, value in kwargs.items():
        setattr(self, key, value)

    self.hp_current = self.hp_maximum


def runScenario():

  global entities
  #entities = []


  # A human
  print('A human:')
  test_human = Human()
  test_human.printProperties()
  entities.append(test_human)

  # A human named 'Jim'
  print('A human named Jim:')
  test_human_jim = Human(name='jim')
  test_human_jim.printProperties()
  entities.append(test_human_jim)

  # A snake
  print('A snake:')
  test_snake = Snake()
  test_snake.printProperties()
  entities.append(test_snake)

  # An anaconda
  print('An anaconda:')
  test_anaconda = Anaconda()
  test_anaconda.printProperties()
  entities.append(test_anaconda)

  # A bear
  print('A bear:')
  #test_bear = Actor(name='bear')
  test_bear = Bear()
  test_bear.printProperties()
  entities.append(test_bear)

  
  while True:

    '''
    modules = [ module for modules in glob.glob('modules/*.yaml') ]
    for module in modules:
      with open(module, 'r') as f:
        module = yaml.safe_load(f)
        f.close()
        
        for key, value in module.items():
    '''

    #class_modules = [ module for modules in glob.glob('modules/*.py') ]
    #  importlib.reload(

    #for class_module in class_modules:
    #  with open(
          

    for entity in entities:
      print(entity.name)

    sleep(5)


def reloadScripts(delay):
  while True:
    print('Waiting for delay timer')
    sleep(delay)

    print('pickling objects')
    with open ('data.pkl', 'wb') as f:
      pickle.dump(entities, f, pickle.HIGHEST_PROTOCOL)

    print('waiting 3 seconds before restarting script...')
    sleep(3)

    print('restarting script')
    args = sys.argv
    sys.argv.append('--reload')
    os.execv(__file__, sys.argv)    
  
def printProperties(obj):
  for attr in dir(obj):
  #for attr in obj.__dict__:
    if not '__' in str(attr):
      pprint("obj.%s = %r" % (attr, getattr(obj, attr)))


#def printAttributes(item):
#  for attr in 
  


if __name__ == '__main__':


  core_class_modules = [ module for modules in glob.glob('modules/core/class/*.py') ]
  for core_class_module in core_class_modules:
    module = importlib.import_module('modules/core/classes/{}'.format(core_class_module))

    globals().update(
    {n: getattr(module, n) for n in module.__all__} if hasattr(module, '__all__') 
    else 
    {k: v for (k, v) in module.__dict__.items() if not k.startswith('_')}
    )   

  print(globals())
  

  parser = argparse.ArgumentParser(prefix_chars='-/--')
  parser.add_argument('--reload', action='store_true')

  global entities
  entities = []

  args = parser.parse_args()
  if args.reload:
    print('script has been reloaded')
    print('Reloading previous objects into memory')
    with open('data.pkl', 'rb') as saved_data:
      entities = pickle.load(saved_data)

  scenario_thread = Thread(target = reloadScripts, args = (10,))
  scenario_thread.start()
  runScenario()

  #example_thing = Thing()
  #example_actor = Actor()

  #print('Example thing: {}'.format(example_thing.__class__.__name__))
  #printProperties(example_thing)
  #print('Example actor: {}'.format(example_actor))
  #printProperties(example_actor)

