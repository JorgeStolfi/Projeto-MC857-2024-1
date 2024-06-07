#! /bin/bash

# Uso: "testa.sh {MODULO}"
# Executa "testes/{MODULO}_TST.py" com o {PYTHONPATH} correto.
# Os resultados de funções que geram HTML estão em "testes/saida/{MODULO}.{ROTULO}.html"
# Cria uma página "testes/saida/{MODULO}.html" contendo a saida "stdout" 
# do programa de teste, e links para todos os resultados acima.

modulo="$1"; shift 

opref="testes/saida/${modulo}" # Prefixo dos arquivos HTML de saída.
otext="${opref}.txt"           # Saida {stdout+stderr} do programa de teste.
opage="${opref}.html"          # Página de saida principal.

# Garante que está no folder principal e não no subfolder:
if [[ ( ! ( -s ${modulo}.py ) ) && ( -s ../${modulo}.py ) ]]; then cd ..; pwd ; fi

# Verifica se o módulo existe:
if [[ ! ( -s ${modulo}.py ) ]]; then echo "** modulo ${modulo} nao existe" 1>&2; exit 1; fi

# Cria folder para saídas:
mkdir -p testes/saida

# Cria links para folders que o programa de testes e as páginas HTML podem querer ler:
for tdir in testes testes/saida; do 
  for idir in imagens videos avatares capas quadros DB; do
    ( cd ${tdir} && if [[ ! ( -r ${idir} ) ]]; then ln -s ../${idir}; fi )
  done
done

lista_funcoes_nao_testadas.sh ${modulo}

# Limpa arquivos de rodadas anteriores:
rm -fv ${otext} ${opage} ${opref}.*.html 

echo "=== executando teste \"testes/${modulo}_TST.py\" ======================" 1>&2
export PYTHONPATH=".:testes:..:/usr/lib/python3.6/site-packages/sos/plugins" ; \
  python3 testes/${modulo}_TST.py > ${otext} 2>&1

# Cria a página principal ${opage}:
if [[ -s ${opage} ]]; then
  echo "** programa gravou ${opage} em vez de ${opref}.{rotulo}.html" 1>&2;
  exit 1
fi

files=( `cd testes/saida && ( shopt -s nullglob; echo ${modulo}.*.html; shopt -u nullglob )` )

# Escreve o cabeçalho da página de índice:
printf "<!DOCTYPE HTML>\n" >> ${opage}
printf "<html>\n" >> ${opage}
printf "<head>\n" >> ${opage}
printf "<link rel=\"icon\" href=\"imagens/favicon.png\" type=\"image/x-icon\"> " +  \
printf "<link rel=\"icon\" href=\"imagens/favicon-32x32.png\" sizes=\"32x32\"> " +  \
printf "<meta charset=\"UTF-8\"/>\n" >> ${opage}
printf "<title>Teste de ${modulo}</title>\n" >> ${opage}
printf "</head>\n" >> ${opage}
printf "<body style=\"background-color:#eeeeee; text-indent: 0px\">\n" >> ${opage}

# Obtém todas as páginas HTML produzidas pelo programa de teste:
if [[ ${#files[@]} -eq 0 ]]; then
  echo "!! nenhuma página ${opref}.*.html criada." 1>&2 
  printf "<h3>Nenhuma página ${opref}.*.html foi criada</h3>\n"  >> ${opage} 
else
  echo "páginas criadas:" 1>&2 
  echo "${files[@]}" | tr ' ' '\012' 1>&2
  printf "<h3>Páginas HTML criadas:</h3>\n"  >> ${opage} 
  printf "<ul>\n" >> ${opage}
  for ff in "${files[@]}" ; do 
    printf "  <li><p><a href=\"%s\">%s</a></p></li>\n" "${ff}" "${ff}" >> ${opage} 
  done
  printf "</ul>\n" >> ${opage}
fi

# Providencia um aviso se nada foi escrito em {stdout} e {stderr}:
if [[ ( ! ( -s ${otext} ) ) ]]; then 
  echo "!! nada foi gravado em {stdout} ou {stderr}" 1>&2
  printf "<h3>Nada foi gravado em {stdout} ou {stderr}</h3>\n" >> ${opage}
else
  echo "gravado em {stdout} ou {stderr}:" 1>&2
  echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" 1>&2
  cat ${otext} 1>&2
  echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" 1>&2

  printf "<h3>Escrito em {stdout}+{stderr}:</h3>\n" >> ${opage}
  printf "<span style=\"font-family:Courier;\">\n" >> ${opage}
  cat ${otext} \
    | sed \
        -e 's:[&]:&amp;:g' \
        -e 's:>:\&gt;:g' \
        -e 's:<:\&lt;:g' \
        -e 's: :\&nbsp;:g' \
        -e 's:$:<br/>:g' \
    >> ${opage}
  printf "</span>\n" >> ${opage}
fi

# Escreve o fecho da página de índice:
printf "</body>\n" >> ${opage}
printf "</html>\n" >> ${opage}

ls -l ${opage} 1>&2

echo "======================================================================" 1>&2
