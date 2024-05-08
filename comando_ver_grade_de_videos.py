from videos import comando_ver_grade_de_videos

def mostrar_grade_de_videos():
    """
    Mostra uma grade de vídeos em formato HTML.
    """
    # Chama a função comando_ver_grade_de_videos() para obter a grade de vídeos aleatórios
    html = comando_ver_grade_de_videos()
    print(html)
