
.PHONY: testes_de_modulos teste_unico

# Módulos que não devem ter programas de teste:
MODULOS_NAO_TESTAR := ${shell gawk '/^[N]/{ print $$2; }' 00-MODULOS.txt}

# Módulos cujos testes estavam OK na última verificação:
MODULOS_OK := ${shell gawk '/^[A]/{ print $$2; }' 00-MODULOS.txt}

# Módulos com testes faltando:
MODULOS_BUG_NO_TST := ${shell gawk '/^[@]/{ print $$2; }' 00-MODULOS.txt}

# Módulos cujos testes falharam na última verificação:
MODULOS_BUG_NO_IMP := ${shell gawk '/^[*]/{ print $$2; }' 00-MODULOS.txt}

MODULOS_RUINS := ${shell gawk '/^[*@]/{ print $$2; }' 00-MODULOS.txt}

# Todos os módulos testáveis:
MODULOS_TODOS := ${shell gawk '/^[*A@]/{ print $$2; }' 00-MODULOS.txt}

# Módulos a testar em {testes_de_modulos}:
MODULOS := ${MODULOS_TODOS}
# MODULOS := ${MODULOS_RUINS}
# MODULOS := ${MODULOS_BUG_NO_IMP}

# O que "make" deve fazer:

# all: testes_de_modulos 00-LINKS.html
# all: teste_unico 00-LINKS.html
all: roda_servidor 00-LINKS.html

# Roda testes dos módulos em ${MODULOS}:
testes_de_modulos:
	-rm -fv testes/saida/*.html
	for modulo in ${MODULOS} ; do \
	  { ./testa.sh $${modulo} ; echo "" ; } ; \
        done

# MODULO := identificador
# MODULO := conversao_sql
# MODULO := base_sql
# MODULO := tabela_generica
# MODULO := usuario
# MODULO := sessao 
# MODULO := compra
# MODULO := html_form_dados_de_trecho
# MODULO := html_pag_trecho
# MODULO := html_form_dados_de_poltrona
# MODULO := html_pag_poltrona
MODULO := html_input

teste_unico:
	./testa.sh ${MODULO}

roda_servidor:
	( ./servidor.py & sleep 1000 )

00-LINKS.html: 00-LINKS.txt ~/bin/convert_links_to_html.gawk
	~/bin/convert_links_to_html.gawk 00-LINKS.txt > 00-LINKS.html
