# bioinformatics

- [bioinformatics](#bioinformatics)
    - [Deep Learning for Genomic Prediction](#deep-learning-for-genomic-prediction)
    - [Computational Genomics (course, Rob Edwards)](#computational-genomics-course-rob-edwards)

### Deep Learning for Genomic Prediction

original title: DL for Genomic Risk Scores

> “ A central aim of computational genomics is to identify variants
> (SNPs) in the genome which increase risks for diseases. Current
> analyses apply linear regression to identify SNPs with large
> associations, which are collected into a function called a Polygenic
> Risk Score (PRS) to predict disease for newly genotyped individuals.
> This project is broadly interested in whether we can improve
> performance of genomic risk scores using modern machine learning
> techniques.
>
> A recent study assessed the disease prediction performance of neural
> networks in comparison to conventional PRSs, but did not find evidence
> of improvement. This project will explore whether neural networks can
> improve performance by incorporating gene expression data to the
> training process. Gene expression is often integrated with SNP data in
> Transcriptome-Wide Association Studies (TWAS), which bear some
> resemblance to neural network architectures with SNPs as input nodes,
> genes as intermediate nodes, and disease status as the output node.
> Modeling this process as a neural network however will require
> defining a more unconventional architecture in which a small subset of
> hidden nodes is anchored to observed values.
>
> This project is designed for students with experience in machine
> learning topics and preferably with deep learning tools such as
> tensorflow or pytorch. Students should also be interested in applying
> machine learning and statistics to genomics applications.” - Jie Yuan

**Terms to know**: Computational genomics, variants, single-nucleotide
polymorphism (SNP), genome, Polygenic Risk Score (PRS),
Transcriptome-Wide Association Studies (TWAS), gene(s), genomics,
genotype, intermediate node (NN), hidden node (NN)

Explain at a high level how PRSs tells us disease risk.

“In what task were neural networks outperformed by conventional PRSs?”

What is meant by “improve performance of genomic risk scores?”

genotype  
: An individual’s collection of genes. Also can refer to the two alleles
inherited for a particular gene.

node (NN)  
: An artificial neural network is an interconnected group of nodes,
inspired by a simplification of neurons in a brain. Here, each circular
node represents an artificial neuron and an arrow represents a
connection from the output of one artificial neuron to the input of
another[1].

hidden node (NN)  
: A node in a hidden layer.

hidden layer (NN)  
:


#### Polygenic Risk Scores (paper) 

##### Abstract (mining)

recurrence risks  
: In genetics, the likelihood that a hereditary trait or disorder
present in one family member will occur again in other family
members[2].

“Evidence for genetic contribution to complex diseases is described by
recurrence risks to relatives of diseased individuals.”

This is distinguished from recurrence risk for cancer, which is the
chance that a cancer that has been treated will recur.

gene  
: a sequence of DNA that codes for a specific peptide or RNA molecule;
the physical and functional unit of heredity.

locus  
: the position of a gene on a chromosomes

somatic cell  
: any cell of the body except sperm and egg cells. A non-germline cell.
any biological cell forming the body of an organism (except gametes).

sôma (Ancient Greek): body

genome  
: An organism’s complete set of DNA, including all of its genes. Each
genome contains all of the information needed to build and maintain that
organism. In humans, a copy of the entire genome—more than 3 billion DNA
base pairs—is contained in all cells that have a nucleus [3]. “genome-wide association”

allosome  
: (1) A sex chromosome such as the X and Y human sex chromosomes. (2) An
atypical chromosome [4].

allo- (Greek)
: other, differnt

autosome  
: Any chromosome that is not a sex chromosome. The numbered chromosomes.

auto (Greek)
: self, one’s own, by oneself, of oneself

-some, soma (Greek): body

allele  
: (genetics) One of a number of alternative forms of the same gene
occupying a given position, or locus, on a chromosome.  
Borrowed from German Allel, shortened from English allelomorph.
Ultimately from the Ancient Greek prefix allēl- from állos (“other”). “their effects and allele frequencies”

allelomorph
: another term for allele.

risk loci  
:

“genome-wide association studies allow a description of the genetics of
the same diseases in terms of risk loci...”

haploid  
: the quality of a cell or organism having a single set of chromosomes.

diploid  
: the quality of having two sets of chromosomes. “Sexually reproducing organisms are diploid” (having two sets of chromosomes, one from each parent)

eukaryotes  
: Organisms whose cells have a nucleus enclosed within a nuclear
envelope.

gamete
: A mature sexual reproductive cell, as a sperm or egg, that unites with
another cell to form a new organism. A haploid cell that fuses with
another haploid cell during fertilization in organisms that sexually
reproduce. A mature haploid male or female germ cell which is able to
unite with another of the opposite sex in sexual reproduction to form a
zygote.
gamete (Ancient Greek): to marry

zygote  
: A eukaryotic cell formed by a fertilization event between two gametes. zygōtos (Greek): joined. yoked.

monozygotic  
: Monozygotic (MZ) or identical twins occur when a single egg is
fertilized to form one zygote (hence, "monozygotic") which then divides
into two separate embryos. “monozygotic twins”

empirical  
: “generate results more consistent with empirical estimates”

genetic variants  
: ...

A human cell containing 22 autosomes and a Y chromosome is a sperm.

#### Neural Networks for Genomic Prediction (paper) 

#### Transcriptome Wide Association

---

#### Jie Yuan meeting \#2 (Sep 10)

- There’s a dot product and its output is passed through some activation function like sigmoid or ReLU. It’s still linear in the sense that there’s some sort of function that takes in a dot product (which is the definition of a linear operation). You can think of "the betas" as the weights in the neural network because the betas are the coefficients of a linear model.
-   Liability is discussed in the multi-locus models paper.
-   In the genomics context, this is called the **liability threshold model**. If you google that, you’ll find some papers. In a broader machine learning sense, this is called the **probit regression model**. WIkipedia probably has a sufficient article on it.
-   The gist of it is that it’s a model to map continuous sums (the dot products basically) into binary labels: cases and controls. This can be any sort of logistic regression type thing where you have 0s and 1s. Basically, the **probit model is an alternative to the logistic regression model**.
-   The liability is related to what’s called the “link function”. The link function in the probit model is the normal CDF function. There’s a term that goes into the link function, and that term is what we’re calling liability.
-   The liability is basically the product of the vector of genotypes and the vector of betas. It’s the linear part of the generalized linear model.
-   Once you have the liability and plug it into the link function. Here, the link function is the probit regression. In a neural network, this would be the linear activation function (sigmoid, ReLU, etc.).
-   You know how a sigmoid has a domain that’s $( − \infty, \infty)$? It’s range is $(0,1)$, so what that function does is map a real value into being a probability. It gives you the probability of being a case. If you look at the normal CDF function, you find that it looks almost the same.

##### Why is the liability threshold model better than or different from the logistic reg model? 

- One reason people use log reg more often is that the betas from log reg are interpretable. The have a meaning in terms of odds ratios. In a log reg model, the effect sizes are the natural log of the odds ratios.
- One disadvantage of log reg compared to liability-threshold is that log reg doesn’t have a concept of the underlying distribution of the liability. In log reg, you get the linear $Xβ$ term, but there’s no sort of distribution around it. In the liability-thresh model, we say that the liability, itself, is standard normally distributed. By taking the normal CDF, what you’re doing is mapping that $Xβ$ value, the liability value, onto this distribution and asking, “what’s the probability that it’s larger than some threshold?"
- Larger than threhsold ⟹ label as 1, smaller ⟹ 0.

- Because liability-threshold has that normal distribution, it gives you more concepts to play with such as variance explained, which the logistic reg model doesn’t have.
- [liability threshold model in simple terms](wikilectures.eu/w/Genetic_Liability,_Threshold_Model.)
- from wikipedia: [Liability threshold model](https://en.wikipedia.org/wiki/Threshold_model#Liability_threshold_model)

##### schizophrenia (SZ) example:
-   Whether or not someone has SZ comes from a combination of factors in both their genes and environment.
-   There are all sorts of variables. Imagine hypothetically that you could collect all of them and produce a score from that (that determines whether or not you have SZ). That score would be the liability.
-   The liability is a $\mathcal{N}(0,1)$ distribution that, if higher than the threshold, predicts/indicates the patient has SZ.
-   The problem with that is that we don’t actually observe everything. We don’t truly observe every factor that goes into whether you have SZ b/c (1) we can’t measure one’s environment and (2) we can’t know all of the genomic risk factors from GWAS. We can only identify the largest risk factors.

This means we are identifying only a small fraction of what goes into genetic risk for SZ.

-   Essentially, what we have is a small subset of the factors that actually determine your SZ risk (which we’re reasonably confident indicate this relationship). In this example, some subset of the risk factors like the genomic variance which increase your risk for SZ.

-   What that means is that inside this standard normal liability distribution/function, what we actually know is a small subset of the factors that go into that. If we score people on that subset of factors, what we get is a smaller distribution, a distribution that has a variance that’s a small fraction of the total liability variance, which we can’t observe. The variance of that small fraction that we observe, that’s the **variance explained**.


### Computational Genomics (course, Rob Edwards)

This section details my notes from [Rob Edwards’s open source
course](https://www.youtube.com/watch?v=WuoHFKm4vXo&list=PLpPXw4zFa0uLMHwSZ7DMeLGjIUgo1IBbn&index=1)
at San Diego State University (Copyright 2018).

What will be learned in this course?

We’ll use cutting-edge tools to analyze microbial genomes.

By the time we’re done with the course, you’ll have the ability to:

-   use Amazon Web Services to analyze genomes

-   use existing bioinformatics applications

-   describe how algorithms used in bioinformatics work

-   download, identify, and analyze data from public repositories

-   critically analyze genomes and metagenomes

#### Central Dogma of Biology

[[lecture video]](https://www.youtube.com/watch?v=FRlNkKhbMAY&list=PLpPXw4zFa0uLMHwSZ7DMeLGjIUgo1IBbn&index=7)

Dogma (def):

1.  a principle or set of principles laid down by an authority as incontrovertibly true."the Christian dogma of the Trinity". "the rejection of political dogma." "the classic dogma of objectivity in scientific observation". "the difficulty of resisting political dogma".
2.  Characterized by assertion of unproved or unprovable principles. A doctrine that is proclaimed as true without proof. "he believed all the Marxist dogma". "dogmatic writings".

##### In Essence:

DNA is the genetic code. DNA is converted to messenger RNA (mRNA) through a process called transcription. There are two other types of RNA: tRNA and rRNA. mRNA is converted into proteins. Proteins are comprised of amino acids. In mRNA, nitrogenous bases consitute what’s called a codon. A codon encodes for one amino acid. mRNA is read sequentially, one codon at a time, to give sequences of amino acids that make up a protein. Bonus: There’s also a "reverse" transcription that certain viruses can do, where mRNA is converted back into DNA. Humans don’t normally do that. Bacteria don’t normally do that. Viruses do. **Bottom Line:** DNA is essentially the standard code for all living organisms as far as we know.

DNA’s alphabet: A C G T

RNA’s alphabet: A C G U

DNA gets transcribed into RNA in a sequence-depended fashion.

DNA has a direction. One side of a strand is 5’, "the 5 prime band", and
one is 3’. This direction is 5’ to 3’.

DNA lines up in pairs of sequences with bases aligned in complementary
pairs. These pairs are called "reverse compliments"

RNA is made with what’s called a template strand.

#### What does it mean to sequence a genome?

##### Q: What’s a genome?

Humans have 23 pairs of chromosomes. Each pair consists of a chromosome
from each parent.

All of the DNA contained in one cell is called the genome. We have one
copy of the genome in nearly every cell in our body. Human genomes are
 ≈ 99.8% identical to that of every other human being. The other 0.2% of
the genome is what is of high interest to healthcare professionals as
understanding it can help in the prediction, prevention, diagnosis, and
treatment of disease.

-   Human genome 3.1 billion bp (base pairs), i.e. 3.1 Gbp
-   bacteria 100 kbp - 2Mbp
-   This means that the computational overhead of studying bacterial genomes is much smaller and can be done on a standard personal computer.

[1]: https://en.wikipedia.org/wiki/Artificial_neural_network
[2]: https://www.cancer.gov/publications/dictionaries/genetics-dictionary/def/recurrence-risk 
[3]: https://ghr.nlm.nih.gov/primer/hgp/genome
[4]: https://www.merriam-webster.com/medical/allosome