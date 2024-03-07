#! /bin/bash
# Last edited on DATE TIME by USER

inicio="$1"; shift

modulos=( \
  ` ( echo "# START" ; cat 00-MODULOS.txt ) \
      | sed -e "0,/${inicio}/d" \
      | egrep -v -e '^ *([#]|$)'
  ` \
)

echo "modulos = ${modulos[*]}" 1>&2 

for m in "${modulos[@]}" ; do
  testa.sh ${m}
done
