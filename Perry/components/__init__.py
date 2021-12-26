from Perry import component

class Label(component):
  def __init__(self, _Text: str, _Type: 'p', cid = None):
    self._component = component(self, Label)
    self.name = f'<Label id:{hex(id(self))}>'
    self._text = _Text
    self.id = cid if cid is not None else ''
    self.type = _Type
    
  def build(self, debug=False):
    # here we construct HTML for the component
    deb = f'<!-- Component: {self.name}--->' if debug else ''
    return self._component.build(
      'literal',
      f"<{self.type} id='{self.id}'> {self._text} </{self.type}>" + deb
    )

class Image(component):
  def __init__(self, _SourceURI: str, cid = None, style=''):
    self._component = component(self, Image)
    self.name = f'<Image id:{hex(id(self))}>'
    self.id = cid if cid is not None else ''
    self.style = style if style is not None else ''
    self._source = _SourceURI
    self.type = Image
    
  def build(self, debug=False):
    # here we construct HTML for the component
    deb = f'<!-- Component: {self.name}--->' if debug else ''
    return self._component.build(
      'literal',
      f"<img src='{self._source}' id = {self.id} style='{self.style}'>" + deb
    )

class DIV(component):
  def __init__(self, *args, cid = None, cclass = None):
    self._component = component(self, DIV)
    self.name = f'<DIV cclass:{cclass} id:{hex(id(self))}>'
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
      f"<div id = '{self.id}' class = '{self.cclass}'> {_HTML} </div>" + deb
    )

class Form(component):
  def __init__(self, *args, cid = None, cclass = None):
    self._component = component(self, Form)
    self.name = f'<Form cclass:{cclass} id:{hex(id(self))}>'
    self.children = args
    self.id = cid if cid is not None else ''
    self.cclass = cclass if cclass is not None else ''
    self.type = DIV
    
  def build(self, _HTML: 'Raw html of built objects' , action='',debug=False):
    # here we construct HTML for the component
    _HTML = ' '.join(_HTML)
    deb = f'<!-- Component: {self.name}--->' if debug else ''
    return self._component.build(
      'literal',
      f"<form id = '{self.id}' class = '{self.cclass}'> {_HTML} </form>" + deb
    )

class Input(component):
  def __init__(self, _Name: str, _Type: 'text', cid = None, placeholder=''):
    self._component = component(self, Input)
    self.name = f'<Input id:{hex(id(self))}>'
    self._name = _Name
    self.id = cid if cid is not None else ''
    self.type = _Type
    self.placeholder = placeholder
    
  def build(self, debug=False):
    # here we construct HTML for the component
    deb = f'<!-- Component: {self.name}--->' if debug else ''
    return self._component.build(
      'literal',
      f"<input placeholder='{self.placeholder}' type='{self.type}' name='{self._name}' id='{self.id}'>" + deb
    )

class Button(component):
  def __init__(self, _Name: str, _Type: 'text', onClick = '' , cid = ''):
    self._component = component(self, Button)
    self.name = f'<Button id:{hex(id(self))}>'
    self._name = _Name
    self.id = cid
    self.type = _Type
    self.onClick =onClick
    
  def build(self, debug=False):
    # here we construct HTML for the component
    deb = f'<!-- Component: {self.name}--->' if debug else ''
    return self._component.build(
      'literal',
      f"<button type='{self.type}' onclick='{self.onClick}' id='{self.id}'> {self._name} </button>" + deb
    )