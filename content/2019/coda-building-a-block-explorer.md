Title: Weekend Project - Coda Blockchain Visualization
Date: 2019-09-14
Author: Conner Swann
Slug: weekend-project-coda-blockchain
Category: Coda Protocol
Tags: Javascript, React, Coda, Blockchain, Block Explorer
Cover: /images/2019/coda-cover.jpeg
Status: draft

# What's Coda?

Coda is a Crypto Protocol that I am working on as part of the O(1) Labs Team. Coda implements a "succinct" blockchain that effectively "[swaps the traditional blockchain for a tiny cryptographic proof.](https://codaprotocol.com/)" Practically, this means that by default once a transition *(a.k.a. block)* with transactions is "swapped" for a proof, it gets thrown out to save disk space. 

The protocol is stil very much in active development, and there are regular [Testnets](https://codaprotocol.com/docs/coda-testnet/) that are designed to help us surface bugs and teach the community how to operate Coda Nodes. 

# The Problem 

When I decided to sit down and get my roommate [@reem](https://github.com/reem) to help me with this visualization, it was to try and solve one particular issue I'd been having. *There wasn't a way to at-a-glance verify that the network was forked!*

Fortunately, John Wu ([@wu-s-john](https://github.com/wu-s-john)), one of the protocol developers, had just implemented basic block archive functionality that allows a node to store all blocks that it observes, along with all the associated metadata. With this data, I figured we could build a nice visualization of the chain and any forks. 

# The Visualization

The blockchain visualization is implemented with using React, the Apollo GraphQL Client, and [React-Vis-Force](https://github.com/uber/react-vis-force) a library for building D3-based force-directed graphs. Since I had used this kind of graphs in the past, I decided to opt to stick with something I was comfortable with -- as I will mention later, this might not have been the best approach. 

A graph from a previous project:
![Social Media Graph]({attach}/images/2019/weekend-project-1-facebook-graph.png)


This is an animated gif of the visualization with roughly 400 blocks depicted. 
![Chain Visualization Gif]({attach}/images/2019/weekend-project-1-chain-visualization.gif)


# Next Steps / Lessons Learned

There's a bunch of stuff I would have done differently, had I been designing this for deployment in a production setting: 
- React-Vis-Force doesn't allow you to dynamically add and remove nodes in the graph without reloading the whole thing. To accomplish this, I'd have to fork their library or craft my own D3-based react components. 
- The `blocks` query in the Coda Daemon's GraphQL endponint doesn't *actually* support pagination at the time of writing, so loading the page gets slow as nBlocks increases. Though, even if it did support pagination, you'd still have to load all the blocks first due to #1. 
- When there's a lot of nodes on the graph, it takes a really long time to work all the crossings out. I wished there was a way I could have laid out the nodes from left-right/top-bottom by their timestamp at render time. 
- The Archive node's endpoint is *dangerous* in that there is no authentication, so anyone with access could change the Daemon's internal state. As such, this only works when running a Daemon on the same machine as the visualization. I would love to build out a GraphQL Proxy of some kind in order to mitigate this risk. 
- I did implement basic "block explorer" functionality, in that if you select a node a `div` appears with the json data from the block. I would have liked to spend more time displaying this data on the graph itself, via colors or otherwise. 
- I would love to mess with different colorings on the graph *way* more than I did here. This visualization can be super useful for visually debugging the blockchain by coloring the blocks based on number of transactions, snark jobs, fee transfers, etc. 

### Examples of Different Coloring: 

Red -> Main Chain / Blue -> Leaf Nodes: 
![colored-by-leaves]({attach}/images/2019/weekend-project-1-chain-vis-red-blue.png)

Black -> No Txs / Redder -> More Txs
![colored-by-transactions]({attach}/images/2019/weekend-project-1-chain-vis-red-black.png)

# Think You Can Do Better? 

I am confident that there are people out there who are better at Javascript than I am. The project is licensed under the [Apache License 2.0](https://github.com/yourbuddyconner/coda-chain-visualization/blob/master/license), which is a perissive license that allows for derivative works! Please, if you decide to make something cool with this please let me know on [Twitter](https://twitter.com/yourbuddyconner)!