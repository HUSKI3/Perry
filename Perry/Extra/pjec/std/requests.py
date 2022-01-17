from Perry.Extra.pjec import endComponent

post_code = '''
var url = "{url}";

var xhr = new XMLHttpRequest();
xhr.open("POST", url);

xhr.setRequestHeader("Accept", "application/json");
xhr.setRequestHeader("Content-Type", "application/json");
'''

get_code = '''
var url = "{url}";

var xhr = new XMLHttpRequest();
xhr.open("GET", url, false);
'''

class Then:
  def __init__(self, _Component, data='console.log("No data?");', extra='', headers=''):
    self.head = _Component
    self.data = data
    self.extra= extra
    self.headers= headers
    
  def then(self, *_Events):
    built = []
    for event in _Events:
      built.append((event.build('global')))
    return endComponent(self.head.format(extra=self.extra.format(then=' '.join(built),data=self.data), headers=self.headers ))
    

class request:
  def __init__(self):
    pass
  def post(self, _Url: 'URL of the server', _Data: 'A Dict or JSON string of data', _varName='response', _Headers = {}):
    headers = []
    for header in _Headers:
      headers.append(f'xhr.setRequestHeader("{header}", "{_Headers[header]}");')
    return Then(
      str(
        post_code.format(url=_Url) + '\n{headers} \n{extra}'
      ),
      data=str(_Data).replace("'",'"'),
      extra = '''xhr.onreadystatechange = function () {{
   if (xhr.readyState === 4) {{
      console.log(xhr.responseText);
      response = xhr.responseText;
      {then}
    }}}};
var data = {data};
console.log(data);

xhr.send(JSON.stringify(data));''',
      headers = '\n'.join(headers)
  )
    
  def get(self, _Url: 'URL of the server', _Headers = {}):
    headers = []
    for header in _Headers:
      value = _Headers[header].raw() if type(_Headers[header]) == endComponent else '"'+str(_Headers[header])+'"'
      headers.append(f'xhr.setRequestHeader("{header}", {value});')
    return Then(
      str(
        get_code.format(url=_Url)+'\n {headers} \n{extra}'
      ),
      extra = '''   
xhr.send(null);
response = JSON.parse(xhr.responseText);
{then}''',
      headers = '\n'.join(headers)
  )