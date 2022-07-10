#!/usr/bin/python3

from brownie import $name_pascal_case$, accounts, config

DECIMAL = 10 ** 18

def main(arg_env, new_price=3 * DECIMAL):
    environment = arg_env or 'tests'
    contract_address = config[environment]['contract_address']
    owner = accounts.add(config['wallets']['owner_key'])

    print("Setting price to:", new_price)
    print("using owner key:", owner.address)

    contract = $name_pascal_case$.at(contract_address)
    contract.setPrice(new_price, {'from': owner})

