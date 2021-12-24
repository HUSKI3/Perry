from Perry import component, pageView, serve, Composite, style
from customComponents.bootstrap import bootstrap
from customComponents.jquery import JQueryEngineStrapper

# Create our pages, we want them to inherit pageView behaviour. 
# As well as other components
Homepage = component(pageView, _Inherit = True)
About = component(pageView, _Inherit = True) 
ourCustomStyle = style()


# Import contents for a pageView
from PerryApp import HomepageContents

# Custom style
ourCustomStyle <= {
  'author':'Us',
  'ctype':'css',
  'css' : '''
  * {
    text-align: center;
    margin: 0 auto;
  } 
  .mycooldiv {
    color: white;
    border: 10px solid black;
    padding: 15px;
    background: black;
  }
  '''}

# Assign page contents
Homepage <= {
  'title': 'Home',
  'path':'',
  'styles': [bootstrap, ourCustomStyle, JQueryEngineStrapper],
  'DOM': pageView.DOM,
  'components': HomepageContents
}

About <= {
  'title': 'About',
  'path':'about',
  'DOM': Homepage
}

# Serve our pages as a composite collection
serve <= Composite(Homepage, About, debug = True)