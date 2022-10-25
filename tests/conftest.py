#!/usr/bin/python3

from brownie import config
import pytest


@pytest.fixture(scope="function", autouse=True)
def isolate(fn_isolation):
    # perform a chain rewind after completing each test, to ensure proper isolation
    # https://eth-brownie.readthedocs.io/en/v1.10.3/tests-pytest-intro.html#isolation-fixtures
    pass

@pytest.fixture(scope="module")
def owner(accounts):
    owner_key = config['wallets']['owner_key']
    if not owner_key:
        return accounts[0]
    acc = accounts.add(owner_key)
    return acc

@pytest.fixture(scope="module")
def admin(accounts):
    admin_key = config['wallets']['admin_key']
    if not admin_key:
        return accounts[1]
    acc = accounts.add(admin_key)
    return acc

@pytest.fixture(scope="module")
def $name_snake_case$($name_pascal_case$, $name_pascal_case$Test, owner, admin):
    _$name_snake_case$_contract = $name_pascal_case$.deploy(admin, {'from': owner})
    return _$name_snake_case$_contract
