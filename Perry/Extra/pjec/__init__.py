import random

class page:
  def __init__(self):
    self._skel = "<script>{}</script>"
    self._connections = []
    self.variables = ['p']
    self.window = Window(self)
    
  def connector(self, _Name, _Component):
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
  def __init__(self, _Skeleton, *args, format=True):
    self.skel = _Skeleton
    self.args = args
    self.format = format
  def build(self, _Name):
    if _Name == 'global' and format:
      innard = self.skel.format(*self.args).replace('\n',' ')
      return f"{innard}\n"
    elif _Name == 'global':
      return self.skel
    elif format:
      innard = self.skel.format(*self.args).replace('\n',' ')
      return f"function {_Name}(){{{innard}}}\n"
    else:
      return self.skel

class Element:
  _skel = 'var {variable} = document.getElementById("{id}");\n{variable}.textContent = "{value}";'
  
  def __init__(self, _Page, _ID):
    self.id = _ID
    self.page = _Page
    
  def set(self, _Value: "Value to set the element to"):
    return endComponent(Element._skel.format(variable=self.page.gen_variable_name(), 
                                id=self.id, 
                                value=_Value
                                ),
                       format = False
                       )

class Window:
  def __init__(self, _Page):
    self.page = _Page
  def get(self, _ElementID: "ID of the element you want to edit"):
    return Element(self.page,_ElementID)
    
class console:
  def log(_Text):
    return endComponent("console.log('{}')", _Text)