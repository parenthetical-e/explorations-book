import numpy as np
import cloudpickle

from collections import defaultdict

from explorationlib.util import save


def experiment(name, agent, env, num_steps=1, num_repeats=1, seed=None):
    """Run an experiment. 
    
    Note: the experiment log gets saved to 'name'. 
    """

    # Create a log
    log = defaultdict(list)

    # Seed
    agent.seed(seed)
    env.seed(seed)

    # !
    for k in range(num_repeats):
        # Reset
        agent.reset()
        state, reward, done, _ = env.reset()

        # Log start
        log["step"].append(0)
        log["repeat"].append(k)
        log["state"].append(state)
        log["action"].append(None)
        log["reward"].append(reward)
        log["info"].append(info)

        # Run episode, for at most num_steps
        for n in range(1, num_steps + 1):
            # Step
            action = agent(state)
            env.step(action)
            state, reward, done, info = env.last()

            # Log step
            log["step"].append(n)
            log["repeat"].append(k)
            log["state"].append(state)
            log["action"].append(action)
            log["reward"].append(reward)
            log["info"].append(info)

            if done:
                break

    # Save the results
    log["env"] = env
    log["agent"] = agent
    save(name, log)


def multi_experiment(name, agents, env, num_episodes=1, seed=None):
    """Run an experiment, with multiple agents. 
    
    Note: the experiment log gets saved to 'name'. 
    """

    raise NotImplementedError("TODO")