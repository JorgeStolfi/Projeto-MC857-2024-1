import random
from videos import gerar_grade_de_videos

def comando_ver_grade_de_videos(total_videos=12, colunas=4):
    """
    Escolhe um conjunto aleatório de vídeos e exibe como uma grade de thumbs.

    Parâmetros:
    total_videos (int): O número total de vídeos para escolher aleatoriamente.
    colunas (int): O número de colunas na grade de vídeos.

    Retorna:
    str: Uma string HTML representando a grade de vídeos aleatórios.
    """
    # Supondo que você tenha uma lista de todos os vídeos disponíveis
    lista_de_videos = [f"{str(i).zfill(8)}" for i in range(1, 1001)]  # Exemplo de lista de vídeos
    
    # Selecionar aleatoriamente um conjunto de vídeos
    videos_aleatorios = random.sample(lista_de_videos, total_videos)
    
    # Gerar a grade de vídeos com os vídeos selecionados aleatoriamente
    return gerar_grade_de_videos(videos_aleatorios)
