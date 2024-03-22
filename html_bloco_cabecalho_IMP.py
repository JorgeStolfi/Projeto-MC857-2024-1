import html_elem_link_img


def gera(title, grande):


  if grande:
    ht_img = html_elem_link_img.gera("logotipo.png", "logotipo", 60, "imagens/logotipo.png")
    styleh1 = " style = 'background-color: #ffdf31; font-family: \"Rowdies\", cursive; line-height: 60px;' "
    header_title = "<h1 " + styleh1 + ">" + ht_img + " " + title + "</h1>"
  else:
    styleh2 = " style = 'background-color: lightgray; font-family: \"Noto Sans JP\", sans-serif;' "
    header_title = "<h2 " + styleh2 + ">" + title + "</h2>"

  return \
    "<!DOCTYPE HTML>\n" + \
    "<html>\n" + \
    "<head>\n" + \
    "<link rel=\"icon\" href=\"imagens/favicon.png\" type=\"image/x-icon\"> " +  \
    "<link rel=\"shortcut icon\" href=\"imagens/favicon.png\" type=\"image/x-icon\"> " +  \
    "<link rel=\"icon\" href=\"imagens/favicon-32x32.png\" sizes=\"32x32\"> " +  \
    "<link rel=\"shortcut icon\" href=\"imagens/favicon-32x32.png\" sizes=\"32x32\" type=\"image/png\"> " + \
    "<link href=\"https://fonts.googleapis.com/css2?family=Rowdies&display=swap\" rel=\"stylesheet\"> " + \
    "<link href=\"https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@500&display=swap\" rel=\"stylesheet\">"  + \
    "<meta charset=\"UTF-8\"/>\n" + \
    "<title>" + title + "</title>\n" + \
    "</head>\n" + \
    "<body style=\"background-color:#eeeeee; text-indent: 0px\">\n" + \
    header_title
