class page:
  def __init__(self):
    self._skel = "<script>{}</script>"
    self._connections = []
    
  def connector(self, _Component):
    self._connections.append(_Component)
    return _Component.build()

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


  def build(self,  _File: 'Put your js file here', *args):
    c = '\n'.join(args)
    print('Components:\n', c)
    return self.page.build(c)
    

class endComponent:
  def __init__(self, _Skeleton, *args):
    self.skel = _Skeleton
    self.args = args
  def build(self):
    return self.skel.format(*self.args)
    
    
class console:
  def log(_Text):
    return endComponent("console.log('{}')", _Text)