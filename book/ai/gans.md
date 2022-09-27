# gans

- [gans](#gans)
    - [Vanilla GANs](#vanilla-gans)

### Vanilla GANs 

#### Abstract & Introduction

##### Abstract: 

Goodfellow et al. propose a new framework for estimating generative models via an adversarial process, in which two models are simultaneously trained:

-   $G$: a generative model that captures the data distribution, and
-   $D$: a discriminative model that estimates the probability that a sample came from the training data rather than *G*

The training procedure for $G$ is to maximize the probability of $D$ making a mistake. This framework corresponds to a minimax two-player game. In the space of arbitrary functions $G$ and $D$, a unique solution exists, with $G$ recovering the training data distribution and $D$ equal to $\frac{1}{2}$ everywhere. In the case where $G$ and $D$ are defined by multilayer perceptrons, the entire system can be trained with backpropagation. There is no need for any Markov chains or unrolled approximate inference networks during either training or generation of
samples.

##### Introduction: 

In the proposed adversarial nets framework, the generative model is pitted against an adversary: a discriminative model that learns to determine whether a sample is from the model distribution or the data distribution.

**Counterfeiters Analogy:** The generative model can be thought of as analogous to a team of counterfeiters, trying to produce fake currency and use it without detection, while the discriminative model is analogous to the police, trying to detect the counterfeit currency. Competition in this game drives both teams to improve their methods until the counterfeits are indistiguishable from the genuine articles.

In this article, we explore the special case when the generative model generates samples by passing random noise through a multilayer perceptron, and the discriminative model is also a multilayer perceptron. We refer to this special case as adversarial nets. In this case, we can **train both models using only the highly successful backpropagation and dropout algorithms** and sample from the generative model using only forward propagation.

#### Adversarial Net Algorithm

The adversarial modeling framework is most straightforward to apply when the models are both multilayer perceptrons. To learn the generator’s distribution $p_g$ over data $x$, $p_g(\bm{x})$, we define a prior on input noise variables, $p_z(\bm{z})$, then represent a mapping to data space as $G(\bm{z}|\theta_g)$, where $G$ is a differentiable function represented by a multilayer perceptron with parameters $\theta_g$. We also define a second multilayer perceptron $D(\bm{x}|\theta_d)$ that outputs a single scalar. $D(\bm{x})$ represents the probability that $\bm{x}$ came from the data rather than $p_g$. We train $D$ to maximize the probability of assigning the correct label to both training examples and samples from $G$. We simultaneously train $G$ to minimize $\log (1 − D(G(\bm{z}))$ . In other words, $D$ and $G$ play the following two-player minimax game with value function, 
$$\begin{align*} 
&V(G, D): \min_G \max_D V(D,  G) \\
&= \mathbb{E}_{\bm{x} \sim p_{\text{data}}(\bm{x}) } 
  [\log D (\bm{x}) ] 
  + \mathbb{E}_{\bm{x} \sim p_{\bm{z}} (\bm{z}) } 
  [ \log (1 − D(G(\bm{z})))
\end{align*}$$.

Goodfellow et al. present a theoretical analysis of adversarial nets, essentially showing that the training criterion allows one to recover the data generating distribution as $G$ and $D$ are given enough capacity, i.e., in the non-parametric limit.

Figure 1 explains this approach: GANs are trained by simultaneously updating the discriminative distribution, $D$, so that it discriminates between samples from the data generating distribution, $p_{\bm{x}}$, and those of the generative distribution $p_g(G)$.

After several steps of training, if $G$ and $D$ have enough capacity, they will reach a point at which both cannot improve because $p_g = p_{\text{data}}$. The discriminator is unable to differentiate b/w the two distributions, i.e. $D(\bm{x})=\frac{1}{2}$.

![](img/GANsAlgo1.png)

Note: 
- $k$ = 1 was used in the experiments.
- Momentum was the gradient-based learning rule used in the experiments.

#### Related Work

The adversarial nets framework does not require a Markov chain for
sampling. Because adversarial nets do not require feedback loops during
generation, they are better able to leverage piece-wise linear units
\[19, 9, 10\], which improve the performance of backpropagation but have
problems with unbounded activation when used in a feedback loop.
