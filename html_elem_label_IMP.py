
def gera(rotulo, sep):
  if rotulo == None or rotulo == "":
    return ""
  else:
    return "<label>" + rotulo + (sep if sep != None else "") + "</label>"
