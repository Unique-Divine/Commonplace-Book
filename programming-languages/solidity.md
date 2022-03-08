### Getting Started

Solidity is an object-oriented language for implementing smart contracts. Smart contracts are programs that govern the behavior of accounts within the Ethereum state. 
- Statically typed
- Supports inheritance
- Compiled language

#### Install the Solidity Compiler

There are a few ways to install a Solidity compiler and each method has some tradeoffs.

Note that there are two compilers, `solcjs` and `solc`. The solc compiler has more features than solcjs, however it's portable and easy to install. See [[solcjs docs]](https://github.com/ethereum/solc-js). The commandline options of `solcjs` are not compatible with `solc` and tools such as `geth` that expect that behavior of `solc` will not work with `solcjs`.


- **Remix**: Remix is good for small contracts and quickly learning Solidity. 
  - Convenient option for testing nightly builds without installing multiple Solidity versions.
  - Online access: [Remix online](https://remix.ethereum.org/) without installing anything. 
  - Offline access: Go to https://github.com/ethereum/remix-live/tree/gh-pages and follow the installation instructions for the `.zip`. 
- **npm**: Quick and convenient way to install solcjs. `npm install -g solc`. THe commandline executable is named "solcjs".
- **Docker**: Docker images of Solidity builds are available using the `solc` image from the Ethereum organization. Instructions can be found [here][solidity-docs-installation].
- **Linux Packages**: Binary packages are available at [solidity/releases](https://github.com/ethereum/solidity/releases).
  - [Personal Package Archives (PPAs)][help-ubuntu-ppa] are available for Ubuntu. To download the latest stable version of `solc`, use the following commands:
  ```bash
  sudo add-apt-repository ppa:ethereum/ethereum
  sudo apt-get update
  sudo apt-get install solc
  ```
- MacOS, Windows, static binaries, and/or building from source: [[More information here]][solidity-docs-installation]


References:
- Solidity docs - [Installing Solidity][solidity-docs-installation]
- Personal Package Archives. [help.ubuntu][help-ubuntu-ppa]

[solidity-docs-installation]: https://docs.soliditylang.org/en/v0.8.12/installing-solidity.html
[help-ubuntu-ppa]: https://help.ubuntu.com/stable/ubuntu-help/addremove-ppa.html.en#:~:text=Personal%20Package%20Archives%20(PPAs)%20are,that%20it%20can%20be%20tested. 


#### Getting a professional development setup with Hardhat 

```
npm install yarn
npm install hardhat
```

Install ethers JS packages: 
```
yarn add --dev @nomiclabs/hardhat-ethers ethers
```

Private keys are kept in a `.env` to store environment variables.

Kovan is one of the Ethereum test networks.

Request some funds from the Kovan faucet via Chainlink's website at https://faucets.chain.link/.  This creates two transactions like the following: 
- https://kovan.etherscan.io/tx/0xbc4f9a9cda792384bd9fb55e4e1c3da2b67f5c0c88a709d986d689da7ba8f536
- https://kovan.etherscan.io/tx/0xa8395f85785361ad61bd7fcb1117459a3a6e0cad38b2f99087b733b623dca98e


Hardhat tutorial:

All solidity code goes in the contracts directory. 
