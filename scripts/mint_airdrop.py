#!/usr/bin/python3

from brownie import $name_pascal_case$, accounts, config

import os, sys
sys.path.append(os.path.join("lib"))

from helpers import get_mint_sig, get_mint_sig_with_nonce, get_nonce

def main(arg_env, beneficary):
    amount = 1
    environment = arg_env or 'tests'
    print("environment: %s" % environment)
    if not config[environment]:
        print("Unknown environment: %s" % environment)
        return
    contract_address = config[environment]['contract_address']
    owner = accounts.add(config['wallets']['owner_key'])
    admin = accounts.add(config['wallets']['admin_key'])
    # accounts.remove(admin.address)
    # admin = accounts.add(config['wallets']['admin_key'])

    print("Minting...")
    print("using owner key:", owner.address, "balance:", owner.balance())
    print("using admin key:", admin.address)

    print("beneficary:", beneficary)
    print("amount:", amount)

    contract = $name_pascal_case$.at(contract_address)
    sig, nonce = get_mint_sig_with_nonce(owner, beneficary, amount, admin, airdrop=True)
    contract.mint(beneficary, amount, nonce, True, sig, {"from": owner, "amount": 0, "gas": 900000})

