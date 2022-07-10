#!/usr/bin/python3

from brownie import $name_pascal_case$, accounts, config


def main(arg_env, base_uri):
    environment = arg_env or 'tests'
    contract_address = config[environment]['contract_address']
    owner = accounts.add(config['wallets']['owner_key'])
    # admin = accounts.add(config['wallets']['admin_key'])

    print("Setting base URI to:", base_uri)
    print("using owner key:", owner.address)

    contract = $name_pascal_case$.at(contract_address)
    contract.setBaseURI(base_uri, {'from': owner})

