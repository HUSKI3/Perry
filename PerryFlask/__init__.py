from flask import Flask, render_template
app = Flask(__name__)

def ext_serve(port, debug, host, pages):
  
  routes = [ ['/'+page['path'], page['func']] for page in pages]
  
  for route, func in routes:
    print('[Flask] Mapped route',route,'with',func)
    view_func = app.route(route)(func)
  
  app.run(debug=debug, port=port, host=host)


class _Serve:
  def __le__(self, _Pages: 'Composite class of pages', debug=False, port=8080, host='0.0.0.0'):
    ext_serve(debug=debug, port=port, host=host, pages=_Pages.pages)

serve = _Serve()