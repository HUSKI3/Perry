from Perry import component, pageView, styleGlobal, styles, serve, Composite
from Perry.components import Label

# Create our pages, we want them to inherit pageView behaviour
Homepage = component(pageView, _Inherit = True)
About = component(pageView, _Inherit = True) 

# Create page contens
HomepageContents = (
  # Our first hello world!
  Label('Hello World!', 'h1'),
  # Then we can place some other stuff
  Label('Bye!', 'p')
)

# Assign page contents
Homepage <= {
  'title': 'Home',
  'path':'',
  'style': styleGlobal(
    styles.all['basic']
  ),
  'DOM': pageView.DOM,
  'components': HomepageContents
}
About <= {
  'title': 'About',
  'path':'about',
  'style': styleGlobal(
    styles.all['basic']
  ),
  'DOM': Homepage
}

# Serve our pages as a composite collection
serve <= Composite(Homepage, About)