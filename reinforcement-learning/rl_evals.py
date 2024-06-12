state = env.reset()
total_reward = 0
for _ in range(100):
    action = trainer.compute_action(state)
    state, reward, done, _ = env.step(action)
    total_reward += reward
    if done:
        break
print(f"Total Reward during evaluation: {total_reward}")