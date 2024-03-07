import html_elem_img
import util_testes

frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
pretty = False # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
util_testes.testa_gera_html(html_elem_img, html_elem_img.gera, "1", frag, pretty, "GO.png", "Texto alternativo da imagem", 100)