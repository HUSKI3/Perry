from Perry.components import Label, Image, DIV, Form, Input, Button
from Perry import ComponentSource, pageView
from Extra.jquery import JQueryEngine
from Extra.bootstrap import Card, CardTitle,CardText

# Let's add JQuery to our website!
js = JQueryEngine(pageView, cid = 'coolscript')
js <= (
  # It's best to load it as a file read, but for demo purposes here's a string
  open('PerryApp/coolscript.js','r').read()
)

# Create page contens
HomepageContents = ComponentSource(
  DIV(
    Label('Hello World!', 'h1'),
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
    ),
    Label('Good bye!', 'p')
  ),
  DIV(
    js,
    cclass = 'forjs',
    cid = 'script'
  )
)
