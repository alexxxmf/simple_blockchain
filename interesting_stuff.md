### Here is where I will store interesting posts/articles related to this repo

[This is a simplified explanation on how bitcoin mining principle works.](https://bitcoin.stackexchange.com/questions/8031/what-are-bitcoin-miners-really-solving)

[This is the explanation of what is the nonce we implemented in this simple blockchain](https://en.bitcoin.it/wiki/Nonce)


The main idea of PoW is finding a hash that meets certain criteria, in this case, number of zeros in the beggining given a certain dificulty.

Here is a explanation about the origin of the PoW concept applied in bitcoin: [Hashcash](https://en.wikipedia.org/wiki/Hashcash)
Basically it's computanionally expensive because finding the hash that meets the criteria requires the use of brute force.

#####Database

The original bitcoin projects seems to be using levelDB (key-value store).
For this case, we'll use [PickeDB](https://pythonhosted.org/pickleDB/) which is a lightweight key-value store based in python.