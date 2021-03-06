from Perry import component, pageView, Composite, style
from Perry.Extra.bootstrap import bootstrap
from Perry.Extra.jquery import JQueryEngineStrapper
from Perry.Extra.pjec import PJECStrapper
import uvicorn

# Create our pages, we want them to inherit pageView behaviour. 
# As well as other components
Homepage = component(pageView, _Inherit = True)
About = component(pageView, _Inherit = True) 
LoginPage = component(pageView, _Inherit = True)
ourCustomStyle = style()


# Import contents for a pageView
from NexomiaApp import HomepageContents, LoginPageContents

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
    --background-light: #4c5360;
    --background-primary-alt: #404754;
    --background-primary: #373d49;
    --background-secondary-alt2: #363b47;
    --background-secondary-alt: #333844;
    --background-secondary: #2c313d;
    --accent: #7794ce;
    --accent-green: #52c96c;
    --accent-yellow: #dcdd6e;
    --accent-alt: #6d87bc;
    --accent-dark: #4e5f82;
    --text-primary: #dadfea;
    --text-secondary: #68707f;
    --text-negative: #ff3d70;
  } 
  div {
    display: block;
  }
  '''}

# Assign page contents
Homepage <= {
  'title': 'Home',
  'path':'',
  'styles': [bootstrap, ourCustomStyle, PJECStrapper],
  'DOM': pageView.DOM,
  'components': HomepageContents
}

LoginPage <= {
  'title': 'Login',
  'path':'login',
  'styles': [bootstrap, ourCustomStyle, PJECStrapper],
  'DOM': pageView.DOM,
  'components': LoginPageContents
}

About <= {
  'title': 'About',
  'path':'about',
  'DOM': Homepage
}

Pages = Composite(Homepage, About, LoginPage)

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

@app.get("/login")
def read_login():
  return Response(content=Pages.get('login').run(), media_type="text/html") 

# Uvicorn for FastAPI
# uvicorn main:app --reload --host=0.0.0.0 --port=8080