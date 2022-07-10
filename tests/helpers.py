from eth_abi import is_encodable
from eth_abi.packed import encode_single_packed
import eth_utils

from eth_account.account import Account
from eth_account.messages import defunct_hash_message

import time


def solidity_keccak(abi_types, values, validity_check=False):
    """
    Executes keccak256 exactly as Solidity does.
    Takes list of abi_types as inputs -- `[uint24, int8[], bool]`
    and list of corresponding values  -- `[20, [-1, 5, 0], True]`

    Adapted from web3.py
    """
    if len(abi_types) != len(values):
        raise ValueError(
            "Length mismatch between provided abi types and values.  Got "
            "{0} types and {1} values.".format(len(abi_types), len(values))
        )
    if validity_check:
        for t, v in zip(abi_types, values):
            if not is_encodable(t, v):
                print(f'Value {v} is not encodable for ABI type {t}')
                return False
    hex_string = eth_utils.add_0x_prefix(''.join(
        encode_single_packed(abi_type, value).hex()
        for abi_type, value
        in zip(abi_types, values)
    ))
    # hex_string = encode_abi_packed(abi_types, values).hex()
    return eth_utils.keccak(hexstr=hex_string)


def get_mint_sig(sender, to, count, admin, nonce, airdrop=False):
    m_hash = solidity_keccak(abi_types=["uint32", "address", "address", "uint32", "uint64", "bool"],
                             values=[1, sender.address, to.address,
                                     count, nonce, airdrop],
                             validity_check=True)

    msg_hash = defunct_hash_message(hexstr=m_hash.hex())
    sig = Account.signHash(msg_hash, admin.private_key)
    return (sig.r, sig.s, sig.v)


def get_mint_sig_with_nonce(sender, to, count, admin, airdrop=False):
    nonce = get_nonce()
    sig = get_mint_sig(sender, to, count, admin, nonce, airdrop)
    return sig, nonce


def get_nonce():
    return int(int(time.time()) / 30)
