#! /bin/bash
# Last edited on 2024-05-17 14:39:15 by stolfi

fname="$1"; shift   # File to search in.
module="$1"; shift  # Module name.

# Finds uses of function "${module}.${func}" in a file.

# Remove garbage from file ${fname} leaving "${module}.${func}" at 
# beginning of line. Then remove "${module}."

cat ${fname} \
  | sed -e 's/ *[#].*$//g' \
  | tr -c '.a-zA-Z0-9_' '\n' \
  | sed -e '/^ *$/d' \
  | egrep -e "^(${module}|module|modulo)[.]" \
  | sed -e "s/^${module}[.]//g" \
  | sed -e "s/^module[.]//g" \
  | sed -e "s/^modulo[.]//g" \
  | sort | uniq

