#!/usr/bin/python3

import pytest
import brownie


def test_change_owner($name_snake_case$, accounts, owner):
    $name_snake_case$.transferOwnership(accounts[1], {"from": owner})
    assert $name_snake_case$.owner() == accounts[1]

def test_change_admin($name_snake_case$, accounts, owner):
    $name_snake_case$.changeAdmin(accounts[1], {"from": owner})
    assert $name_snake_case$.admin() == accounts[1]

def test_only_owner_can_change_admin($name_snake_case$, accounts, owner):
    with brownie.reverts():
        $name_snake_case$.changeAdmin(accounts[1], {"from": accounts[1]})
    
    $name_snake_case$.changeAdmin(accounts[1], {"from": owner})

    # admin cannot change admin
    with brownie.reverts():
        $name_snake_case$.changeAdmin(accounts[1], {"from": accounts[1]})

    $name_snake_case$.transferOwnership(accounts[1], {"from": owner})
    $name_snake_case$.changeAdmin(accounts[1], {"from": accounts[1]})

