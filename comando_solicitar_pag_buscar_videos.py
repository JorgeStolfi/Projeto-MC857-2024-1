import comando_solicitar_pag_buscar_videos_IMP

def processa(ses, args):
    """Esta função é chamada quando o usuário aperta o botão "Buscar Video"
    no menu geral da pagina do administrador.

    A função retorna uma página HTML {pag} com o formulário que mostra
    campos que podem ser usados para busca de Videos, com campos editáveis.
    O formulário deve conter um botão de sumbissão "Buscar".

    O argumento {ses} deve ser uma sessão atualmente aberta.

    A sessão aberta deve ser de um administrador, que pode realizar uma busca
    para encontrar qualquer video cadastrado"""
    return comando_solicitar_pag_buscar_videos_IMP.processa(ses, args)
