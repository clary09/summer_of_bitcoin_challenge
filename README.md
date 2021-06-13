# summer_of_bitcoin_challenge
Bitcoin miners construct blocks by selecting a set of transactions from their mempool. Each transaction in the mempool:
1. includes a fee which is collected by the miner if that transaction is included in a block
2. has a weight , which indicates the size of the transaction
3. may have one or more parent transactions which are also in the mempool

### This transaction.py reads a file mempool.csv, with the format:
txid,fee,weight,parent_txids

### The output from the program is txids, separated by newlines, which make a valid block, maximizing the fee to the miner.
### The txids are arranged in descending order of their fees.
### The block.text displays the output of the code.
