
import html_bloco_tabela_de_campos

def gera(id_com, atrs, admin):
    #com = obj_comentario.busca_por_identificador(id_com)
    atrs = {}.copy() if atrs == None else atrs.copy()
    atrs.update( { 'id_comment': id_com } )


    dados_linhas = \
    (
      ( "Usuario",  "user",        "user",     None,             False, ),
      ( "Data",     "date",        "data",     None,             False, ),
      ( "Pai",      "comment",     "pai",      None,             False, ),
      ( "Texto",    "comment",     "text",     None,             False, ),
    )

    if id_com != None:
      dados_linhas += \
        ( 
          ( "Identificador",  "readonly",  'id_comment',   None,   True, ),
        )

    return html_bloco_tabela_de_campos.gera(dados_linhas, atrs, admin)