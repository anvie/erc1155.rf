#!/usr/bin/python3

from brownie import $name_pascal_case$, accounts, config
import json

# BASE_URL="https://$name_snake_case$.one/meta/"
BASE_URL="https://ipfs.io/ipfs/QmTTs1nv828MRno5p6NFbxjiWb8qaVFLCY52iF2bhYDtEJ/"


def main():
    owner = accounts.add(config['wallets']['owner_key'])
    admin = accounts.add(config['wallets']['admin_key'])

    print("Deploying $name_snake_case$-contract...")
    print("using owner key:", owner.address)

    # return $name_pascal_case$.deploy("https://$name_snake_case$.one/meta/", owner, admin, {'from': owner}, publish_source=True)
    contract = $name_pascal_case$.deploy(BASE_URL, admin, {'from': owner})
    print("contract address:", contract.address)

    standard_json_input = $name_pascal_case$.get_verification_info()['standard_json_input']
    with open('$name_pascal_case$Flattened.json', 'w') as f:
      f.write(json.dumps(standard_json_input))
    print("$name_pascal_case$Flattened.json saved.")

