### Here is where I will store interesting posts/articles related to this repo

[This is a simplified explanation on how bitcoin mining principle works.](https://bitcoin.stackexchange.com/questions/8031/what-are-bitcoin-miners-really-solving)

[This is the explanation of what is the nonce we implemented in this simple blockchain](https://en.bitcoin.it/wiki/Nonce)


The main idea of PoW is finding a hash that meets certain criteria, in this case, number of zeros in the beggining given a certain dificulty.

Here is a explanation about the origin of the PoW concept applied in bitcoin: [Hashcash](https://en.wikipedia.org/wiki/Hashcash)
Basically it's computanionally expensive because finding the hash that meets the criteria requires the use of brute force.

#####Database

The original bitcoin projects seems to be using levelDB (key-value store).
For this case, we'll use [PickeDB](https://pythonhosted.org/pickleDB/) which is a lightweight key-value store based in python.

We are going to use the following structure:
* DB to store chainstate
* DB to store index as key and hash as value
* DB to store hash as key and properties of that block as values

[This is an interesiting discussion on why bitcin core did originally picked LevelDB](https://bitcoin.stackexchange.com/questions/48959/why-is-bitcoin-core-using-leveldb-instead-of-redis-or-sqlite)

[And this is why I opted for chosing SQLite, nice excuse to try it](https://lists.linuxfoundation.org/pipermail/bitcoin-dev/2015-October/011604.html)


#####Basic idea behind PoW

It should be difficult to calculate but really easy to verify that the nonce provided is the one that solves the computational problem