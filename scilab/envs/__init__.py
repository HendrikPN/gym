from scigym.envs.registration import registry, register, make, spec


# Quantum Physics
# ----------------------------------------

register(
    id='Inverse_CartPole-v0',
    entry_point='scigym.envs.quantum_physics:InverseCartPoleEnv',
)


# Algorithmic
# ----------------------------------------

register(
    id='Copy-v0',
    entry_point='scigym.envs.algorithmic:CopyEnv',
    max_episode_steps=200,
    reward_threshold=25.0,
)

register(
    id='RepeatCopy-v0',
    entry_point='scigym.envs.algorithmic:RepeatCopyEnv',
    max_episode_steps=200,
    reward_threshold=75.0,
)

register(
    id='ReversedAddition-v0',
    entry_point='scigym.envs.algorithmic:ReversedAdditionEnv',
    kwargs={'rows' : 2},
    max_episode_steps=200,
    reward_threshold=25.0,
)

register(
    id='ReversedAddition3-v0',
    entry_point='scigym.envs.algorithmic:ReversedAdditionEnv',
    kwargs={'rows' : 3},
    max_episode_steps=200,
    reward_threshold=25.0,
)

register(
    id='DuplicatedInput-v0',
    entry_point='scigym.envs.algorithmic:DuplicatedInputEnv',
    max_episode_steps=200,
    reward_threshold=9.0,
)

register(
    id='Reverse-v0',
    entry_point='scigym.envs.algorithmic:ReverseEnv',
    max_episode_steps=200,
    reward_threshold=25.0,
)

# Classic
# ----------------------------------------

register(
    id='CartPole-v0',
    entry_point='scigym.envs.classic_control:CartPoleEnv',
    max_episode_steps=200,
    reward_threshold=195.0,
)

register(
    id='CartPole-v1',
    entry_point='scigym.envs.classic_control:CartPoleEnv',
    max_episode_steps=500,
    reward_threshold=475.0,
)

register(
    id='MountainCar-v0',
    entry_point='scigym.envs.classic_control:MountainCarEnv',
    max_episode_steps=200,
    reward_threshold=-110.0,
)

register(
    id='MountainCarContinuous-v0',
    entry_point='scigym.envs.classic_control:Continuous_MountainCarEnv',
    max_episode_steps=999,
    reward_threshold=90.0,
)

register(
    id='Pendulum-v0',
    entry_point='scigym.envs.classic_control:PendulumEnv',
    max_episode_steps=200,
)

register(
    id='Acrobot-v1',
    entry_point='scigym.envs.classic_control:AcrobotEnv',
    max_episode_steps=500,
)

# Toy Text
# ----------------------------------------

register(
    id='Blackjack-v0',
    entry_point='scigym.envs.toy_text:BlackjackEnv',
)

register(
    id='KellyCoinflip-v0',
    entry_point='scigym.envs.toy_text:KellyCoinflipEnv',
    reward_threshold=246.61,
)
register(
    id='KellyCoinflipGeneralized-v0',
    entry_point='scigym.envs.toy_text:KellyCoinflipGeneralizedEnv',
)

register(
    id='FrozenLake-v0',
    entry_point='scigym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '4x4'},
    max_episode_steps=100,
    reward_threshold=0.78, # optimum = .8196
)

register(
    id='FrozenLake8x8-v0',
    entry_point='scigym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '8x8'},
    max_episode_steps=200,
    reward_threshold=0.99, # optimum = 1
)

register(
    id='CliffWalking-v0',
    entry_point='scigym.envs.toy_text:CliffWalkingEnv',
)

register(
    id='NChain-v0',
    entry_point='scigym.envs.toy_text:NChainEnv',
    max_episode_steps=1000,
)

register(
    id='Roulette-v0',
    entry_point='scigym.envs.toy_text:RouletteEnv',
    max_episode_steps=100,
)

register(
    id='Taxi-v2',
    entry_point='scigym.envs.toy_text.taxi:TaxiEnv',
    reward_threshold=8, # optimum = 8.46
    max_episode_steps=200,
)

register(
    id='GuessingGame-v0',
    entry_point='scigym.envs.toy_text.guessing_game:GuessingGame',
    max_episode_steps=200,
)

register(
    id='HotterColder-v0',
    entry_point='scigym.envs.toy_text.hotter_colder:HotterColder',
    max_episode_steps=200,
)

# Unit test
# ---------

register(
    id='CubeCrash-v0',
    entry_point='scigym.envs.unittest:CubeCrash',
    reward_threshold=0.9,
    )
register(
    id='CubeCrashSparse-v0',
    entry_point='scigym.envs.unittest:CubeCrashSparse',
    reward_threshold=0.9,
    )
register(
    id='CubeCrashScreenBecomesBlack-v0',
    entry_point='scigym.envs.unittest:CubeCrashScreenBecomesBlack',
    reward_threshold=0.9,
    )

register(
    id='MemorizeDigits-v0',
    entry_point='scigym.envs.unittest:MemorizeDigits',
    reward_threshold=20,
    )

