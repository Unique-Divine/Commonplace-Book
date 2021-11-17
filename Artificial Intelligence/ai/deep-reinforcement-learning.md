# 2. Deep Reinforcement Learning

---

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->


## Getting Started

From Lex Fridman’s intro lecture on deep reinforcement learning
[[video]](https://youtu.be/zR11FLZ-O9M?t=0).

Deep reinforcement learning (RL) is perhaps one of the most exciting fields in artificial intelligence (AI). It marries the beauty and power of deep neural networks to represent and comprehend the world with the ability to act on that understanding. That’s basically what the creation of intelligent beings is. Recent breakthroughs in RL captivate our imagination and inspire us.

RL at high level: An agent has to make a sequence of decisions.

##### Types of Learning:

4 learning domains within machine learning: Supervised, semi-supervised, unsupervised, and reinforcement. People often think that supervised learning is the only domain that requires manual labeling, however in reality, all types of machine learning are "supervised" in some way by a loss function. Every type of machine learning is supervised learning to a degree. These names for the domains tell us about the cost of human labor required to obtain that supervision.

-   Supervised learning: "teach by example"; RL: "teach by experience"

##### RL in humans: 

Humans appear to learn to walk (and do many other activities) through "very few examples" of trial and error. **How** is an open question.
Possible answers:

-   Hardware: 230 million years of bipedal movement data
-   Imitation learning: Observation of other humans walking
-   Algorithms: Better than backpropagation and stochastic gradient descent

Current spot: <https://youtu.be/zR11FLZ-O9M?t=757>

#### 3 Types of RL

There are countless ways to taxonomize all of the reinforcement learning algorithms. At the highest level, there are model-based algos and model-free algos. We generally put algorithms under 3 categories:
model-based, value-based, and policy-based.

##### Model-based: 
-   Learn a model of the world, then plan using the model. As an agent interacts with the environment, it constructs a model for what the dynamics of the world might be.
-   Better sample efficiency. Once you have a model, you can do all kinds of reasoning that doesn’t require experiencing each scenario.
-   In chess and in Go, the model is given to you. The agent knows the rules of the game.

What is meant by “model" is model-based learning?

In this context, a model of the environment would be a function which predicts state transitions and rewards.

AlphaZero is the reinforcement learning algorithm that learned to play Chess and Shogi.

AlphaZero is a famous example of a model-based algorithm.

[[AlphaZero paper, 2017]](https://arxiv.org/pdf/1712.01815.pdf)

Q: If model-based methods are more sample efficient when they work, what is the advantage of model-free methods?

Q-functions are also called action-value functions.

Q: And what’s the difference between action-value function and state-value function?  
A: The state-value function returns the value of achieving a certain state, whereas the action-value function returns the value for choosing an
action in a state.

Q: Why are Q-functions sometimes called action-value functions?  
A: Because the Q-function gives us the value for taking an action in some state.

Note that, as of 2018, model-free methods are more popular and have been
more extensively developed and tested than model-based methods.

##### Value-based: 

-   Learn the state or state-action value. Value-based methods look to estimate the quality of states and the possible actions performed in them. This quality of the state is then used to pick a “best” action.

-   Act by choosing the best action in a state. This is considered indirect learning of a “policy”.

##### Policy-based: 

- Learn the stochastic policy function that maps state to action.
- Directly learn a policy function. In other words, take as input the representation (or representation of that world) and output an action. This action will be stochastic.
- Act by sampling policy.
- Exploration is baked in. Why? The output action is stochastic, meaning it’s a r.v.

Great resource for learning about deep reinforcement learning: Open AI Spinning Up [[link]](https://spinningup.openai.com/en/latest/user/introduction.html)

![](img/rl_algos_taxonomies.png)

### Review Paper: 

Deep learning is enabling reinforcement learning (RL) to scale to problems that were previously intractable, such as learning to play video games directly from pixels. Deep reinforcement learning algorithms are also applied to robotics, allowing control policies for robots to eb learned directly from camera inputs in the real world.

**Topics covered**: Value-based methods, policy-based methods, central algorithms in deep reinforcement learning such as the deep Q-network, trust region policy optimisation, and asnchronous advantage actor-critic. Conclude with several current areas of research within the field.

Primary goal of the field of artificial intelligence (AI) is to produce fully autonomous agents that interact with their environments to learn optimal behaviours, improving over time through trial and error. Reinforcement learning is a principled mathematical framework for experience-driven autonomous learning. RL is a general way of approaching optimisation problems by trial and error.

The most important property of deep learning is that deep neural networks can automatically find compact low-dimensional representations (features) of high-dimensional data (e.g., images, text and audio)

the use of deep learning algorithms within RL defining the field of “deep reinforcement learning” (DRL)

For a more comprehensive survey of recent efforts in DRL, including applications of DRL to areas such as natural language processing, we refer readers to the overview by Li.

The first, kickstarting the revolution in DRL, was the development of an algorithm that could learn to play a range of Atari 2600 video games at a superhuman level, directly from image pixels. Providing solutions for the instability of function approximation techniques in RL, this work was the first to convincingly demonstrate that RL agents could be trained on raw, high-dimensional observations, solely based on a reward signal. The second standout success was the development of a hybrid DRL system, AlphaGo, that defeated a human world champion in Go, paralleling the historic achievement of IBM’s Deep Blue in chess two decades earlier and IBM’s Watson DeepQA system that beat the best human Jeopardy! players .

AlphaGo was composed of neural networks that were trained using supervised and reinforcement learning, in combination with a traditional heuristic search algorithm

In a step towards even more capable agents, DRL has been used to create agents that can meta-learn (“learn to learn”), allowing them to generalise to complex visual environments they have never seen before

One of the driving forces behind DRL is the vision of creating systems that are capable of learning how to adapt in the real world.

---

## On Policy Algorithms

### Vanilla Policy Gradient (VPG)

Goal: Learn a distribution of action probabilities where each probability reflects how likely an action is to yield high rewards. Naturally, actions that lead to lower rewards have lower probabilites. Train in this manner until an optimal policy is reached. 

Policy gradient methods produce **stochastic policy**, $\pi_w$, which outputs a probability distribution. This policy is described as being the agent's brain. 
- Here, the $w$ in $\pi_w$ denotes the parameters, or weights and biases, of a neural network module. 

Let $\mathcal{A} = \{a_t\}$ denote the space of possible actions and $\mathcal{S} =\{s_t\}$ the space of states. A stochastic policy gradient approach essentially models $a_t \sim \pi_w(s_t)$, meaning that actions are sampled from the policy distribution.  

How do we train and optimize this policy, $\pi_w(s)$?

Learn a state value function $V_{\pi_w}(s) = \mathbb{E}_{\tau\sim\pi}[R(\tau) | s ]$, where
- $\tau$ is a trajectory, a sequence of state-action pairs.
- $R(\tau)$ is a reward function. A reward function accepts a state or sequence of states (i.e., a trajectory) and outputs a reward value. If the trajectories in an environment cannot be described only by states, they are instead defined as sequences of state-action pairs, in which case the reward function accepts a state-action pair of sequence of such pairs and outputs a reward value.

To state the equation, $V_{\pi_w}(s) = \mathbb{E}_{\tau\sim\pi}[R(\tau) | s ],$ in words, the value of state $s$, $V_{\pi_w}(s)$, is taken to be the expected rewards for acting in accordance with policy $\pi_w$ in state $s$ along trajectory $\tau$.

VPG is an on-policy algorithm.  

#### VPG Implementation
Let's assume you are using a simple mlp for the policy gradient, $\pi_w$.
```python
class PolicyNetwork(nn.Module):
    def __init__(self, in_dim: int, n_actions: int, hidden_dim: int = 50):
        super().__init__()
        self.mlp = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.LeakyReLU(),
            nn.Linear(hidden_dim, n_actions))

    def forward(self, x):
        return self.mlp(x)
```


##### References
- Open AI Spinning Up. Vanilla Policy Gradient. [[web]](https://spinningup.openai.com/en/latest/algorithms/vpg.html)

---

## Mine (Deep RL)

#### [Q-learning](https://en.wikipedia.org/wiki/Q-learning)

Q-learning is a model-free RL algorithm.

Q-learning gets is name because the agent learns the quality of actions
to know how to act.

In Q-learning, "Q" function is computed to maximize expected rewards for
an action taken in a given state.

"Model-free" means that an agent does not require a model of the
environment.

For set of states $S$ and set of actions $A$, the Q-function is a map
s.t. $Q : S \times A \to \mathbb{R}$.

In Q-learning, *Q* is updated according to
$$Q_{\text{new}}(s, a) := Q(s, a) 
		+ \alpha \cdot 
			\left( r + \gamma \max_{a_b\in A} Q(s', a_b) 
			- Q(s, a) \right).  $$
-   $Q(s, a)$: The "quality" fn. at the current state *s*
-   $\alpha$: The learning rate. $0 \leq \alpha \leq 1$. Values close to 1 make faster changes to $Q$.  
-   $r$: Reward received when moving from $s \to s'$
-   $γ$: The discount factor. Quantifies how much to "discount" the ...
- $\max_{a_b\in A} Q(s', a_b)$: Estimate of optimal future Q-value. This would be the highest $Q(s'|a_b)$, where $a_b$ is the "best" action and $s'$ is the next state.


#### Collection of Refs

Deep Attention Recurrent Q-Network. 2015.

<https://causalai.net/r26.pdf>

[Papers with Code -
RL](https://paperswithcode.com/methods/area/reinforcement-learning)

[Papers with Code - Representation
Learning](https://paperswithcode.com/task/representation-learning)

[ Near-Optimal Representation Learning for Hierarchical Reinforcement
Learning](https://paperswithcode.com/paper/near-optimal-representation-learning-for)

[Mastering Atari, Go, Chess and Shogi by Planning with a Learned Model,
2020](https://arxiv.org/pdf/1911.08265.pdf)

"... deep RL algorithm based on the maximum entropy reinforcement
learning framework. In this framework, the actor aims to maximize
expected reward while also maximizing entropy. That is, to succeed at
the task while acting as randomly as possible" - [Soft Actor-Critic:
Off-Policy Maximum Entropy Deep RL w/ a Stochastic
Actor](https://arxiv.org/pdf/1801.01290.pdf)
