#! /usr/bin/python3

import html_bloco_erro
import html_elem_table
import html_elem_label
import html_elem_input
import html_elem_button_simples
import util_testes


def testa(rotulo, *args):
    """Testa {funcao(*args)}, grava resultado
    em "testes/saida/{modulo}.{funcao}.{rotulo}.html"."""

    modulo = html_elem_table
    funcao = modulo.gera
    frag = True  # {True} se for apenas um fragmento HTML, {False} se for página completa.
    pretty = False  # Se {True}, formata HTML para legibilidate (mas introduz brancos nos textos).
    util_testes.testa_gera_html(modulo, funcao, rotulo, frag, pretty, *args)


linhas = [].copy()

label_de_teste_input = html_elem_label.gera("Teste das funcionalidades de html_elem_table, coloque um input aqui embaixo", ":")
input_de_teste = html_elem_input.gera(None, "text", "input", None, None, True, "Me edite!", None)

label_de_teste_botao = html_elem_label.gera("Aperte o botão para ser redirecionado à URL principal", "!")
botao_de_teste = html_elem_button_simples.gera("OK", 'principal', None, '#55ee55')

erro_de_teste_html = html_bloco_erro.gera("Houston, we've got a problem. Nevermind, this is just a Test!")

cabecalho=("Coluna 1", "Coluna 2")
linhas.append((label_de_teste_input, input_de_teste))
linhas.append((label_de_teste_botao, botao_de_teste))
linhas.append((erro_de_teste_html, botao_de_teste))

testa("Teste", linhas, cabecalho)
