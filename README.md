# linux-blockchain
A open source blockchain joined by many engineers and researcher that can people understand total blockchain application architecture easily.

## Introduction to architecture modules

### consensus algorithm module
Consensus algorihtm is another topic in many blockchain. All of invest also only look this topic too. We also define an module for consensus algorithm, so that we can setup different consensus algorithm in this system and make a lot of different research and open source easily. The consesus algorihtm design can easily to implement their idea of conesensus algorithm and run on linux-blockchain system. They don't need to implement all blockchain architecture but they can demo their idea to everyone 

### P2P network module
There are so many P2P network protocol in the world, in the implementation of blockchain, like Ethereum, Nervos, EOS and BitCoin, they use different P2P Network but all of their purpose is to make a point to point communication. That why we define P2P Network as a module. In future, we can put different P2P network module in this linux-blockchain system. 

### contract executor module
There are many kind new smart contract can be added in this linux-blockchain, but the way to execute them is by corresponding contract executor. For example, The EVM in Ethereum can execute solidity smart contract, so EVM is like the contract-executor corresponding to sodility.

### smart contract module
The linux-blockchain can support different smart contract (mean different computer program). You can use their corresponding contract-executor to execute it. For now, we support python smart contract and python contract executor first.

### distributed data storage module
Many account model blockchain can save all record of state chaning and show current state in different account. The program in smart contract is like to make a state machine with this storage. So different distributed data storage should try to support these smart contract. The input of distributed data storage are smart contract executing and consensus algorithm. It should know how to sync data for different node. The output of distributed storage is a trust and managed datas of all account.

### client-interface module
Each runner on the P2P network is named node in Ethereum, Nervos and BitCoin. The runner(node) use their P2P network protocol to communicate in different node. But the node still need to face clients, So that the client can upload smart contract to the node and interact to the node. In the world of ethereum, they use JSONRPC that run on HTTP service to communicate with client.

In here, is give the name for this module as face-client module. The face-client module can not only be implemented by  JSONRPC. We exepct it can support TCP/IP , SPI, I2C, BLE and any different protocol. Because we exepct linux-blockchain can face different client implement by different technology, like FPGA, MCU, PLC, LabView, JavaScript, Server, desktop application, mobile, etc.	

### vallet module
You can think vallet module is like the wallet in ethereum. We don't call wallet module is because people alwasy think wallet as tool to play coin but not with the view of user experience and system integration. 

Vallet is responbile to enhance user experience, security, key management, sign transaction and application side development between face-client module and different kind of client (like MCU, FPGA, web client, mobile app ,etc.)



(https://hackmd.io/@FgfHJXr4TqqaJTKS4F__tw/HkgPrBbmS)
