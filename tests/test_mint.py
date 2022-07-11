#!/usr/bin/python3
import pytest
import brownie

from consts import *
from helpers import get_mint_sig, get_mint_sig_with_nonce, get_nonce

import pytest
import brownie


def test_mint($name_snake_case$, accounts, admin):
    sig, nonce = get_mint_sig_with_nonce(accounts[1], ITEM1, 3, admin)
    tx = $name_snake_case$.mintWithSig(ITEM1, 3, nonce, sig, {"from": accounts[1], "amount": 15 * 3 * 10 ** 17})

    assert tx.return_value == True
    assert $name_snake_case$.balanceOf(accounts[1], ITEM1) == 3

    assert len(tx.events['Mint']) == 1

def test_mint_airdrop_should_free($name_snake_case$, accounts, admin):
    sig, nonce = get_mint_sig_with_nonce(accounts[1], ITEM1, 1, admin, airdrop=True)
    tx = $name_snake_case$.mintWithSig(ITEM1, 1, nonce, True, sig, {"from": accounts[1], "amount": 0})
    assert tx.return_value == True
    assert $name_snake_case$.balanceOf(accounts[2]) == 0

def test_mint_sign_count($name_snake_case$, accounts, admin):
    sig, nonce = get_mint_sig_with_nonce(accounts[1], ITEM1, 3, admin)
    with brownie.reverts("Invalid signature"):
        $name_snake_case$.mintWithSig(ITEM1, 30, nonce, sig, {"from": accounts[1], "amount": 15 * 30 * 10 ** 17})


def test_mint_invalid_signature($name_snake_case$, accounts, admin):
    with brownie.reverts("Invalid signature"):
        sig, nonce = get_mint_sig_with_nonce(accounts[1], ITEM1, 1, admin)
        $name_snake_case$.mintWithSig(accounts[3], ITEM1, 1, nonce, sig, {"from": accounts[3], "amount": 15 * 10 ** 17})
    with brownie.reverts("Invalid signature"):
        random_acc = accounts.add()
        sig, nonce = get_mint_sig_with_nonce(accounts[1], ITEM1, 1, random_acc)
        $name_snake_case$.mintWithSig(accounts[3], ITEM1, 1, nonce, sig, {"from": admin, "amount": 15 * 10 ** 17})


def test_mint_invalid_nonce($name_snake_case$, accounts, admin):
    with brownie.reverts("Invalid nonce"):
        random_acc = accounts.add()
        nonce = get_nonce() - 30
        sig = get_mint_sig(accounts[1], ITEM1, 1, nonce, random_acc)
        $name_snake_case$.mintWithSig(accounts[3], ITEM1, 1, nonce, sig, {"from": admin, "amount": 15 * 10 ** 17})

def test_mint_invalid_nonce_by_time_lapsed($name_snake_case$, accounts, admin, chain):
    with brownie.reverts("Invalid nonce"):
        random_acc = accounts.add()
        nonce = get_nonce()
        chain.sleep(30)
        sig = get_mint_sig(accounts[1], ITEM1, 1, nonce, random_acc)
        $name_snake_case$.mintWithSig(accounts[3], ITEM1, 1, nonce, sig, {"from": admin, "amount": 15 * 10 ** 17})


def test_burn($name_snake_case$, accounts, admin):
    sig, nonce = get_mint_sig_with_nonce(accounts[1], ITEM1, 1, admin)
    $name_snake_case$.mintWithSig(ITEM1, 1, nonce, sig, {"from": accounts[1], "amount": 15 * 10 ** 17})
    $name_snake_case$.burn(1, {"from": accounts[1]})
    assert $name_snake_case$.totalSupply(ITEM1) == 0

# def test_mint_max_supply($name_snake_case$, accounts, admin):
#     assert $name_snake_case$.totalSupply(ITEM1) == 0
#     assert $name_snake_case$.maxSupply() == MAX_SUPPLY
#     with brownie.reverts():
#         sig, nonce = get_mint_sig_with_nonce(accounts[1], ITEM1, 3, admin)
#         for i in range(0, MAX_SUPPLY + 1):
#             $name_snake_case$.mintWithSig(ITEM1, 3, nonce, sig, {"from": accounts[1], "amount": 15 * 10 ** 17})

def test_non_owner_cant_burn($name_snake_case$, accounts, admin):
    sig, nonce = get_mint_sig_with_nonce(accounts[1], ITEM1, 1, admin)
    $name_snake_case$.mintWithSig(ITEM1, 1, nonce, sig, {"from": accounts[1], "amount": 15 * 10 ** 17})
    with brownie.reverts("only owner can burn"):
        $name_snake_case$.burn(1, {"from": accounts[2]})

def test_mint_emits_events($name_snake_case$, accounts, admin):
    sig, nonce = get_mint_sig_with_nonce(accounts[5], accounts[5], 2, admin)
    tx = $name_snake_case$.mintWithSig(accounts[5], 2, nonce, sig, {"from": accounts[5], "amount": 15 * 2 * 10 ** 17})
    assert len(tx.events['Mint']) == 2
    assert tx.events["Mint"][0]["tokenId"] == 1
    assert tx.events["Mint"][0]["owner"] == accounts[5].address
    assert tx.events["Mint"][1]["tokenId"] == 2
    assert tx.events["Mint"][0]["owner"] == accounts[5].address
