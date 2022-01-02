##################### 
# Please dont mind this, python failed to find these due to some weird regex errors
from flask import Flask, render_template
app = Flask(__name__)

def ext_serve(port, debug, host, pages):
  
  routes = [ ['/'+page['path'], page['func']] for page in pages]
  
  for route, func in routes:
    print('[Flask] Mapped route',route,'with',func)
    view_func = app.route(route)(func)
  
  app.run(debug=debug, port=port, host=host)

import os, re, os.path

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
    print(f'I got called! Im {self.name}!')
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

class Composite:
  def __init__(self, *args, debug=False):
    self.pages = list(args)
    self.debug = debug
  
class style:
  def __init__(self):
    self.config = ''
  def __le__(self, _Config: dict):
    self.ctype = _Config['ctype']
    self.css = _Config['css'] if 'css' in _Config else ''
    self.html = _Config['html'] if 'html' in _Config else ''

class ComponentSource:
  def __init__(self, *args):
    self.components = list(args)
    
  def add(self, _Component: 'Desired Component'):
    self.components.append(_Component)

class styleGlobal:
  def __init__(self, _Style: style):
    self._ = _Style

class _Serve:
  def _build_div(self, _Source: 'a collection of children inside the div', debug=False):
    ext_ = []
    for o in _Source.children:
      print(f'[DIV] Constructing {o.name} of type {o.type}...')
      if o.type == components.DIV:
        _inner = self._build_div(o, debug=debug)
        chtml = o.build(_inner, debug=debug)
        ext_.append(chtml)
      else:
        ext_.append(o.build(debug))
    return ext_
  
  def __le__(self, _Pages: Composite, debug=False, port=8080, host='0.0.0.0'):
    pages = []
    print(f'[Perry] prep to clean')
    clean('_preped')
    for component in _Pages.pages:
      
      if component.type == pageView:        
        componentsList = []
        
        for _ in component.children:
          print(f'[Builder] Constructing {_.name} of type {_.type}...')
          ext_ = []
          if _.type == components.DIV:
            ext_ = self._build_div(_, debug=_Pages.debug)
            chtml = _.build(ext_, debug=_Pages.debug)
          else:
            chtml = _.build(_Pages.debug)
          componentsList.append(chtml)

        if _Pages.debug:
          componentsList.append(components.Label("Running on Perry v0.9 with Debug Mode on!", 'p').build(_Pages.debug))
        
        print(f'[Perry] Preparing page ({component.name}) for flask...')
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

        
    ext_serve(debug=debug, port=port, host=host, pages=pages)

serve = _Serve()