import gym

if __name__ == "__main__":
    env = gym.make("FrozenLake-v0")
    observation = env.reset()

    for i in range(10):
        env.render()