from Perry import component

class page:
  def __init__(self):
    self._skel = "<script>{}</script>"
    self._connections = []
    
  def connector(self, _Name, _Component):
    self._connections.append(_Component)
    return _Component.build(_Name)

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
  def __init__(self, _Skeleton, *args):
    self.skel = _Skeleton
    self.args = args
  def build(self, _Name):
    innard = self.skel.format(*self.args).replace('\n',' ')
    return f"function {_Name}(){{{innard}}}"
    
    
class console:
  def log(_Text):
    return endComponent("console.log('{}')", _Text)

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