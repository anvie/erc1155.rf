pragma solidity ^0.8.0;

// SPDX-License-Identifier: MIT

/**
 *
 * This code is part of $name_pascal_case$ project (https://xxxx).
 *
 * Author: $param.author_name$
 *
 * $param.description$
 *
 */

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "./SigVerifier.sol";

contract $name_pascal_case$ is ERC1155, Ownable, SigVerifier {
    uint256 public constant MAX_SUPPLY = $param.max_supply$;
    uint16 public constant ITEM1 = 1;

    address public admin;

    mapping(uint16 => uint256) private _supplyFor;

    event Mint(uint256 indexed tokenId, address indexed owner);

    constructor(address _owner, address _admin)
        ERC1155("$param.base_metadata_url$/{id}.json")
    {
        admin = _admin;
    }

    function changeAdmin(address _newAdmin) external onlyOwner {
        admin = _newAdmin;
    }

    function mint(uint32 qty) external payable {
        // @TODO: add your logic here
        _mint(_msgSender(), ITEM1, qty, "");
        _supplyFor[ITEM1] += qty;
    }

    function totalSupply(uint16 itemId) external view returns (uint256) {
        return _supplyFor[itemId];
     }
}
