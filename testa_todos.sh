#! /bin/bash
# Last edited on 2024-03-13 16:26:10 by stolfi

inicio="$1"; shift

modulos=( \
  ` ( echo "# START" ; cat 00-MODULOS.txt ) \
      | sed -e "0,/${inicio}/d" \
      | egrep -v -e '^ *([#]|$)'
  ` \
)

# echo "modulos = ${modulos[*]}" 1>&2 

for m in "${modulos[@]}" ; do
  testa.sh ${m}
  echo "" 1>&2 
  echo "" 1>&2 
done
