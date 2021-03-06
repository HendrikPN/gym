#!/usr/bin/env python3
import argparse
import scigym


parser = argparse.ArgumentParser(description='Renders a SciGym environment for quick inspection.')
parser.add_argument('env_id', type=str, help='the ID of the environment to be rendered (e.g. CartPole-v0')
parser.add_argument('--step', type=int, default=1)
args = parser.parse_args()

env = scigym.make(args.env_id)
env.reset()

step = 0
while True:
    if args.step:
        env.step(env.action_space.sample())
    env.render()
    if step % 10 == 0:
        env.reset()
    step += 1
