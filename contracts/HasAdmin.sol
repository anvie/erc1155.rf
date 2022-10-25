pragma solidity ^0.8.0;

// SPDX-License-Identifier: MIT

contract HasAdmin {
    address private _admin;

    event AdminChanged(address indexed admin);

    modifier onlyAdmin {
        _onlyAdmin();
        _;
    }

    function _onlyAdmin() private view {
        require(_isAdmin(msg.sender), "Only admin may perform this action");
    }

    function admin() public view returns(address) {
        return _admin;
    }

    function _setAdmin(address account) internal {
        _admin = account;
        emit AdminChanged(_admin);
    }

    function _isAdmin(address account) internal view returns(bool) {
        return account == _admin;
    }

}
