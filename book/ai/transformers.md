# Transformers

The Transformer is revolutionary and disruptive. It is one of the most influential breakthroughs in AI in the past decade as Transformers have pushed or approached the state-of-the-art (SOTA) in almost every area of deep learning, leaving recurrent neural networks (RNNs) and convolutional neural networks (ConvNets) behind.

The Transformer architecture was introduced in "[Attention is All You Need](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)". This paper presented improvements to soft attention and made it possible to do sequence to sequence (seq2seq) modeling without the use of RNNs. The Transformer is entirely built on self-attention mechanisms (1.1).

Papers to mine:

* Rethinking Attention with Performers. Choromanski et al. 2021. [[paper]](https://arxiv.org/pdf/2009.14794.pdf)
  * Tags: transformer, efficient transformer
  * Affiliations: Google Brain

--- 

### 1.1 Vanilla Transformer Architecture

The Vanilla Transformer was created by a research team at Google AI in "Attention if All You Need" ([Vaswani et al., 2017](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)). The Vanilla Transformer was originally used for machine translation and consists of an encoder-decoder structure.

The Transformer encoder and decoder are actually stacks of layers. The encoder is a stack of encoder layers and the decoder is a stack of decoder layers. This diagram shows an example of one encoder layer and one decoder layer.

![](img/vanilla-transformer-encoder-decoder.png)

Encoder: Takes in a sequence, $\bm{x}$, and generates an a sequence of continuous representation vectors, $\bm{z}\_{enc}$. These representations are then used as input for the decoder.

Decoder: Takes the sequence of representations, $\bm{z}\_{enc}$, created by the encoder and generates a new output sequence, $\bm{y}$.

Note that $\bm{x} = (x\_1, \ldots, x\_n)$ and $\bm{z} = (z\_1, \ldots, z\_n)$ must be equidimensional, whereas $\bm{y} = (y\_1, \ldots, y\_m)$ can have a different dimension. In the context of machine translation, this says that an input sentence represented by $\bm{x}$ with length $n$ may translate to an output sentence represented by $\bm{y}$ with length $m$ and $n$ doesn't necessarily equal $m$.

#### 1.1.1 Input Embeddings and the Encoder Stack

A single encoder layer is composed of two main blocks, the multi-head attention block and a feed-forward block. Before a sequence can be passed into encoder stack, it has to be embedded and given positional encodings/embeddings. Here, embedding a sequence means converting each element of the sequence into a vector representation.

**Sequence transduction models**

What is transduction?

> transduce: to convert (something, such as energy or a message) into another form. "Essentially, sense organs transduce physical energy into a nervous signal." - [Merriam-Webster Dictionary](https://www.merriam-webster.com/dictionary/transduce) (online).

Thus, it's safe to assume that sequence transduction models are loosely defined as models that convert a sequence into another form. Here are some examples of transduction models (mostly from NLP).

* Transliteration: Generating words in a target form given examples in a source form.
* Spelling Correction: Predicting correct word spelling (sequence of letters) given incorrect word spelling (sequence of letters).
* Machine Translation: Generating sentences in a target language (sequences of words) given sentences in a source language.
* Speech Recognition: Predicting sequences of text given sequences of audio.
* Protein Secondary Structure Prediction: Generating 3D structure of protein given sequences of amino acids.
* Text-to-Speech, or speech synthesis: Generating audio given text sequences.
* Signal processing transduction: Generating electrical energy within a system given an audio signal (sound waves). This is done by a transducer.

Transduction is closely related to the concepts of deductive and inductive reasoning. **Deductive reasoning** is taking a general theory to make a claim about specific observations, whereas inductive reasoning is taking specific observations to form a general theory.

Ex. When my niece, Kambri, was 4 years old, she noticed that most adults she came across existed in mom-dad pairs. She'd met my girlfriend at the time and, when eating the French toast sticks and eggs we made her for breakfast, she asked, "Uncle 'Nique, are you a daddy too?" Her thought process: Uncle Unique is an adult, male, and has a female companion. Therefore, he's probably a daddy. This is an example of deductive reasoning because my niece was confirming her theory about moms and dads with a specific observation (me).

In machine learning, logic, and statistical inference, **transduction is the combination of induction and deduction to go from specific training observations to specific test observations**. Consider machine translation. English sentence → model → Spanish sentence. Here, the model acts as the "general theory".

**Handling sequences of varied length**

You wonder how sequences of different length are handled as inputs to the Transformer. Sometimes, people go as far as saying that "Transformers can handle inputs of arbitrary length", which is false, or at least, incomplete. What people mean to say is that **Transformers can handle inputs of arbitrary length up to some maximum length threshold**. But how?

> "Attention mechanisms have become an integral part of compelling sequence modeling, allowing modeling of dependencies without regard to their distance in the input or output sequences." - Vaswani et al., 2017

* [ ] Q: How can dependencies in the sequence ignore distance?

Just as in other sequence transduction models, the Transformer uses learned embeddings. These learned embeddings convert input tokens and output tokens into vectors of dimension $d\_{\text{model}}$.

**Input embeddings**

***

#### 1.1.2 Why use Transformers over RNNs?

* [ ] Q: If the vanilla Transformer is an encoder-decoder architecture why use it instead of the RNN based encoder-decoder?

RNN models have several problems. They are slow to train and cannot deal with long sequences. An RNN encoder-decoder

* [ ] Q: Why are RNNs slow?
* [ ] Q: Why can't RNNs deal with long sequences?

RNNs need data to be processed sequentially. A more precise way of saying this is, the elements of a given input vector must be processed in sequential order rather than in parallel. That's a big problem. This recurrent process doesn't make efficient use of modern GPUs and TPUs, which are designed for parallel computation.

> "RNNs are so slow that truncated backpropagation was introduced to limit the number of timesteps in the backward pass, estimating gradients to update the weights rather an doing backpropagation fully." - Jingles (Hong Jing)

Long-term dependency problems in RNNs

One reason that RNNs can't handle long sequences is that the have vanishing or exploding gradients if the input sequence gets too long. This can result in NaNs (Not a Number) popping up in the losses in the training process. Long Short-Term Memory (LSTM) networks were introduced in 1997 (Hochreiter and Schmidhuber) to address these problems. LSTMs have improved memory and can handle longer sequences than traditional RNNs, however they are even slower to train.

In RNNs, each hidden state $h\_i$ has dependencies on the previous hidden state $h\_{i-1}$. Consequently, the embeddings made by the encoder must be computed one at a time. Transformers have no concept of a time step. **An entire input sequence is passed into a Transformer encoder in parallel**, and the "time step" information is integrated via position embeddings.

Transformer Encoder

```python
# Ex. Transformer Encoder (conceptual pseudo code)
sentence = get_input_sentence() # Input an English sentence.
for word_idx, word in enumerate(sentence): 
    # This part is written as a loop for clarity, but it's typically in parallel
    semantic_vec = compute_embedding(word)
    position_embedding = encode_position(position = word_idx)
    word_representation = semantic_vec + position_embedding
```

1. Input an English sentence.
2. Each word in the sentence is converted into an embedding to represent meaning/semantics called a context vector.
3. Add a position embedding to the context vector of each word in the sentence.

**References**

* Illustrated Guide to Transformer: A component by component breakdown analysis. [[article]](https://jinglescode.github.io/2020/05/27/illustrated-guide-transformer/)

***

#### 1.1.3 Positional embeddings

positional embedding is synonymous with positional encoding

Transformers proven to work well on any kind of data, especially when there is a large amount of data to train on with self-supervision. Transformers do not process inputs sequentially but all at one time (in parallel). For each element of the input, information is combined from the other elements through self-attention. Each element does this aggregation on its own independently of what the other elements do. The transformer architecture does not model the order of the input anywhere. Thus, positional information in the input sequence must be explicitly encoded.

Positional embeddings are identifiers or hints that tell the Transformer where an element of the input lies within the sequence. These positional embeddings are then added to the original vector representation of the input sequence. Positional embeddings are order, or position, vectors added to vectors for the Transformers to know the order of the sequence.

Positional embeddings requirements:

1. Every position must have the same identifier regardless of the length of the input sequence length or what the input is. I.e., swapping out sequence should not change the positional embedding vector.
2. The values of a positional embedding should not be too large, or they will push vectors into super distinct subspaces, where the positional similarity is too powerful for semantic similarity to take effect in the vector space.

In "Attention is All You Need", the choice of positional embeddings was not obvious. We'll discuss simple examples.

1. Let's say we have an input sequence $x$. Why not use integer encodings for each element of $x$, i.e. a linear function? These integer values are too large. People tend to aim for keeping the values in a positional embedding between 0 and 1.
2. What about a sigmoid? It's bounded between 0 and 1 and can handle values that are infinitely large. → We also want variability in the positional embeddings. The sigmoid doesn't differentiate values that are extremely positive or extremely negative because it's asymptotic at the ends. An example of a function that has some variability and still accepts all reals would be sine and cosine.

What are some issues with sine and cosine? These functions are periodic, meaning that we'll see the same positional embedding at different values. What's a possible solution? Use such a low frequency for the trig functions such that, even for the longest sequence lengths, our function will not repeat. This solves some of the aforementioned problems, but it's still not optimal because:

* the positional embeddings must push far enough in the vector space to make reasonable clusters, but they also shouldn't push too far or their signal will outshine that of the semantic information. Distances between points in the representation space should not be dominated by either positional or semantic information. What's the solution here? → Herein lies using the alternating sine and cosines with increasing frequency.
* (Video notes in progress)

Date: 21年8月1日

***

#### 1.1.4 Self-attention

Self-attention is when a model makes predictions for each part of an input sample using other parts the same sample. A self-attention module returns the same number of outputs as inputs it receives.

All Transformer-based architectures rely on self-attention.

Broad categories of attention:

* [ ] **Self-attention** relates different positions of the same input sequence. Self-attention is also referred to as intra-attention.
* [ ] **Soft attention** is when a model attends to the entire input state space. Soft attention is a.k.a. global attention.
* [ ] **Hard attention** is when a model attends to part of the input state space, i.e. a patch of an input image or a chunk of an input sequence. Hard attention is a.k.a. local attention.
* [ ] Q: What makes it self-attention as opposed to just attention?

Each layer of a neural network has inputs, potential activations, and outputs. RNNs additionally have states of the layers. When an attention mechanism is used, a model takes input from the activations or states of some layer. If this layer that the inputs are taken from is the same layer that the attention mechanism is applied to, this process is called **self-attention** because a layer is attending to itself.

Ex. Each word in a sequence attends to every other word in the same sequence. Self-attention captures the relationship between words in the sequence.

Attention is often applied to transfer information from encoder to decoder, meaning that the decoder neurons receive input from the encoder states/outputs. This would not be self-attention because two different components (encoder and decoder) are connected. Self attention is applied within one component.

Ex. In the BERT architecture, there is no decoder, only self-attention within the encoder.

Ex. Self-attention (**intra-attention**) models dependencies between different parts of a sequence. To use a previous example, we could try to get the semantic relationship between words in a sentence. Non-self-attention (**inter-attention**) models could look at dependencies between different sequences, such as those between a text and its translation to another language. Note however that self-attention is also extremely effective at translation tasks (hence Transformers).

Ex. Inter-attention can quantify dependencies between an image and its description.

* [ ] How does self-attention work?

**Alignment Score Functions**

Each type of attention has an alignment score function. Some examples of alignment score functions are content-base, additive, location-based, general, dot-product, and scaled dot-product.

Alignment score functions dictate how inputs are multiplied and added together to get the attention score. They do not dictate whether the mechanism is self-attention or inter-attention.

* [ ] Q:

Neural Machine Translation by Jointly Learning to Align and Translate. Badhanau, Cho, and Bengio. 2016. [[paper]](https://arxiv.org/pdf/1409.0473.pdf)

* [ ] Q: What is machine translation?
* [ ] Q: What makes neural machine translation neural?

**Types of alignment score functions**

* [ ] Q: Why use scaled dot-product attention instead of regular dot-product attention? A: Multiplying by a scaling factor of $\frac{1}{\sqrt{n}}$ helps deal with problem that, when the input is large, the softmax function may have an extremely small gradient, leading to inefficient learning.

***

#### 1.1.5 Multi-Head Attention

***

**1.1 References**

Transformers

* Attention is All You Need. Vaswani et al. 2017. [[paper]](https://proceedings.neurips.cc/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf)
* Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2018). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. arXiv preprint arXiv:1810.04805. [[paper]](https://arxiv.org/pdf/1810.04805.pdf)
* Adalogou, Nikolas. (2021). Transformers in Computer Vision. AI Summer. [\[github-repo\]](https://github.com/The-AI-Summer/self-attention-cv)

Input Embeddings

* Alammar, Jay. (2019). The Illustrated Word 2 Vec. [[blog]](https://jalammar.github.io/illustrated-word2vec/)
* Tsu. (2020). [[Artificial Intelligence Stack Exchange]](https://ai.stackexchange.com/questions/22957/how-can-transformers-handle-arbitrary-length-input)

Sequence Transduction Models

* Transduction (machine learning). [Wikipedia](https://en.wikipedia.org/wiki/Transduction\_\(machine\_learning\)).
* Gentle Introduction to Transduction in Machine Learning. Brownlee. 2017. [\[article\]](https://machinelearningmastery.com/transduction-in-machine-learning/)

Positional Embeddings

* Adalogou, Nikolas. (2021). How Positional Embeddings work in Self-Attention (code in PyTorch). AI Summer. [\[blog\]](https://theaisummer.com/positional-embeddings/)
* Parcalabescu, Letitia. (2021). Positional embeddings in transformers EXPLAINED | Demystifying positional encodings. AI Coffee Break with Letita. [\[video\]](https://youtu.be/1biZfFLPRSY)
* Parcalabescu, Letitia. (2021). Self Attention with Relative Position Representations – Paper explained. AI Coffee Break with Letita. [\[video\]](https://youtu.be/DwaBQbqh5aE)

***

### 1.2 Bidirectional Encoder Representations from Transformers (BERT)

BERT: pre-Training of Deep Bidirectional Transformers for Language Understanding. Devlin et al. 2019.

* Tags: transfer learning, pre-training, Transformer, NLP, masked language model, bidirectional
* Affiliations: Google AI Language
* [[paper]](https://arxiv.org/pdf/1810.04805.pdf)

BERT does not include a Transformer decoder.

Alammar, Jay. (2020). The Illustrated BERT, ELMo, and co. (How NLP Cracked Transfer Learning) [\[blog\]](https://jalammar.github.io/illustrated-bert/)

CodeEmporium. (2020). BERT Neural Network - EXPLAINED! [\[YouTube\]](https://youtu.be/xI0HHN5XKDo)

***

### Image + Attention

***

**Facebook AI Research applies Transformer architecture to streamline object detection models. 2020.**

* Tags:
* Affiliations: Facebook AI
* [[paper]](https://ai.facebook.com/research/publications/end-to-end-object-detection-with-transformers) [\[article\]](https://venturebeat.com/2020/05/28/facebook-ai-research-applies-transformer-architecture-to-streamline-object-detection-models/)

**An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale. Dosovitsky et al., 2021.**

* Tags: Transformer, image recognition, CNNs, scale
* Affiliations: Google AI
* [\[paper\]](https://arxiv.org/abs/2010.11929) [\[article\]](https://ai.googleblog.com/2020/12/transformers-for-image-recognition-at.html) [\[code\]](https://paperswithcode.com/paper/an-image-is-worth-16x16-words-transformers-1)

A pure Transformer applied directly to sequences of image patches can perform well on image classification tasks. Vision Transformer (ViT) attains comparable results to state-of-the-art ConvNets while requiring substantially fewer computational resources to train.

**Preliminary questions**

1. How does it require fewer computational resources?
2. What are these excellent results?
3. What was the architecture size?
4. How did the pre-training work?
5. What are the components of the architecture?
6. Why use those components in the architecture?

Transformers are self-attention based architectures.

Transformers are considered to have been made by Vaswani et al. in 2017 in Attention is all you need.

The dominant approach for using Transformers in NLP has been to pre-train on a large text corpus and then fine-tune to a smaller task-specific dataset. This was the central theme of the initial BERT paper (BERT: Pre-training of deep bidirectional transformers for language understanding. Devlin et al. 2019.).

In large-scale image recognition, classic ResNet-like architectures are still state of the art (below papers).

* Exploring the limits of weakly supervised pretraining. Mahajan et al. 2018.
* Self-training with noisy student improves ImageNet classification. Xie et al. 2020.
* Big Transfer (BiT). Kolesnikov et al. 2020.

A standard Transformer is applied directly to images by splitting an image into patches and then providing the sequence of linear embeddings of these patches as an input to the Transformer. Image patches are treated like tokens (words) in an NLP application. Image classification is then a standard supervised training procedure.

In which ways are ConvNets better or worse than Transformers? Transformers, when compared to ResNets of comparable size, are outperformed by a few percentage points in accuracy when trained on mid-sized datasets such as ImageNet without strong regularization. Why? Because Transformers lack certain biases inherent to ConvNets such as translational equivariance and locality. Consequently, Transformers don't generalize as well when trained on insufficient amounts of data.

However, when trained on datasets of 14M-300M images, the large scale training outdoes inherent bias of ConvNets, approaching or beating the state-of-the-art on multiple image recognition benchmarks.

Common image recognition benchmarks:

* ImageNet
* ImageNet-ReaL
* CIFAR-100
* VTAB suite of 19 tasks

Vision Transformer (ViT) gets excellent results when pre-trained at sufficient scale and transferred to tasks with fewer data points.

The related work section of the paper gives a thorough review of some of the recent breakthroughs in applications of attention to image-based tasks.

Naive application of self-attention to an image would require that each pixel attends to every other pixel. -> quadratic cost in the number of pixels -> doesn't scale to realistic image sizes

* [ ] Q: What's the alternative?

The Transformer encoder consists of alternating layers of multiheaded self-attention and MLP blocks.

* [ ] Q: Is there such thing as a single-headed attention?

Come back to this paper after deep-diving on Vaswani's paper. You've read maybe 5 pages so far.

**Attention Agent: Neuroevolution of Self-Interpretable Agents. Tang, Ngyuen, and Ha. 2020.**

* Tags: interpretability, evolutionary algorithm, Transformer, self-attention, deep RL, image input
* Affiliations: Google Brain (Google AI), Google Japan

**CURL: Contrastive Unsupervised Representations for Reinforcement Learning. Srinivas et al., 2020.**

* Tags: unsupervised, representation learning, deep RL, CNNs, image input
* Affiliations

**M-CURL: Masked Contrastive Representation Learning for Reinforcement Learning. Zhu et al., 2020.**

* Tags: masked training, representation learning, sample efficiency, self-supervised, CNNs, transformer, deep RL, BERT, contrastive learning, image input
* Affiliations: 1. University of Science an Technology of China. 2. Microsoft Research

Improving sample efficiency is a key research problem in reinforcement learning (RL). Contrastive Unsupervised representations for Reinforcement Learning (CURL).

Q: Besides the involvement masked training, what’s the key difference between M-CURL and CURL?\
A: M-CURL deals with videos (seqs of images) rather than individual images. Although consecutive frames are highly correlated, CURL handles them independently. M-CURL’s main improvement, outside of getting improved performance on several benchmarks, is that it takes into consideration the correlation between sequential frames.

This is where the transformer comes in. The Transformer, together with a CNN encoder, leverages the correlation of consecutive input frames to reproduce missing features in masked frames.

Q: Why use Transformers, specifically?\
A: The input in this paper was a sequence of images rather than a single image. Transformers (Waswani et al., 2017) are the current state-of-the-art module for modeling sequences and capturing their interdependencies.

Q: The authors call the Transformer module an "auxiliary Transformer". What makes it auxiliary?

Q: CNN encoder of what? What’s being encoded? And what is meant by "encode" here?

Q: Why discard the Transformer during action selection?

Q: Policy network? What does it do? What is it made up of? What are its inputs?

Q: Contrastive learning?
