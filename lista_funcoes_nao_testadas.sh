#! /bin/bash
# Last edited on 2024-05-19 19:42:32 by stolfi

modulo="$1"; shift

# Pega as funções da interface:
egrep -e '^def ' ${modulo}.py \
  | sed \
      -e 's/^def *//g' \
      -e 's/[ ]*[\\(].*$//g' \
  | sort \
  > .funcs

# Acha funções da interface que não estão sendo testadas
lista_chamadas_de_funcoes.sh testes/${modulo}_TST.py ${modulo} > .uses
egrep --invert-match --line-regexp -f .uses .funcs  > .missing
if [[ -s .missing ]]; then
  echo "!! Atenção: estas funções da interface não são chamadas pelo programa de teste:" 1>&2
  cat .missing | sed -e 's:^:  :g' 1>&2 
fi

# Mostra chamadas que estão comentadas
cat testes/${modulo}_TST.py | egrep -e '^[#]+ *test' > .commented
if [[ -s .commented ]]; then
  echo "!! Atenção: estas chamadas de funções no programa de testes estão comentadas:" 1>&2
  cat .commented | sed -e 's:^:  :g' 1>&2 
fi
