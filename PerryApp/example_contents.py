from Perry.components import Label, Image, DIV, Form, Input, Button
from Perry import ComponentSource, pageView
from Perry.Extra.jquery import JQueryEngine
from Perry.Extra.bootstrap import Card, CardTitle,CardText
from Perry.Extra.pjec import PjecLoader, PjEngine, console, Events
from Perry.Extra.pjec.std import random

# Let's add JQuery to our website!
js = JQueryEngine(pageView, cid = 'coolscript')
js <= (
  # It's best to load it as a file read, but for demo purposes here's a string
  open('PerryApp/coolscript.js','r').read()
)

engine = PjEngine()
@engine.function
def hello( page ):
  window = page.window
  
  events = Events(
    window.get('text').set(
      random.int(0,20)
    )
  )
  return page.connector('hello', events)

# Create page contens
HomepageContents = ComponentSource(
  ######## This is the meme maker
  DIV(
    Label('WHAT meme maker', 'h1'),
    Card(
      Image('https://tse3.mm.bing.net/th?id=OIP.f1BTli7-ohJqh0cTJLIaDwHaE8&pid=Api', 
            cid='myCoolImage',
            style='''
            max-width: 100%; 
            display: block; 
            height: auto
            '''
           ),
      CardTitle('Red Panda', 'h5', cid='CardTitle'),
      CardText("It's a red panda", 'p', cid='CardText'),
      cclass = 'mycooldiv'
    ),
    Form(
      DIV(
        Input('whatTitle','text', placeholder='Title', cid='whatTitle'),
        Input('whatText','text', placeholder='Text', cid='whatText'),
        Input('whatImage','text', placeholder='Image URL', cid='whatImage'),
        Button('Create','button', cid='button'),
        cclass = 'inputs'
      )
    )
  ),
  DIV(
    js,
    cclass = 'forjs',
    cid = 'script'
  ),
  ####### This is for PJEC testing
  Label('Random number generator!', 'h1'),
  DIV(
    Label('Random number here', 'p',cid='text'),
    Button('Next random number','button', onClick='hello()', cid='button'),
    PjecLoader(engine, hello())
  )
)
