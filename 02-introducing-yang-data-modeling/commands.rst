Install pyang
..code: bash
  pip install pyang

Clone YangModels
..code: bash
  mkdir -p ~/Documents/github.com/YangModels
  cd git@github.com:YangModels/yang.git
  clone git@github.com:YangModels/yang.git

View pyang for IETF interfaces
..code: bash
  pyang -f tree ~/Documents/github.com/YangModels/yang/
