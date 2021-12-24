from Perry import component
from Perry.components import DIV

class bootstrap:
  source = "https://getbootstrap.com/"
  ctype = 'mixed'
  html = '''
<!-- CSS -->
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
  <!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
  '''

class Card(component):
  def __init__(self, *args, cid = None, cclass = None):
    self._component = component(self, Card)
    self.name = f'<BootrstrapCard cclass:{cclass} id:{hex(id(self))}>'
    self.children = args
    self.id = cid if cid is not None else ''
    self.cclass = cclass if cclass is not None else ''
    self.type = DIV
    
  def build(self, _HTML: 'Raw html of built objects' ,debug=False):
    # here we construct HTML for the component
    _HTML = ' '.join(_HTML)
    deb = f'<!-- Component: {self.name}--->' if debug else ''
    return self._component.build(
      'literal',
      f"<div style='width: 18rem;' id = '{self.id}' class = 'card, {self.cclass}'> <div class='card-body'> {_HTML} </div> </div>" + deb
    )

class CardTitle(component):
  def __init__(self, _Text: str, _Type: 'p', cid = None):
    self._component = component(self, CardTitle)
    self.name = f'<BootstrapCardTitle id:{hex(id(self))}>'
    self._text = _Text
    self.id = cid if cid is not None else ''
    self.type = _Type
    
  def build(self, debug=False):
    # here we construct HTML for the component
    deb = f'<!-- Component: {self.name}--->' if debug else ''
    return self._component.build(
      'literal',
      f"<{self.type} id = {self.id} class='card-title'> {self._text} </{self.type}>" + deb
    )

class CardText(component):
  def __init__(self, _Text: str, _Type: 'p', cid = None):
    self._component = component(self, CardText)
    self.name = f'<BootstrapCardText id:{hex(id(self))}>'
    self._text = _Text
    self.id = cid if cid is not None else ''
    self.type = _Type
    
  def build(self, debug=False):
    # here we construct HTML for the component
    deb = f'<!-- Component: {self.name}--->' if debug else ''
    return self._component.build(
      'literal',
      f"<{self.type} id = {self.id} class='card-text'> {self._text} </{self.type}>" + deb
    )