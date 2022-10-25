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
    event Burn(uint256 indexed tokenId, address indexed burner);

    constructor(address _admin)
        ERC1155("$param.base_metadata_url$/{id}.json")
    {
        admin = _admin;
    }

    function changeAdmin(address _newAdmin) external onlyOwner {
        admin = _newAdmin;
    }

    function mint(uint32 qty) external payable returns (bool) {
        // @TODO: add your logic here
        _mint(_msgSender(), ITEM1, qty, "");
        _supplyFor[ITEM1] += qty;

        emit Mint(ITEM1, _msgSender());

        return true;
    }

    function mintWithSig(
        uint16 itemId,
        uint32 qty,
        uint64 nonce,
        Sig memory sig
    ) external payable returns (bool) {
        require(_supplyFor[itemId] + qty <= MAX_SUPPLY, "Limit exceeded");

        require(nonce >= uint64(block.timestamp) / 30, "Invalid nonce");

        bytes32 message = sigPrefixed(
            keccak256(abi.encodePacked(_msgSender(), itemId, qty, nonce))
        );

        require(_isSigner(admin, message, sig), "Invalid signature");

        _mint(_msgSender(), itemId, qty, "");
        _supplyFor[itemId] += qty;

        emit Mint(itemId, _msgSender());

        return true;
    }

    /**
     * @dev check supply for specific item.
     */
    function totalSupply(uint16 itemId) external view returns (uint256) {
        return _supplyFor[itemId];
    }

    function burn(uint16 itemId, uint256 amount) external {
        uint256 _bal = balanceOf(_msgSender(), itemId);
        require(_bal >= amount, "Not enough tokens");
        _supplyFor[itemId] -= amount;
        _burn(_msgSender(), itemId, amount);
        emit Burn(itemId, _msgSender());
    }
}
