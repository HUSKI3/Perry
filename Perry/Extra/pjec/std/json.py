from Perry.Extra.pjec import endComponent

class JSON:
  def parse(_Json:'Json variable to be parsed'):
    return endComponent("JSON.parse({});".format(_Json), format=False)