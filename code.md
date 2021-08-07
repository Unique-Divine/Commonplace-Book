# Code Commonplace <!-- omit in toc -->

#### Table of Contents<!-- omit in toc -->
- [§ Python](#-python)
    - [Reading and Writing Files](#reading-and-writing-files)
  - [Object-Oriented Programming (OOP)](#object-oriented-programming-oop)
  - [Miscellaneous](#miscellaneous)
- [§ Web development](#-web-development)
  - [Hugo Web Design](#hugo-web-design)
  - [HTTP, TCP, IP](#http-tcp-ip)
  - [HTML, CSS](#html-css)
- [§ Algorithms](#-algorithms)
  - [Algorithms](#algorithms)
  - [Design Patterns](#design-patterns)
- [§ C++](#-c)

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

---

# § Python

---

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->


## Standard Libarry <!-- omit in toc -->

---

### Reading and Writing Files

`open()` returns a file object.

File objects mediate access to on-disk files. File objects are also called streams.

Q: `file_name (str)` is the name of a file. How do you read the file line by line in Python?
```python
with open(file=file_name, mode="r") as file:
    for idx, line in enumerate(file):
        pass # line (str): A line in the file
```

The two arguments of `open()` are 'file' and 'mode'.

Modes of `open()`:
- Mode `'a'`: For appending data to the end of 'file'. 
- Mode `'w'`: For writing only. An existing file with the same name as 'file' will be erased.
- Mode `'r+'`: opens a file for both reading and writing.

Q: Why use the `with` keyword with the `open` method?

It is good practice to use the `with` keyword when dealing with file objects because the file will be properly closed after its suite finishes even if an exception is raised at some point. Using `with` is also much shorter than writing equivalent `try-finally` blocks.

```python
with open(file="some_file") as file:
    pass
file.closed
```
`True`

- Python glossary - file object [[docs]](https://docs.python.org/3/glossary.html#term-file-object)

Date: 21年6月

<!-- -------------------------------- -->

---

## Object-Oriented Programming (OOP)

---

<!-- --------------------------------  -->

#### Prefer composition over inheritance

Inheritance makes it difficult to duplicate functionality to different classes. 

With composition, our goal is to separate out concepts so that they can be combined in meaningful ways. We're not creating hierarchies of classes. 

If we have a class that we want to make subclasses of, it's beneficial to make the first one an abstract base class. 

```python
from abc import ABC, abstractmethod
from typing import Optional 

class FFNN(ABC):  
    """Represents a PyTorch module for a feed-forward neural network."""

    @abstractmethod
    def forward()
```


Reference: ArjanCodes. Why COMPOSITION is better than INHERITANCE - detailed Python example. 2021. [[YouTube]](https://youtu.be/0mcP8ZpUR38)


#### Data classes

Python's `dataclass` functionality allows you to write shorter code and initialize, print, compare, and order data much more easily. 

Why use data classes?

A class for a data container is often used differently. Many instances may need to be made. You probably want to order them, compare them, easily inspect the data inside them, etc. 

Regular classes don't provide much built-in convenient functionality for data oriented classes. Classes that build around a behavior may not have as many instances or be conducive to representing data structures. Because of this, some programming languages provide a type of class that is better tuned to storing data, e.g. C#'s struct type that is good for representing data structures. 

Data classes have a built-in initialize that will help you quickly fill in an object with data. There are easy ways to print compare and order them. 

```python
# Regular class
class Person:
    """A person that has a name, job, and age."""
    name: str
    job: str
    age: int

    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age

p1 = Person()
```

Reference: ArjanCodes. 2021. If you're not using Python DATA CLASSES yet, you should. 🚀 [[YouTube]](https://youtu.be/vRVVyl9uaZc)


---

## Miscellaneous

#### ML Finance Project

#### [example w/ multivariate time series in PyTorch](https://stackabuse.com/time-series-prediction-using-lstm-with-pytorch-in-python/)

Q: Neural networks can be constructed using the `torch.nn` Python module.

Q: Import the package for constructing neural networks in PyTorch.
```python
import torch.nn as nn
```

Q: Seaborn comes with built-in datasets.

Q: Load seaborn’s flights dataset.
```python
flight_data = sns.load_dataset("flights")
```

Q: Why must time series data be scaled for sequence predictions?
: When a network is fit on unscaled data, it is possible for large inputs to slow down the learning and convergence of your network and in some cases prevent the network from effectively learning your problem.

Q: What's the sklearn import for min-max scaling data?
```python
from sklearn import preprocessing
scaler = preprocessing.MinMaxScaler()
```

We know the field is fast moving. If the reader looking for more recent free reading resources, there are some good  introductory/tutorial/survey papers on Arxiv

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

---

# § Web development

---

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

## Hugo Web Design

Start Sep 16 (Mike Dane Tutorial Series)

#### Intro to Hugo -[(video)](https://youtu.be/qtIqKaDlqXo) 

- Hugo is a static site generator.
- Static website generators allow you to compromise between writing a bunch of static html pages and using a heavy, and potentially expensive, content management system.
- Why Hugo? It's extremely fast.
- 2 kinds of websites, dynamic and static. Dyanmic ex. Facebook. Facebook pages are dynamically generated for each user. For static websites, what you see is what you get.
- Static websites are notoriously harder to maintain b/c you lack some of the flexibility of things on a dynamic site. Usually you can't use much conditional logic, functions, or variables.
- However, static pages are extremely fast.
- Hugo is great for a blog, portfolio website, etc.
- Hugo doesn't explicity require you to write a single line of HTML code.
- Flexibility \| With that said, if you want to go in and change every little detail of the layout of the site, you cna do that. You can write as much of the HTML and have as much control as you'd like.
- Hugo is 100% free and open-source.

#### Intalling Hugo on Windows - [(video)](https://youtu.be/G7umPCU-8xc?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3) 

-   Mine's already installed. I'll skip this for now.
-   a
-   a

#### Creating a new site - [(video)](https://youtu.be/sB0HLHjgQ7E?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3) 

-   skip, a bit too easy

#### Installing & Using Themes - [(video)](https://youtu.be/L34JL_3Jkyc?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3) 

-   my themes are already installed

#### Creating & Organizing Content - [(video)](https://youtu.be/0GZxidrlaRM?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3) 

-   Hugo has 2 types of content: single pages and list pages
-   List content lists other content on the site. You can call this a list page.
-   Individual blog posts are single pages.
-   Your posts should not just be in the content directory. They should be in directories inside the content directory.

-   A list page is automatically created for directories inside thecontent folder. Hugo automatically does this. Note, this only occursfor directories at the "root\" level of the content directory. Forexample: `content/post/` would generate a list page at`site.com/post/`, but `content/post/dir0` would not.

-   If you want a list page to be generated for a dir that is not at theroot level of the content dir, you have to create an **indexfiled**, `_index.md`. For a convenient and efficient way to do thisfrom the cmd, use `hugo new post/dir0/_index.md` (above aboveexample), then there will be a list page for dir0. Content can alsobe added to`_index.md` and it should show up on the page.

-   Additionally, for list pages that are aautomatically generate by hugo, you can edit the content by adding an index.md to those as well. Ex. ` content/post/_index.md`.

#### Front Matter- [(video)](https://youtu.be/Yh2xKRJGff4?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3 ) 

- Front matter in Hugo is what is commonly called meta data.
- Front matter is data about our content files.
- The metadata automatically generated by Hugo at the top of md files when using `hugo new ` is front matter
- Front matter is stored in key-value pairs
- Front matter can be written in 3 different languages: YAML, TOML, and JSON
- The defualt lang for front matter in Hugo is YAML
  - YAML - indicated by "--",
  - TOML - indicated by \"+++\" and uses \"=\" instead of \":\",
  - JSON - indicated by 
- You can create your own custom front matter variables.

Front matter is super powerful in its utility.

#### Archetypes - [(video)](https://youtu.be/bcme8AzVh6o?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3 ) 

-   How does the default front matter from using `hugo new  .md` get selected? Short answer: archetypes
-   An archetype is basically the default front matter template for when you create a new content file.
-   Archetypes are modified under `static/themes/archetypes/default.md`
-   Suppose your content dir has a subdirectory, `content/dir0`. If you wanted to create an archetype for the files in dir0, you'd simply create `dir0.md` inside the archetypes dir.

#### Shortcodes - [(video)](https://youtu.be/2xkNJL4gJ9E?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3 ) 

-   Shortcodes are predefined chunks of HTML that you can insert into your markdown files.

-   Let's say you have a md file that you want to spice up by adding in some custom HTML. For instance, maybe you'd like to embed a YouTube video. Normally this would require lots of HTML that you'd have to paste it. Shortcodes can allow you to sidestep this. Hugo comes with a YouTube video shortcode predefined.

-   General shortcode syntax `< shortcode_name param0 >`

-   Youtube shortcode \| For a YouTube video with url, `youtube.com/watch?v=random-text\`, the shortcode we'd use to embed would be `< youtube random-text >` because "random-text" is the id of the youtube video and the only parameter for that shortcode.

#### Taxonomies - [(video)](https://youtu.be/pCPCQgqC8RA?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3 )

-   Taxonomies in hugo are basically ways that you can logically group
    different pieces of content together in order to organize it in a
    more efficient way.

-   Hugo provids 2 defualt taxonomies: tags & categories

-   All taxonomy information is declared in front matter. In YAML, tags
    has the syntax `tags: ["tag0", "tag1", \ldots]`

#### Templates - [(video)](https://youtu.be/gnJbPO-GFIw)

-   Templates here mostly refers to HTML templates. If you're not
    comfortable writing HTML, CSS, and coding for the web, templates
    might be a little bit above your head.

-   A hugo theme is actually made up of hugo templates.

-   Any template that you use in Hugo is going to be inside
    `themes/theme-name/layouts`. This is where all the templates live.

-   ` /layouts/default` usually contains a default style for list and
    single pages by use of `list.html` and `single.html`.

#### List Templates - [(video)](https://youtu.be/8b2YTSMdMps)

-   List templates give default HTML layout to list content files.

-   .

#### Resources 

- [A clear and concise beginner hugo tutorial](https://www.linkedin.com/learninglearning-static-site-building-with-hugo-2/build-a-static-site-with-hugoresume=false)
- [CSS Crash Course for Absolute Beginners](https://youtu.be/yfoY53QXEnI)

## HTTP, TCP, IP

#### HTTP

HTTP = Hypertext Transfer Protocol

HTTP is a protocol that allows the fetching of resources such as HTML
documents. It allows web-based apps to communicate and exchange data.

HTTP is a client-server protocol. This means requests are initiated by a
recipient, usually the web browser, and a complete document is
constructed from the files fetched such as text, layout description,
images, videos, scripts, etc.

-   The client is the one making the request.

-   The server responds to this request.

##### Three important things about HTTP 

1.  HTTP is connectionless: After making the request, the client disconnects from the server. Then when the response is ready, the server re-establishes the connection again and delivers the response.
2.  HTTP can deliver any sort of data.
3.  HTTP is stateless: The client and server know about each other only during the current request. If the current request closes and the two computers want to connect again, they need to provide information to each other anew. In other words, statelessness means that the connection between the browser and the server is lost once the transaction ends.

To learn about requests and repsonses:
<https://youtu.be/eesqK59rhGA?t=275>

#### TCP/IP

The internet protocol suite is the conceptual model and set of
communications protocols used in the internet and similar computer
networks. It is commonly known as TCP/IP because the foundational
protocols in the suite are the Transmission Control Protocol (TCP) and
Internet Protocol (IP).

Communication prootocl: A system of rules that allow two or more
entitites of a communications system to transmit information via any
kind of variation of a physical quantity.

##### Internet Protocol (IP): {#internet-protocol-ip .unnumbered}

IP has the task of delivering packets from from the source host to the
destination host solely based on the IP addresses in the packet headers.
For this purpose, IP defines packet structures that encapsulate the data
to be delivered.It also defines addressing methods that are used to
label the datagrame with source and destination information.

- (network) packets: Formatted units of data carried by a packet-switched network. A packet consists of control information and user data; the latter is also known as the payload. Control information provides data for delivering the payload (e.g. source and destination network addresses, error detection codes, or sequencing information).

Q: What's an IP address?

An Internet Protocol address, or IP address, is a numerical label assigned to each device connected to a computer network tha tuses the Internet Protocol for communication.

##### Bandwitdth (computing): 

(Computing) bandwitdth is the maximum rate of data transfer across a
given path. Bandwidth can be characterized as network bandwidth, data
bandwidth, or digital bandwidth.

Computing bandwidth is different from the bandwidth defined in the field
of signal processing, signal bandwidth. Signal bandwidth is the
frequency range between lowest and highest attainable frequency while
meeting a well-defined impairment level in signal power. It's measured
in hertz.

In relation to internet protocol, we often talk about consume dbandwidth
in bit/s, which corresponds to achieved throughput or goodput, i.e. the
avg rate of successful data transfer through a communication path.

Q: Why is network bandwidth an average rate instead of a current rate?

A channel with $v_\beta$ may not necessarily transmit data at $v_t$ rate
since protocols, encryption, and other factors can add overhead. For
instance, internet traffic often uses TCP, which requires a three-way
handshake for each transaction. TCP is efficient, but it does add
significant overhead compared to simpler protocols. Additionally, data
packets may be lost, further reducing the data throughput.

Packet loss?
: Packet loss occurs when one or more packets of data travelling across a
computer network fail to reach their destination. Packet loss is either
caused by errors in data transmission, typically across wireless
networks, or network congestion. Packet loss is measured as a percentage
of packets lost with respect to packets sent.

Packet switching
: Packet switching is a method of grouping data that is transmitted over a
digital netowrk into packets. Packets are made of a header and a
payload. Data in the header is used by networking hardware to direct the
packet to its destination, where the payload is extracted and used by
application software. Packet switching is the primary basis for data
communications in computer networks worldwide.

#### Resources {#resources-1 .unnumbered}

-   <https://en.wikipedia.org/wiki/Internet_protocol_suite>

-   .

## HTML, CSS


<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

---

# § Algorithms

---

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

## Algorithms

> "4.5 years of learning programming and working as fullstack software engineer ... had interview with one of the FAANG companies this summer in Hong Kong but failed it due to the fact that I suck in DSA (Data Structures & Algorithms)."

> "I’m using to leetcode.com to learn data structures and algorithms since I got a rejection from FAANG after interviewing with them onsite."

[Role of DSA in Programming (July, 2020)](https://blog.codechef.com/2020/07/24/the-role-of-data-structure-and-algorithms-in-programming/)

## Design Patterns

Why use "design patterns"?

- Design patterns let your write better code more quickly by providing a clearer picture of how to implement the design
- Design patterns encourage code reuse and accomodate change by supplying well-tested mechanisms for delegation, composition, and other non-inheritance based reuse techniques
- Design patterns encourage more legible and maintainable code

Delegation? Composition?

- delegation: a pattern where a given object provides an interface to a set of operations. However, the actual work for those operations is performed by one or more other objects.
- composition: Creating objects with other objects as members. Should be used when a "has-a" relationship appears.

What are design patterns?

Which resources will you use to start learning about design patterns?

GOF patterns (C++). Then, potentially Head First Design Patterns (Java)/

#### References & Further Reading

[Introduction to Design Patterns Course](https://www.gofpatterns.com/design-patterns/module1/intro-design-patterns.php)

---

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

---

# § C++

---

<!-- ------------------------------------------------------------------ -->
<!-- ------------------------------------------------------------------ -->

C++ source code files end with a .cpp extension.

Hello world program: Run these and find out which one works.
```cpp
#include <iostream>;

int main() 
{
  std::cout << "Hello, world!";
  return 0;
}
```

Compiling and executing the C++ program:

1.  Step 1 is to install the gcc compiler.
2.  Verify the install of g++ and gdb with `whereis g++` and `whereis gdb`. To install gdb (linux or WSL), use `sudo apt-get install build-essential gdb`.

##### [Open MP](https://www.openmp.org//wp-content/uploads/openmp-examples-4.5.0.pdf)

People use OpenMP for shared memory parallelization. To import:
```cpp
#include <omp.h>;
```

#### Header files

C++ programs consist of more than just .cpp files. They also use **header files**, which can have a .h extension, .hpp extension, or even none at all.

Q: What is a `.h` file?
: header file

Q: What is the purpose of a header file?  
: Header files allow us to put declarations in one location and then import them wherever we need them. This can save a lot of typing in multi-file programs.

What’s contained in a `.h` file?

..

#### References & Further Reading

- [C header files](https://www.tutorialspoint.com/cprogramming/c_header_files.htm)
- [learncpp.com/.../header-files](https://www.learncpp.com/cpp-tutorial/header-files/)
