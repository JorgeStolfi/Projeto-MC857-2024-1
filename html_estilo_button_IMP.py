import re

def gera(cor_fundo):
  fam_fonte = "Courier"
  peso_fonte = "Bold"
  tam_fonte = "18px"
  estilo = \
    " color: #000000; " + \
    " font-family:" + fam_fonte + ";" + \
    " font-weight:" + peso_fonte + ";" + \
    " font-size:" + tam_fonte + ";" + \
    " background:" + cor_fundo + ";" + \
    " padding: 2px 5px 2px 5px; " + \
    " border-radius: 5px; " + \
    " transition: all 0.4s ease 0s;"
  return estilo

def escolhe_cor_fundo(texto):
  
  # Reduz o texto à primeira palavra:
  chave = (re.sub(r'[ ].*$', "", texto)).lower()
  
  cores = {
      "recalcular": "#44eeee",
      #
      "confirmar":  "#55ee55",
      "enviar":     "#55ee55",
      "salvar":     "#55ee55",
      "subir":      "#55ee55",
      "postar":     "#55ee55",
      #
      "entrar":     "#ff88ee",
      #
      "comentar":   "#88eeff",
      "responder":  "#88eeff",
      "cadastrar":  "#88eeff",
      #
      "ok":         "#aaff66",
      "principal":  "#aaff66",
      #
      "meu":        "#c8fac8",
      "meus":       "#c8fac8",
      "minha":      "#c8fac8",
      "minhas":     "#c8fac8",
      #
      "cancelar":   "#ee5555",
      #
      "buscar":     "#eeccff",
      #
      "alterar":    "#ffcc55",
      "editar":     "#ffcc55", 
      #
      "ver":        "#eeee55",
      "examinar":   "#eeee55",
      #
      "fechar":     "#ffcc88",
      "sair":       "#ffcc88",
    }
    
  cor = cores.get(chave, "#cccccc")
  return cor
  
