#!/usr/bin/python3
import pytest
import brownie

from consts import *
from helpers import get_mint_sig_with_nonce

import pytest
import brownie

def test_owner_admin($name_snake_case$, owner, admin):
    assert $name_snake_case$.owner() == owner
    assert $name_snake_case$.admin() == admin

def test_supports_interface($name_snake_case$, owner, admin):
    assert $name_snake_case$.supportsInterface("0x01ffc9a7") == True
    # assert $name_snake_case$.supportsInterface("0x80ac58cd") == True
    # assert $name_snake_case$.supportsInterface("0x780e9d63") == True
    assert $name_snake_case$.supportsInterface("0xffffffff") == False

@pytest.mark.parametrize("count", range(1, 5))
def test_total_supply($name_snake_case$, accounts, admin, count):
    assert $name_snake_case$.totalSupply(ITEM1) == 0
    sig, nonce = get_mint_sig_with_nonce(accounts[3], ITEM1, count, admin)
    $name_snake_case$.mint(count, {"from": accounts[3], "amount": 15 * count * 10 ** 17})
    assert $name_snake_case$.totalSupply(ITEM1) == count

@pytest.mark.parametrize("idx", range(1, 10))
def test_total_supply_increased($name_snake_case$, accounts, admin, idx):
    assert $name_snake_case$.totalSupply(ITEM1) == 0
    for i in range(idx):
        sig, nonce = get_mint_sig_with_nonce(accounts[3], ITEM1, 1, admin)
        $name_snake_case$.mint(1, {"from": accounts[3], "amount": 15 * 10 ** 17})
    assert $name_snake_case$.totalSupply(ITEM1) == idx

def test_base_uri($name_snake_case$, admin):
    assert $name_snake_case$.uri(1) == "$param.base_metadata_url$/{id}.json"
    sig, nonce = get_mint_sig_with_nonce(admin, ITEM1, 1, admin)
    $name_snake_case$.mint(1, {"from": admin, "amount": 15 * 10 ** 17})
    assert $name_snake_case$.uri(1) == "$param.base_metadata_url$/{id}.json"
    $name_snake_case$.mint(1, {"from": admin, "amount": 15 * 10 ** 17})
    assert $name_snake_case$.uri(2) == "$param.base_metadata_url$/{id}.json"
    $name_snake_case$.mint(1, {"from": admin, "amount": 15 * 10 ** 17})
    assert $name_snake_case$.uri(3) == "$param.base_metadata_url$/{id}.json"
    $name_snake_case$.mint(1, {"from": admin, "amount": 15 * 10 ** 17})
    assert $name_snake_case$.uri(4) == "$param.base_metadata_url$/{id}.json"
