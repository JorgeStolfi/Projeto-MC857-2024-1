def escolhe_cor_fundo(texto):
    text_splited = texto.split()

    if text_splited[0] == "Ver":
        return '#808080'

    if text_splited[0] == "Buscar":
        return 'PaleVioletRed'

    if text_splited[0] == "Meus" or text_splited[0] == "Meu" or text_splited[0] == "Minha" or text_splited[0] == "Minhas":
        return "#c8fac8"
    
    if text_splited[0] == "Entrar":
        return '#55ee55'
    
    if text_splited[0] == "Sair":
        return "#ffcc88"

    if text_splited[0] == "Cancelar":
        return '#ee5555'
    
    if text_splited[0] == "Fechar":
        return '#FF7700'
    
    if text_splited[0] == "OK":
        return '#55ee55'

    if text_splited[0] == "Responder":
        return '#55ee55'
    
    if text_splited[0] == "Editar":
        return '#eeee55'
    
    if text_splited[0] == "Alterar":
        return '#eeee55'
    
    if text_splited[0] == "Principal":
        return "#60a3bc"

    if text_splited[0] == "Cadastrar":
        return '#55ee55'
    
    if text_splited[0] == "Subir":
        return "#88eeff"
    
    if text_splited[0] == "Comentar":
        return '#55ee55'
    
    if text_splited[0] == "Checar":
        return "#eeccff"
    
    if text_splited[0] == "Confirmar":
        return '#55ee55'
    
    if text_splited[0] == "Postar":
        return '#55ee55'
    
    if text_splited[0] == "Salvar":
        return '#55ee55'
    
    if text_splited[0] == "Enviar":
        return '#55ee55'
    
    if text_splited[0] == "Botao":
        return '#55ee55'