from Perry.Extra.pjec import endComponent

post_code = '''
var url = "{}";

var xhr = new XMLHttpRequest();
xhr.open("POST", url);

xhr.setRequestHeader("Accept", "application/json");
xhr.setRequestHeader("Content-Type", "application/json");

{}

var data = `{}`;

xhr.send(data);
'''

class request:
  def __init__(self):
    pass
  def post(self, _Url: 'URL of the server', _Data: 'A Dict or JSON string of data'):
    return endComponent(post_code.format(_Url,'''xhr.onreadystatechange = function () {
   if (xhr.readyState === 4) {
      console.log(xhr.responseText);
   }};''', str(_Data)))