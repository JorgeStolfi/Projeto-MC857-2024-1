import obj_raiz
import sys, re
import obj_usuario
import obj_sessao
import obj_video
import obj_comentario

def elimina_alteracoes_nulas(cmd_args, obj_atrs):
  if obj_atrs != None:
    # Elimina argumentos supérfluos de {cmd_args}:
    for chave, val_atual in obj_atrs.items():
      if chave in cmd_args:
        val_novo = cmd_args[chave]
        # Reduz objetos a seus identificadores: 
        if isinstance(val_atual, obj_raiz.Classe): val_atual = val_atual.id
        if isinstance(val_novo, obj_raiz.Classe): val_novo = val_novo.id
        # Elimina se valores são inalterados:
        if val_novo == val_atual:
          cmd_args.pop(chave)
    # Verifica chaves espúrias:
    for chave, val_novo in cmd_args.items():
      assert chave in obj_atrs, f"Parâmetro espúrio do comando {chave} = {val_novo}"
  return cmd_args

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
  
def para_identificadores(obj_atrs): 
  assert obj_atrs != None and isinstance(obj_atrs, dict), "parâmetro inválido"
  args_res = {}
  erros = []
  for chave, val in obj_atrs.items():
    if isinstance(val, obj_raiz.Classe):
      args_res[chave] = val.id
    else:
      args_res[chave] = val
  return args_res

def normaliza_busca_por_data(atrs):
  erros = [ ]
  
  if 'data_min' in atrs or 'data_max' in atrs:
    if 'data' in atrs:
      erros.append("A busca não pode usar 'data' com 'data_min', 'data_max'")
    data_min = atrs.pop('data_min', None)
    data_max = atrs.pop('data_max', None)
    if data_min == None:
      erros.append("A busca não pode usar 'data_max' sem 'data_min'")
    elif data_max == None:
      erros.append("A busca não pode usar 'data_min' sem 'data_max'")
    else:
      # Busca intervalar:
      atrs['data'] = ( data_min, data_max, )
  
  return erros

def normaliza_busca_por_nota(atrs):
  erros = [ ]
  
  if 'nota_min' in atrs or 'nota_max' in atrs:
    if 'nota' in atrs:
      erros.append("A busca não pode usar 'nota' com 'nota_min', 'nota_max'")
    nota_min = atrs.pop('nota_min', None)
    nota_max = atrs.pop('nota_max', None)
    if nota_min == None:
      erros.append("A busca não pode usar 'nota_max' sem 'nota_min'")
    elif nota_max == None:
      erros.append("A busca não pode usar 'nota_min' sem 'nota_max'")
    else:
      # Busca intervalar:
      atrs['nota'] = ( nota_min, nota_max, )
  return erros
