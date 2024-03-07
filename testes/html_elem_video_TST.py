import html_elem_video
import util_testes

frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
util_testes.testa_gera_html(html_elem_video, html_elem_video.gera, "1", frag, pretty, "virus.mp4", "Um virus animado", 320)
