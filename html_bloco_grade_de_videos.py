def gerar_grade_de_videos(videos):
    """
    Gera uma grade de vídeos com links para assistir e títulos exibidos ao passar o mouse.

    Parâmetros:
    videos (list): Uma lista de nomes de vídeos.

    Retorna:
    str: Uma string HTML representando a grade de vídeos.
    """
    html = "<div class='video-grid'>"
    for video in videos:
        html += f"<a href='ver_video?video={video}'><img src='thumbs/V-{video}.png' title='{video}'></a>"
    html += "</div>"
    return html
