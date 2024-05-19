def gera(display, width, word_wrap, padding, line_height):

  estilo = \
    " display: " + display + ";" + \
    " width:" + width + ";" + \
    " word-wrap:" + word_wrap + ";" + \
    f" padding: {padding[0]} {padding[1]} {padding[2]} {padding[3]};" + \
    " line-height:" + line_height + ";"
  return estilo
