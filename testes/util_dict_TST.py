#! /usr/bin/python3

from util_erros import aviso_prog
import util_dict
from util_testes import testa_funcao
import sys, re
import obj_raiz
import db_tabelas_do_sistema
import db_base_sql
import obj_usuario
import obj_sessao
import obj_video
import obj_comentario

sys.stderr.write("!!! Testar as funções !!!\n")
ok_global = False

modulo = util_dict

sys.stderr.write("  Conectando com base de dados...\n")
res = db_base_sql.conecta("DB",None,None)
assert res == None

sys.stderr.write("  Criando alguns objetos...\n")
db_tabelas_do_sistema.cria_todos_os_testes(True)

def teste_normaliza_busca_por_data():
  # TUPLAS DO TIPO ({nome_test}, {args} ,{resultado_esperado})
  casos_de_teste = [
    ("SEM_DATA", {}, []),
    ("DATA_MIN_E_DATA", {"data_min": "2024-02-02", "data": "2024-02-02"}, ["A busca não pode usar 'data' com 'data_min', 'data_max'", "A busca não pode usar 'data_min' sem 'data_max'"]),
    ("DATA_MIN_SEM_DATA_MAX", {"data_min": "2024-02-02"}, ["A busca não pode usar 'data_min' sem 'data_max'"]),
    ("DATA_MAX_SEM_DATA_MIN", {"data_max": "2024-02-02"}, ["A busca não pode usar 'data_max' sem 'data_min'"] ),
    ("NORMALIZADO", {"data_max": "2024-02-02", "data_min":  "2024-02-02"}, [])
  ]

  for (rot, args, esperado) in casos_de_teste:
    global ok_global
    ok_global = testa_funcao(rot, modulo, modulo.normaliza_busca_por_data, esperado, False, None, None, args)

def teste_normaliza_busca_por_nota():
  # TUPLAS DO TIPO ({nome_test}, {args} ,{resultado_esperado})
  casos_de_teste = [
    ("SEM_NOTA", {}, []),
    ("NOTA_MIN_E_NOTA", {"nota_min": "1.0", "nota": "1.0"}, ["A busca não pode usar 'nota' com 'nota_min', 'nota_max'", "A busca não pode usar 'nota_min' sem 'nota_max'"]),
    ("NOTA_MIN_SEM_NOTA_MAX", {"nota_min": "1.0"}, ["A busca não pode usar 'nota_min' sem 'nota_max'"]),
    ("NOTA_MAX_SEM_NOTA_MIN", {"nota_max": "2.0"}, ["A busca não pode usar 'nota_max' sem 'nota_min'"] ),
    ("NORMALIZADO", {"nota_min": "1.0", "nota_max": "2.0"}, [])
  ]

  for (rot, args, esperado) in casos_de_teste:
    global ok_global
    ok_global = testa_funcao(rot, modulo, modulo.normaliza_busca_por_nota, esperado, False, None, None, args)

def teste_para_identificadores():
  class TestObj(obj_raiz.Classe):
    def __init__(self, id, atrs):
      obj_raiz.Classe.__init__(self, id, atrs)

  casos_de_teste = [
    ("RETORNA_OBJETO", {"obj": TestObj('id', {}), "val": 123}, {"obj": "id", "val": 123}) 
  ]


  for (rot, args, esperado) in casos_de_teste:
    global ok_global
    ok_global = testa_funcao(rot, modulo, modulo.para_identificadores, esperado, False, None, None, args)

def teste_elimina_alteracoes_nulas():
  class TestObj(obj_raiz.Classe):
    def __init__(self, id, atrs):
      obj_raiz.Classe.__init__(self, id, atrs)
      
  obj1 = TestObj('id-1', {})
  obj2 = TestObj('id-2', {})

  casos_de_teste = [
    ('CMD_ARGS_SANITIZADO', [{'duplicata': 1, "diff": obj1 }, {'duplicata': 1, "diff": obj2}], {'diff': obj1})
  ]

  for (rot, args, esperado)in casos_de_teste:
    global ok_global
    ok_global = testa_funcao(rot, modulo, modulo.elimina_alteracoes_nulas, esperado, False, None, None, *args)

def teste_para_objetos():
  u_obj= obj_usuario.obtem_objeto("U-00000002")
  s_obj = obj_sessao.obtem_objeto("S-00000002") 
  v_obj = obj_video.obtem_objeto("V-00000002") 
  c_obj = obj_comentario.obtem_objeto("C-00000002") 
  casos_de_teste = [
    (
      'OBTEM_OBJ',
      {
        "U": "U-00000002",
        "S": "S-00000002",
        "V": "V-00000002",
        "C" : "C-00000002"
      },
      {
        "U": u_obj,
        "S": s_obj,
        "V": v_obj,
        "C": c_obj
        })
  ]

  for (rot, args, esperado) in casos_de_teste:
    global ok_global
    ok_global = testa_funcao(rot, modulo, modulo.para_objetos, esperado, False, None, None, args)

teste_normaliza_busca_por_data()
teste_normaliza_busca_por_nota()
teste_para_identificadores()
teste_elimina_alteracoes_nulas()
teste_para_objetos()
# ----------------------------------------------------------------------
# Veredito final:

if ok_global:
  sys.stderr.write("Testes terminaram normalmente.\n")
else:
  aviso_prog("Algum teste falhou", True)
