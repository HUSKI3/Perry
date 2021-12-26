from . import Event

class onClick(Event):
  def __init__(self, _Function: 'Whatever u do here idfk'):
    self._event = Event(self, Card)
    self.name = f'<PJEC_onClick id:{hex(id(self))}>'
    self.func = _Function
    self.type = onClick
    
  def build(self,debug=False):
    # here we construct JS for the component
    deb = f'Component: {self.name}' if debug else ''
    return f"{self.func.caller}() /*{deb}*/"
