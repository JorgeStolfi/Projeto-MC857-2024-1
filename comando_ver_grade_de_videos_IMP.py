import html_pag_grade_de_videos 
import obj_sessao
import 

def processa(ses, cmd_args):
    
    # Estas condições devem ser satisfeitas por páginas geradas pelo sistema:
    assert ses == None or isinstance(ses, obj_sessao.Classe), "sessão inválida"
    if ses != None: assert obj_sessão.aberta(ses), "sessão já foi fechada"
    assert isinstance(cmd_args, dict) and len(dict) == 0, "argumentos inválidos"

    ncols = 4  # Colunas da grade.
    nlins = 5  # Linhas da grade.
    nvids = ncols*nlins  # Total de videos na grade.
    
    vid_ids = obj_video.amostra(nvids)
    
    pag = html_pag_grade_de_videos.gera(ses, vid_ids, ncols, None)
    return pag
