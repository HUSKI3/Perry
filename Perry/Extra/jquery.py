# A simple JQuery processor
# To be added to the start of a component tuple
from Perry import component

class JQueryEngine(component):
  def __init__(self, _DOM: 'PageView DOM', cid=None):
    self._component = component(self, JQueryEngine)
    self.name = f'<JQueryEngine id:{hex(id(self))}>'
    self.id = cid if cid is not None else ''
    self.dom = _DOM
    self.type = JQueryEngine

  def __le__(self, _JQ: 'Pure JQuery code'):
    self.code = _JQ
    
  def build(self, debug=False):
    # here we construct HTML for the component
    deb = f'<!-- Component: {self.name}--->' if debug else ''
    return self._component.build(
      'literal',
      f"<script id = {self.id}> {self.code} </script>" + deb
    )

class JQueryEngineStrapper:
  source = "https://getbootstrap.com/"
  ctype = 'mixed'
  html = '''
  <!-- Minified JQuery bundle -->
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
  '''
