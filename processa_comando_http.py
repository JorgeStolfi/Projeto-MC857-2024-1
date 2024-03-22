# Este módulo processa comandos HTTP (GET,POST, ou HEAD)
# recebidos do usuário.  

# Implementação desta interface:
import processa_comando_http_IMP

def cria_objeto_servidor(host,porta):
  """Devolve um objeto da classe {HTTPServer} que é usado pelo servidor HTTP
  para processar comandos GET, POST, e HEAD recebidos dos usuários remotos
  no {host} especificado (um string que é um endereço IP), pela porta especificada
  (um inteiro, p.ex. 80 ou 8081).  Se {host} for '0.0.0.0', aceita comandos de qualquer
  máquina."""
  return processa_comando_http_IMP.cria_objeto_servidor(host,porta)
