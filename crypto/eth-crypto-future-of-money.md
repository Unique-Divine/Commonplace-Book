# Ethereum, Cryptocurrency, and the Future of Money    <!-- omit in toc -->

eth-crypto-future-of-money

Vitalik Buterin: Ethereum, Cryptocurrency, and the Future of Money - Lex Fridman Podcast #80
[[Podcast link]](https://youtu.be/3x1b_S6Qp2Q)
Date: 20年3月16日 


Quadratic funding: 
- Vitalik's primer article on [Quadratic Payments](https://vitalik.ca/general/2019/12/07/quadratic.html)
- Useful to combat the tragedy of the commons

Tragedy of the commons: Idea that if there is some public good that many people will benefit from, no one wants to contribute to it because they'll only get a small part of the benefit from their contribution even though they'll pay the full contribution.  

What's a public good?
- Privacy tools

In ETH network, they tried using this concept. 


#### What is the blockchain? Or perhaps, we might start with the Byzantine general's problem and Byzantine fault tolerance that Bitcoin was taking steps toward finding a solution for.

Timestamp [30:03](https://youtu.be/3x1b_S6Qp2Q?t=1803)

Byzantine general's problem: a thought experiment
- Suppose you have two (allied) generals camped outside a city and they're planning on when to attack the city. How can they communicate with each other to coordinate an attack on the city?
- They can send messengers.
- With only two generals, there's not really any solution in a finite number of rounds.
- With more than two generals, you 
Given certain numbers of generals and constraints, when can you launch an attack?

Many people have a misconception that this is an unsolved problem, but it was already  solved by [Lesli Lamport](https://lamport.azurewebsites.net/pubs/byz.pdf)
- [Lamport on Byzantine Generals and Byzantine Failures](https://www.youtube.com/watch?v=gKSbAEbNifA).

What's unsolved then? 
> All of these solutions assume that you've already agreed on a fixed list of who exactly the generals are. The generals can't be anonymous because the enemy could just be 99% of the generals. 

> In the 1980s and 90s, the use case for distirbuted systems was sort of "enterprisey". 
You could assume you knew who was running the computer networks. Flight control uses distributed systems processing. 

#### Cyberpunks had a different idea.

> They wanted to create a decentralized global permissionless currency. 

Cyberpunks didn't want any authorities. They didn't want any kind of privileged list of people. 

Who are the cyberpunks? TODO 




How do you use these techniques to **create consensus when you have no idea about identity**? One clever solution for this comes from Satoshi Nakamoto. At Vitalik's presentation at DevCon in 2019/2020, he said the thing that Satoshi invented was crypto economics, an idea that says you can use economic resources to limit how many identities one can get.

If there isn't any existing digital currency, the only way to do this is with **proof of work**. With proof of work, the solution is to publish the solution to a problem that has a clear implication of computational resources needed to solve it. If you solve it, you get an identity.

Proof of work is the fundamental idea proposed in the Bitcoin whitepaper.

#### [Lex] What's the idea of consensus that we wish to reach? Why is consensus important here and what is it?

Wire together a large number of computers so that they pretend to be a single computer, that of which continues to function even if a large proprotion of its constituents go down.

The cyberpunks wanted to make this system to run one program. That program puts in place a currency system.

Is proof of work a revolutional idea? The fact you can exchange resources for an identity?  TODO

A: Not necessarily. PoW has been put in place to prevent email spam in the past.


Why do we use the term blockchain?

Blockchain refers to the underlying data structure we use to store the sequence of transactions.

How does the fault tolerance work? Is it built into the blockchain data structure?

You have a bunch of nodes. The nodes occasionally create blocks and chain them together. Let's say block $b_1$ is valid. We want to append block $b_2$, which is also valid, but an attacker creates block $b_{2'}$ and wants to append it to $b_1$. 

In the event of an attack in the Bitcoin system, the nodes follow the **longest chain**. This means that if there was already a chain $b_1$→ $b_2$→$b_3$, the attack chain would be ignored since it would only have two blocks, $b_1$→$b_{2'}$. 

So what happens in the case that an attacker wants to revert a block and the resultant chain is the same length ($b_1 \to b_2$ versus $b_1 \to b_{2'}$)? TODO 

#### Does quantum  computing throw a wrench into any of this?

Someone asked me about this at Cosmoverse and I was caught completely off-guard. 

Quantum computers have two important algorithms related to cryptography.

#### Shorr's Algorithm

Shorr's algo: Shorr's algorithm compeltely breaks the hardness of certain kinds of mathematical problems. 
- You've probably heard of it being used to factor numbers (prime factorization). 
- Can be used to break elliptic curve cryptography.
- Can be used to break hidden order group.

> "The good news is that, for every major example of Shorr's algo breaking a problem, we already know of quantum proof alternatives."

Q: What is meant by "know of quantum proof alternatives"? TODO

> "We don't use these quantum proof alternatives yet because, in many cases, they're 5-10 times less efficient... The crypto community kind of knows that this is coming eventually and it's kind of ready to take the hit and switch to that stuff when we have to."

#### Grover's algorithm

Grover's algorithm: Familiar to AI people. Described as solving search problems.

<!-- skipped some sentences -->

> "It would not necessarily break proof of work."

We'd see a quadratic speedup, not an exponential one.

#### Reasons quantum computing might not take over

TODO: Mine this whole section.

Quantum computers have a lot of overhead. 
- There's lots of complexity involved in maintaining quantum states.
- Making quantum computers work requires quantum error correction, which requires a 1000 real qbits per logical qbit.

> "There's a very real possibility that the overhead of running a quantum computer will be higher than the speedup you get with Grover's"

The other key idea of Bitcoin is public key crytography and the verification process for signatures.

<!--  -->

#### Beautiful Ideas in Ethereum

> Money can emerge out of a database if enough people believe in it. 



Placeholder timestamp for current watch progress: https://youtu.be/3x1b_S6Qp2Q?t=2812



