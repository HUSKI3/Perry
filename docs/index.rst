Perry
=====

   Perry <= A framework that let’s you compose websites in Python with
   ease!

Perry works similar to Qt and Flutter, allowing you to create component
collections. Say you want to create a div with some text and an image.
To do that you’d first need to create the page:

.. code:: python

   from Perry import component, pageView, serve, Composite

Let’s break it down: - Component - A given element that can be added
anywhere on the page - pageView - Creates a page with a route for us, we
can load styles, JS and other things into it by using the ‘styles’
argument - Serve - A Flask based micro-server for Perry - Composite -
The most important part! This tells our components to build themselves
recursively as well as creating the skeleton, route and debugging info.

Now let’s create the page

.. code:: python

   Homepage = component(pageView, _Inherit = True)
   # a pageView is also a component, but inherits different functionality

   # Assign page contents
   Homepage <= {
     'title': 'Home', # Title of the page 
     'path':'',       # Route on the webserver, no need to include the starting /
     'styles': [bootstrap], # Styles and other components, here we load bootstrap which is included in Extras
     'DOM': pageView.DOM,   # DOM, not yet implemented but worth using in case you want to upgrade to a newer verion of Perry later
     'components': HomepageContents # A ComponentSource with our elements
   }

This page will just show up as an error as we haven’t yet created our
component source! This can be done through importing ``ComponentSource``

.. code:: python

   HomepageContents = ComponentSource(
     DIV(
       Label('Hello World!', 'h1'),
       Card(
           Image('Image URL'),
           CardText('Sample Text which has attributes for bootstrap cards', 'p')   
       ),
       Label('Good bye!', 'h1')
     )
   )

You’ll get something like this. The trailing comment is used for
debugging

.. code:: html

   <body>
      <!-- Components -->  
      <div id="" class="">
         <h1 id=""> Hello World! </h1>
         <!-- Component: <Label id:0x7f398481c910> --> 
         <div style="width: 18rem;" id="" class="card, ">
            <div class="card-body">
               <img src="Image URL" id="style=''">
               <!-- Component: <Image id:0x7f398481c9d0> --> 
               <p id="class='card-text'"> Sample Text which has attributes for bootstrap cards </p>
               <!-- Component: <BootstrapCardText id:0x7f398481ca60> --> 
            </div>
         </div>
         <!-- Component: <BootrstrapCard cclass:None id:0x7f398481cb20> --> 
         <h1 id=""> Good bye! </h1>
         <!-- Component: <Label id:0x7f398481cbe0> --> 
      </div>
      <!-- Component: <DIV cclass:None id:0x7f398481cca0> -->  
      <p id=""> Running on Perry v0.9 with Debug Mode on! </p>
      <!-- Component: <Label id:0x7f3984885d90> -->
      <!-- End of Components -->
   </body>

Custom Element Bundles and Styling
==================================

Want to bundle together multiple elements and create a universal one?
That’s easy to do!

.. code:: python

   OurCoolNewElement = DIV(
       Label('Hello, I have custom stuff!', 'h1', id = 'CoolTitle'),
       cclass = 'NewElement'
   )
   # Let's give it some style
   ourCustomStyle = style()
   ourCustomStyle <= {
     'author':'HUSKI3',
     'source':'Local-made ;)'
     'ctype':'css',
     'css' : '''
     .NewElement {
       color: white;
       background: black;
     }
     '''}
   # And now add it to the components
   HomepageContents = ComponentSource(
     DIV(
       Label('Hello World!', 'h1'),
       OurCoolNewElement , # <--- here
       Label('Good bye!', 'h1')
     )
   )

You’ll need to load the style when defining the homepage contents!

.. code:: python

   Homepage <= {
     ...,
     'styles': [some, styles, ourCustomStyle],
     ...
   }

Adding JS Support
=================

At the moment JS doesn’t have direct support through built in
components, but you can use ``JQueryEngine`` and
``JQueryEngineStrapper`` from Extras.

.. code:: python

   # First we create the component with JQuery, give it a pageView to wrap around (WIP)
   js = JQueryEngine(pageView, cid = 'coolscript')
   # Now you load in the script, it can either be a string or a read from file
   js <= ( open('PerryApp/coolscript.js','r').read() )
   # To load it in, you need to add JQueryEngineStrapper to the styles of the page and add the js component to the components
   HomepageContents.add( js )

Serving pages with Flask
========================

In Perry you always serve pages as a Composite collection, this way they
are built and then loaded on Flask on the specified routes.

.. code:: python

   # Serve our pages as a composite collection
   serve <= Composite(Homepage, About, OtherPage, debug = True)

Serving pages with FastAPI
==========================

.. code:: python

   from fastapi import FastAPI, Response

   app = FastAPI()
   pages = Composite(Homepage, About, OtherPage, debug = True)

   # You can check all page info by printing the Composite component
   print(pages)

   # You can also get page info by querying it's route,
   # NOTE: The routes do not contain the initial '/'
   print(pages.get(''))

   @app.get("/")
   def read_root():
     return Response(content=pages.get('').run(), media_type="text/html") 
