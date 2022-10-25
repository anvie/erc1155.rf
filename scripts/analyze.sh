#!/usr/bin/env bash

slither ./contracts/$name_pascal_case$.sol \
  --solc-remaps "@openzeppelin=$HOME/.brownie/packages/OpenZeppelin/openzeppelin-contracts@4.3.2" \
  --solc $SOLC_BIN
