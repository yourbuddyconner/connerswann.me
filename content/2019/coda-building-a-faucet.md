Title: Weekend Project - Coda Faucet Bot
Date: 2019-09-14
Author: Conner Swann
Slug: weekend-project-coda-faucet
Category: Coda Protocol
Tags: Python, React, Coda, Blockchain, Discord Bot
Cover: images/2019/coda-cover.jpg
Status: draft

# What's Coda?

Coda is a Crypto Protocol that I am working on as part of the O(1) Labs Team. Coda implements a "succinct" blockchain that effectively "[swaps the traditional blockchain for a tiny cryptographic proof.](https://codaprotocol.com/)" 

Practically, this means that in the average Coda node, once a transition *(a.k.a. block)* with transactions is "swapped" for a proof, it gets thrown out to save disk space. 

# The Problem

When one builds a blockchain testnet, the first thing you're going to want to do is send tokens to people to test out functionality. Without a dedicated faucet service, you'd have to manually issue transactions so the need is obvious.

# The Python Client

In the spirit of "**D**on't **R**epeat **Y**ourself" I opted to start this project by writing a quick wrapper around the Coda Daemon's GraphQL Endpoint. It provides a nice clean API that abstracts away the GraphQL calls, leaving synchronous queries and mutations as simple function calls that return `dict` objects. 

The GraphQL subscriptions are exposed via [Asyncio](https://docs.python.org/3/library/asyncio.html) coroutines, and are simple to program with in an event-driven manner.

# The Bot

The main meeting spot online for the Coda Community is the official [Coda Discord Server](https://bit.ly/CodaDiscord), so it was an easy decision to write a Discord bot that would enable community members to get testnet tokens on-demand! 

 My goals for the bot were the following: 

 - Automate the sending of Coda testnet tokens.
 - Prevent people from requesting a bunch of tokens. 
 - Allow server mods to make unlimited requests. 
 - Get live metrics from the bot about its operations.

Since I enjoy a little bit of personality in my bots, I decided that he'd be called "The Grumpus" and would embody this picture of this grumpy shiba I found on the internet: 

![Doggo](/../images/2019/coda-discord-bot-grumpus.jpg)

In keeping with the Python theme, I decided to build the bot using the [DiscordPy](https://discordpy.readthedocs.io/en/latest/quickstart.html) framework. The library is event-driven and makes it simple to create a Discord bot with a couple functions. 

I also wanted to expose [Prometheus](https://prometheus.io/) metrics, which is easy to do with the official [Prometheus Python Library](https://github.com/prometheus/client_python).


  
