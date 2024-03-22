#! /bin/bash

# Uso: "testa.sh {MODULO}"
# Executa "testes/{MODULO}_TST.py" com o {PYTHONPATH} correto,
# e manda a saída "stdout" (se não for vazia)
# para testes/saida/{MODULO}.html

modulo="$1"; shift  # 
opref="testes/saida/${modulo}"
ofile="${opref}.html"

if [[ $PWD =~ .*/testes ]]; then cd .. ; fi
mkdir -p testes/saida
( cd testes && if [[ ! ( -r imagens ) ]]; then ln -s ../imagens; fi )
( cd testes && if [[ ! ( -r testa.sh ) ]]; then ln -s ../testa.sh; fi )
( cd testes && if [[ ! ( -r Makefile ) ]]; then ln -s ../Makefile; fi )
( cd testes/saida && if [[ ! ( -r imagens ) ]]; then ln -s ../imagens; fi )
echo "=== executando teste testes/${modulo}_TST.py ======================"
rm -f ${ofile} ${opref}.*.html 
export PYTHONPATH=".:testes:..:/usr/lib/python3.6/site-packages/sos/plugins" ; \
  python3 testes/${modulo}_TST.py > ${ofile}
if [[ ( -e ${ofile} ) && ( ! ( -s ${ofile} ) ) ]]; then 
  # echo "" 1>&2
  # echo "${ofile} is empty" 1>&2
  rm -f ${ofile}
fi
shopt -s nullglob
files=( ${opref}.*.html  )
shopt -u nullglob
if [[ -s ${ofile} ]]; then files+=( ${ofile} ); fi
if [[ ${#files[@]} -gt 0 ]]; then
  echo "Paginas criadas:" 1>&2 
  ls -1 ${files[@]}
else
  echo "Nenhuma página ${opref}*.html criada." 1>&2 
fi
echo "======================================================================"
