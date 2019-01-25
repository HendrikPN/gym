# Agents

An "agent" describes the method of running an RL algorithm against an environment in the scigym. The agent may contain the algorithm itself or simply provide an integration between an algorithm and the scigym environments.

## RandomAgent

A sample agent located in this repo at `scigym/examples/agents/random_agent.py`. This simple agent leverages the environments ability to produce a random valid action and does so for each step.  

## cem.py

A generic Cross-Entropy agent located in this repo at `scigym/examples/agents/cem.py`. This agent defaults to 10 iterations of 25 episodes considering the top 20% "elite".
