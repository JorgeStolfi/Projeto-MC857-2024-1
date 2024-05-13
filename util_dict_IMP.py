import util_dict
import sys, re

def elimina_alteracoes_nulas(cmd_args, obj_atrs):
  if obj_atrs != None:
    # Elimina argumentos supérfluos de {cmd_args}:
    for chave, val_atual in obj_atrs.items():
      if chave in cmd_args:
        # Reduz objetos em {obj_atrs} a seus identificadores:
        if isinstance(val_atual, obj_raiz.Classe):
          val_atual = val_atual.id
        # Valores em {cmd_args} não podem ser objetos:
        val_novo = cmd_args[chave]
        assert not isinstance(val_novo, obj_raiz.Classe)
        # Elimina se valores são inalterados:
        if val_novo == val_atual:
          cmd_args.pop(chave)

def verifica_chaves_espurias(cmd_args, obj_atrs):
  if obj_atrs != None:
    # Valida chaves de {cmd_args}:
    for chave, val_novo in cmd_args.items():
      assert chave in obj_atrs, f"Parâmetro espúrio do comando {chave} = {val_novo}" 


def para_objetos(args_cmd):
  assert args_cmd != None and isinstance(args_cmd, dict), "parâmetro inválido"

  atrs_res = {}
  erros = []
  for chave, val in args_cmd.items():
    if isinstance(val, str) and re.match(r'^[USVC]-[0-9]{8}$', val):
      let = val[0]
      if let == 'U':
        obj = obj_usuario.obtem_objeto(val)
      elif let == 'S':
        obj = obj_sessao.obtem_objeto(val)
      elif let == 'V':
        obj = obj_video.obtem_objeto(val)
      elif let == 'C':
        obj = obj_comentario.obtem_objeto(val)
      else:
        assert False
      atrs_res[chave] = obj
    else:
      atrs_res[chave] = val
  return atrs_res
  
def para_identificadores(atrs_obj): 
  assert atrs != None and isinstance(atrs, dict), "parâmetro inválido"
  args_res = {}
  erros = []
  for chave, val in atrs_obj.items():
    if isinstance(val, obj_raiz.Classe):
      args_res[chave] = val.id
    else:
      args_res[chave] = val
  return args_res
