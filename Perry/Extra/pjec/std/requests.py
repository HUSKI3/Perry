from Perry.Extra.pjec import endComponent

post_code = '''
var url = "{url}";

var xhr = new XMLHttpRequest();
xhr.open("POST", url);

xhr.setRequestHeader("Accept", "application/json");
xhr.setRequestHeader("Content-Type", "application/json");

'''

class Then:
  def __init__(self, _Component, data='console.log("No data?");'):
    self.head = _Component
    self.data = data
    
  def then(self, *_Events):
    built = []
    for event in _Events:
      built.append((event.build('global')))
    return endComponent(self.head.format(extra='''xhr.onreadystatechange = function () {{
   if (xhr.readyState === 4) {{
      console.log(xhr.responseText);
      response = xhr.responseText;
      {}
    }}}};
var data = {data};
console.log(data);

xhr.send(JSON.stringify(data));'''.format(' '.join(built),data=self.data), ))
    

class request:
  def __init__(self):
    pass
  def post(self, _Url: 'URL of the server', _Data: 'A Dict or JSON string of data', _varName='response'):
    return Then(
      str(
        post_code.format(url=_Url)+'\n{extra}'
      ),
      data=str(_Data).replace("'",'"')
  )