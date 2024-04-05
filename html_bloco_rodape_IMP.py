from datetime import datetime, timezone

def gera():
  data_bin = datetime.now(timezone.utc)
  data_fmt = data_bin.strftime("%Y-%m-%d %H:%M:%S %z")
  return \
    "  <div>\n" + \
    "    <small><p>Página criada em " + data_fmt + "</p></small>\n" + \
    "  </div>\n" + \
    "  </body>\n" + \
    "</html>\n"
