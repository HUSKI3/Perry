from Perry import component, pageView, Composite, style
from Perry.Extra.bootstrap import bootstrap
from Perry.Extra.jquery import JQueryEngineStrapper
import uvicorn

# Create our pages, we want them to inherit pageView behaviour. 
# As well as other components
Homepage = component(pageView, _Inherit = True)
About = component(pageView, _Inherit = True) 
ourCustomStyle = style()


# Import contents for a pageView
from NexomiaApp import HomepageContents

# Custom style
ourCustomStyle <= {
  'author':'Us',
  'ctype':'css',
  'css' : '''
  * {
    text-align: center;
    margin: 0;
    font-family: "Inter",sans-serif;
    -webkit-font-smoothing: antialiased;
    box-sizing: border-box;
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

Pages = Composite(Homepage, About, debug = True)

# Multiple types of serving the pages are supported
# 
'Flask'
# from PerryFlask import serve
# Serve our pages as a composite collection
# serve <= Pages
#


'FastAPI (Single page)'
from fastapi import FastAPI, Response

app = FastAPI()
# pages = Pages

# You can check all page info by printing the Composite component
# print(pages)

# You can also get page info by querying it's route,
# NOTE: The routes do not contain the initial '/'
# print(pages.get(''))

@app.get("/")
def read_root():
  return Response(content=Pages.get('').run(), media_type="text/html") 

# Uvicorn for FastAPI
# uvicorn main:app --reload --host=0.0.0.0 --port=8080