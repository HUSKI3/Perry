from Perry.Extra.pjec import endComponent

class random:
  def int(low = 0, max = 1, include=0):
    return endComponent(f"Math.floor(Math.random() * ({max} - {low} + {include}) ) + {low};")