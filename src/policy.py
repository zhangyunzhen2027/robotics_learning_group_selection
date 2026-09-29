import numpy as np

class LinearPolicy:
    """Provided baseline: least-squares linear behavioral cloning."""
    def __init__(self, X, Y):
        Xb = np.concatenate([X, np.ones((len(X), 1))], axis=1)
        self.W = np.linalg.pinv(Xb) @ Y

    def act(self, obs):
        x = np.concatenate([obs, [1.0]])
        a = x @ self.W
        n = np.linalg.norm(a)
        if n > 1.0:
            a = a / n
        elif n > 1e-8:
            a = a / n
        return a.astype(np.float32)

# Implement StudentPolicy in this file (optional class name if you document it in your report).
# Training data: make_dataset() -> (X, Y), fixed demo budget unless you justify otherwise.
# At runtime, act(obs) receives obs = [target_x - robot_x, target_y - robot_y].
