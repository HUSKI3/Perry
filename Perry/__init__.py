##################### 
# Please dont mind this, python failed to find these due to some weird regex errors
import os, os.path

def clean(_Path: 'location to clean'):
  for root, dirs, files in os.walk(_Path):
    for file in files:
        os.remove(os.path.join(root, file))

######################

from random import randint

class component:
  def __init__(self, _Type: None, _Inherit = False) -> None:
    self.state = 0
    self.type = _Type
    
    if _Inherit == True:
      self._component = _Type.__init__(self)
      
  def __le__(self, _ComponentConfig: dict):
    self._component = _ComponentConfig
    self.name = _ComponentConfig['title']
    self.children = _ComponentConfig['components'].components if 'components' in _ComponentConfig else []
    self.path = _ComponentConfig['path'] if 'path' in _ComponentConfig else 'Invalid'
    self.style = _ComponentConfig['styles'] if 'styles' in _ComponentConfig else None

  def _proc(self):
    return self.html

  def build(self, type: None, inner: '<></>', children=[]):
    # Here we do the builing of HTML
    built = ''
    if self.type == pageView:
      # If it's a pageView we need to build the skeleton
      style = []
      if self.style is not None:
        for _ in self.style:
          # Check type of the style!
          if _.ctype == 'mixed':
            style.append(_.html)
          elif _.ctype == 'css':
            style.append(f"<style>{_.css}</style>")
          elif _.ctype == 'js':
            style.append(f"<script>{_.js}</script>")
      style ='\n'.join(style).replace('"',"'") if style is not None else ''
      children = '\n  '.join(children)
      skel = f'''
<html>
<head>
  <title>{self.name}</title>
  {style}
</head>
<body>
  <!-- Components --->
  {children}
  <!-- End of Components --->
</body>
</html>
'''
      built = skel
      self.html = built
      func = 'builder_'+str(randint(0,99999999))
      setattr(self, func, self._proc)
      return (built, func)
    else:
      if type == 'literal':
        built = inner
      else:
        print('TODO')
    self.html = built
    return built
    
      
class pageView:
  DOM = {}
  def __init__(self):
    self.children = ()
    self.html = ""

class style:
  def __init__(self):
    self.config = ''
  def __le__(self, _Config: dict):
    self.ctype = _Config['ctype']
    self.css = _Config['css'] if 'css' in _Config else ''
    self.html = _Config['html'] if 'html' in _Config else ''

class ComponentSource:
  def _build_div(self, _Source: 'a collection of children inside the div', debug=False):
    ext_ = []
    for o in _Source.children:
      print(o)
      print(f'[DIV] Constructing {o.name} of type {o.type}...')
      if o.type == components.DIV:
        _inner = self._build_div(o, debug=debug)
        chtml = o.build(_inner, debug=debug)
        ext_.append(chtml)
      else:
        ext_.append(o.build(debug))
    return ext_
    
  def __init__(self, *args):
    self.components = list(args)
    
  def add(self, _Component: 'Desired Component'):
    self.components.append(_Component)

  def raw(self, debug=False):
    componentsList = []
    for _ in self.components:
      print(f'[Builder] Constructing {_.name} of type {_.type}...')
      ext_ = []
      if _.type == components.DIV:
        ext_ = self._build_div(_, debug=debug)
        chtml = _.build(ext_, debug=debug)
      else:
        chtml = _.build(debug)
      componentsList.append(chtml)
    return '\n'.join(componentsList)

class styleGlobal:
  def __init__(self, _Style: style):
    self._ = _Style

class builtPage:
  def __init__(self, _Source: 'Page dictionary source'):
    self.name = _Source['name']
    self.path = _Source['path']
    self.func = _Source['func']
    self.src  = _Source
    
  def __repr__(self):
    return str(self.src)

  def run(self):
    '''
    Run the actual page to get the raw html
    '''
    return self.func()
    
# GH Issue #1 -  Move all the building components to Composite class and move Flask-Serve over to a seperate module 
class Composite:
  def _build_div(self, _Source: 'a collection of children inside the div', debug=False):
    ext_ = []
    for o in _Source.children:
      print(o)
      print(f'[DIV] Constructing {o.name} of type {o.type}...')
      if o.type == components.DIV:
        _inner = self._build_div(o, debug=debug)
        chtml = o.build(_inner, debug=debug)
        ext_.append(chtml)
      else:
        ext_.append(o.build(debug))
    return ext_

  def __repr__(self):
    info = ['______Pages______']
    for page in self.pages:
      info.append(f'''
Title: {page['name']}
Path:  /{page['path']}
Func:  {page['func']} (returns raw html)
            ''')
    return '\n'.join(info)

  def get(self, _Path: 'Path that the page is located on'):
    return builtPage(self._dict[_Path])
    
  def __init__(self, *args, debug=False):
    self.pages = list(args)
    self.debug = debug
    pages = []
    
    print(f'[Perry] prep to clean')
    clean('_preped')
    for component in self.pages:
      
      if component.type == pageView:        
        componentsList = []
        
        for _ in component.children:
          print(f'[Builder] Constructing {_.name} of type {_.type}...')
          ext_ = []
          if _.type == components.DIV:
            ext_ = self._build_div(_, debug=debug)
            chtml = _.build(ext_, debug=debug)
          else:
            chtml = _.build(debug)
          componentsList.append(chtml)

        if debug:
          componentsList.append(components.Label("Running on Perry v0.9 with Debug Mode on!", 'p').build(debug))
        
        print(f'[Perry] Preparing page ({component.name})...')
        a, b = component.build('pageView', '', children = componentsList)
        html = component.html.replace('\n','')
        with open('_preped/.'+b,'w+') as f:
          f.write(html)
        exec(f'''def {component.name}_func():
  return open("_preped/.{b}","r").read() ''')
        pages.append({
          'name':component.name,
          'path':component.path,
          'func':eval(f'{component.name}_func')
        })
      else:
        print(f'Unsupported type {component.type}')
    self.pages = pages
    self._dict = {}
    for page in pages:
      self._dict[page['path']] = page