import random

class page:
  def __init__(self):
    self._skel = "<script>{}</script>"
    self._connections = []
    self.variables = ['p']
    self.window = Window(self)
    
  def connector(self, _Name, _Component):
    if type(_Component) == Events:
      c = []
      for i, event in enumerate(_Component.events):
        if event is not None:
          print(event.skel)
          self._connections.append(event)
          c.append( event.build('global', format=True) )
        else:
          print(f'[WARNING] Event at pos {i} is currently None, ignore?\n(This can happen when handling variable creation incorrectly, be ware!)')
          input()
      return "function {}() {{{}}}".format(_Name, '\n'.join(c))
    else:
      self._connections.append(_Component)
      return _Component.build(_Name)

  def gen_variable_name(self):
    s = 'p'
    while s in self.variables:
      l = []
      [ l.append(chr(random.randint(97, 97 + 26 - 1))) for x in range(0,10) ]
      s = ''.join(l)
    else:
      self.variables.append(s)
    return s

  def build(self, _ComponentsSource):
    return self._skel.format(_ComponentsSource)
  
class PjEngine:
  def __init__(self):
    self.components = {}
    self.page = page()
    
  def function(self, _Function):
    self.components[_Function.__name__] = _Function
    
    def wrapped(*args):
      return _Function( self.page, *args)
    
    return wrapped


  def build(self, *args: "Your JS functions"):
    c = '\n'.join(args)
    print('Components:\n', c)
    return self.page.build(c)
    

class endComponent:
  def __init__(self, _Skeleton, *args, format=True, _StringPa=True):
    self.skel = _Skeleton
    self.args = []
    for arg in args:

      print(arg,'<>',type(arg))
      if type(arg) == endComponent:
        # Yes very big brain implementation ik ik tyty
        self.args.append(arg.build('global')[:-2])
      else:
        if type(arg) == str:
          if _StringPa:
            self.args.append('"'+arg+'"')
          else:
            self.args.append(arg)
    self.format = format
    print('===========>', self.args)
  def build(self, _Name, format=True, special=False): # Special is dangerous!
    if _Name == 'global' and format:
      try:
        innard = self.skel.format(*self.args).replace('\n',' ')
      except:
        innard = self.skel.replace('\n',' ')
      print('======[]===>',innard)
      return f"{innard}\n"
    elif _Name == 'global' and special == True:
      return self.skel.format(*self.args)
    elif _Name == 'global':
      return self.skel
    elif format:
      innard = self.skel.format(*self.args).replace('\n',' ')
      return f"function {_Name}(){{{innard}}}\n"
    else:
      return self.skel

class Element:
  _skel_set = 'var {variable} = document.getElementById("{id}");\n{variable}.textContent = {value};'
  _skel_get = 'document.getElementById("{id}").value;'
  
  def __init__(self, _Page, _ID):
    self.id = _ID
    self.page = _Page
    self.value = self.get()
    
  def set(self, _Value: "Value to set the element to"):
    if type(_Value) != str:
      _Value = _Value.build('global')
    else:
      _Value = '"'+_Value+'"'
    return endComponent(Element._skel_set.format(variable=self.page.gen_variable_name(), 
                                id=self.id, 
                                value=_Value
                                ),
                       format = False
                       )
  def get(self):
    return endComponent(Element._skel_get.format(
                                id=self.id
                                ),
                       format = False
                       )

# Wrappers
class Events:
  def __init__(self, *_Components: "A tuple or list of components that will be fed to the constructor.\nORDER IS IMPORTANT!", debug=False):
    self.debug  = debug
    if debug:
      self.events = []
      for x in _Components:
        self.events.append(x)
        self.events.append(console.log(str( x.skel )))
    else:
      self.events = _Components

class setVar:
  def __init__(self):
    pass
  def __le__(self, *args):
    args = list(args[0])
    if type(args[1]) is not str:
      args[1] = args[1].build('global')
    return endComponent(f"{args[0]} = {args[1]}", format=False, _StringPa=False)
    input()

class Window:
  def __init__(self, _Page):
    self.page = _Page
    self.set_var = setVar()

  def get_var(self, _Name:'Name of the variable'):
    # [TODO] Stupid fix for now, fix the string formatting here for variables? But I don't think anyone in their right mind would use "" in a variable
    return endComponent(
      "{};", 
      _Name,
      _StringPa=False
    )
    
  def get(self, _ElementID: "ID of the element you want to edit"):
    return Element(self.page,_ElementID)

  def alert(self, _Message: "Message to show in the alert"):
    return endComponent("alert({});", _Message)
    
  def set_cookie(self, _Name: 'Name of the variable', _Content:'Contents of the variable'):
    return endComponent(
      "document.cookie = '{}='+{};", 
      _Name,
      _Content,
      _StringPa=False
    )
  
class console:
  def log(*_Text):
    return endComponent("console.log({});", *_Text)


from Perry import component
class PjecLoader(component):
  def __init__(self, _Engine, *_Functions: 'Your JS functions'):
    self._component = component(self, PjecLoader)
    self.name = f'<PJEC id:{hex(id(self))}>'
    self.funcs = _Engine.build( *_Functions )
    self.type = PjecLoader
    
  def build(self, debug=False):
    # here we construct HTML for the component
    deb = f'<!-- Component: {self.name}--->' if debug else ''
    return self._component.build(
      'literal',
      f"{self.funcs} </script>" + deb
    )