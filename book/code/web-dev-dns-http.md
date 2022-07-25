<!-- web-dev.md -->
# Web Dev: HTML, CSS, etc.              <!-- omit in toc -->

- [HTML, CSS](#html-css)
  - [Flex Boxes](#flex-boxes)
    - [Margin](#margin)
    - [Padding](#padding)
    - [Scaling Vector Graphic (SVG)](#scaling-vector-graphic-svg)
- [Other](#other)
  - [Hugo Web Design](#hugo-web-design)
  - [HTTP, TCP, IP](#http-tcp-ip)
  - [Domain Name System (DNS)](#domain-name-system-dns)

---

# HTML, CSS


## Flex Boxes

Flex box: 

Flex item: elements of a flex box

Once a parent elemtent is configured with "`display: flex;`", the children no longer behave like blocks. They behave like "flex items".
What a flex item wants to do is be as small is it possibly can while staying on one line *if* they can stay within the parent flex. 


How to make flex items equal: Set "`flex: 1;`" in the style of the items. You can also use 
```css
.flex-box > * {
  flex-basis: 100%;
  /* or */ width: 100%;
}
```


### Margin 

Margin creates space around elements outside of any defined borders. For individual sides, there are properties like: `margin-top`, `margin-left`, `margin-bottom`, and `margin-right`.

Margin properties can have the following values: 
- auto: browser calculates the margin
- length: specify a margin in px, pt, cm, etc.
- %: specifies a margin in % of the width of the containing element
- inherit: specifies that the margin should be inherited from the parent element.

You can specify margin with four values as a shorthand for each direction:
```css
p {
  margin: 25px 50px 75px 100px;
  /* margin: top, right, bottom, left */
}
```

### Padding 

Padding is the space between the border and content of an element. Thus, padding is located inside the border of an element. 
```css
some-class {
  padding: 25px 50px;
  /* paddding - 2 vals: vertical, horizontal */
}
```

- 3 values: top, horizontal, right
- 4 values: top, right, bottom, left (clockwise from the top)

### Scaling Vector Graphic (SVG)

Useful command for converting svg files to React SVG Functional Components using [SVGR](https://react-svgr.com/docs/cli/):
```sh
npx @svgr/cli icon.svg > icon.tsx  
```

---

# Other

## Hugo Web Design

Start Sep 16 (Mike Dane Tutorial Series)

**Intro to Hugo -** [[video]](https://youtu.be/qtIqKaDlqXo)

- Hugo is a static site generator.
- Static website generators allow you to compromise between writing a bunch of static html pages and using a heavy, and potentially expensive, content management system.
- Why Hugo? It's extremely fast.
- 2 kinds of websites, dynamic and static. Dyanmic ex. Facebook. Facebook pages are dynamically generated for each user. For static websites, what you see is what you get.
- Static websites are notoriously harder to maintain b/c you lack some of the flexibility of things on a dynamic site. Usually you can't use much conditional logic, functions, or variables.
- However, static pages are extremely fast.
- Hugo is great for a blog, portfolio website, etc.
- Hugo doesn't explicity require you to write a single line of HTML code.
- Flexibility | With that said, if you want to go in and change every little detail of the layout of the site, you cna do that. You can write as much of the HTML and have as much control as you'd like.
- Hugo is 100% free and open-source.

**Intalling Hugo on Windows - **[**(video)**](https://youtu.be/G7umPCU-8xc?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3)

* Mine's already installed. I'll skip this for now.
* a
* a

**Creating a new site - **[**(video)**](https://youtu.be/sB0HLHjgQ7E?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3)

* skip, a bit too easy

**Installing & Using Themes - **[**(video)**](https://youtu.be/L34JL\_3Jkyc?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3)

* my themes are already installed

**Creating & Organizing Content - **[**(video)**](https://youtu.be/0GZxidrlaRM?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3)

* Hugo has 2 types of content: single pages and list pages
* List content lists other content on the site. You can call this a list page.
* Individual blog posts are single pages.
* Your posts should not just be in the content directory. They should be in directories inside the content directory.
* A list page is automatically created for directories inside thecontent folder. Hugo automatically does this. Note, this only occursfor directories at the "root" level of the content directory. Forexample: `content/post/` would generate a list page at`site.com/post/`, but `content/post/dir0` would not.
* If you want a list page to be generated for a dir that is not at theroot level of the content dir, you have to create an **indexfiled**, `_index.md`. For a convenient and efficient way to do thisfrom the cmd, use `hugo new post/dir0/_index.md` (above aboveexample), then there will be a list page for dir0. Content can alsobe added to`_index.md` and it should show up on the page.
* Additionally, for list pages that are aautomatically generate by hugo, you can edit the content by adding an index.md to those as well. Ex. ` content/post/_index.md`.

**Front Matter- **[**(video)**](https://youtu.be/Yh2xKRJGff4?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3)

* Front matter in Hugo is what is commonly called meta data.
* Front matter is data about our content files.
* The metadata automatically generated by Hugo at the top of md files when using `hugo new `is front matter
* Front matter is stored in key-value pairs
* Front matter can be written in 3 different languages: YAML, TOML, and JSON
* The defualt lang for front matter in Hugo is YAML
  * YAML - indicated by "--",
  * TOML - indicated by "+++" and uses "=" instead of ":",
  * JSON - indicated by
* You can create your own custom front matter variables.

Front matter is super powerful in its utility.

**Archetypes - **[**(video)**](https://youtu.be/bcme8AzVh6o?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3)

* How does the default front matter from using `hugo new  .md` get selected? Short answer: archetypes
* An archetype is basically the default front matter template for when you create a new content file.
* Archetypes are modified under `static/themes/archetypes/default.md`
* Suppose your content dir has a subdirectory, `content/dir0`. If you wanted to create an archetype for the files in dir0, you'd simply create `dir0.md` inside the archetypes dir.

**Shortcodes - **[**(video)**](https://youtu.be/2xkNJL4gJ9E?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3)

* Shortcodes are predefined chunks of HTML that you can insert into your markdown files.
* Let's say you have a md file that you want to spice up by adding in some custom HTML. For instance, maybe you'd like to embed a YouTube video. Normally this would require lots of HTML that you'd have to paste it. Shortcodes can allow you to sidestep this. Hugo comes with a YouTube video shortcode predefined.
* General shortcode syntax `< shortcode_name param0 >`
* Youtube shortcode | For a YouTube video with url, `youtube.com/watch?v=random-text\`, the shortcode we'd use to embed would be `< youtube random-text >` because "random-text" is the id of the youtube video and the only parameter for that shortcode.

**Taxonomies - **[**(video)**](https://youtu.be/pCPCQgqC8RA?list=PLLAZ4kZ9dFpOnyRlyS-liKL5ReHDcj4G3)

* Taxonomies in hugo are basically ways that you can logically group different pieces of content together in order to organize it in a more efficient way.
* Hugo provids 2 defualt taxonomies: tags & categories
* All taxonomy information is declared in front matter. In YAML, tags has the syntax `tags: ["tag0", "tag1", \ldots]`

**Templates - **[**(video)**](https://youtu.be/gnJbPO-GFIw)

* Templates here mostly refers to HTML templates. If you're not comfortable writing HTML, CSS, and coding for the web, templates might be a little bit above your head.
* A hugo theme is actually made up of hugo templates.
* Any template that you use in Hugo is going to be inside `themes/theme-name/layouts`. This is where all the templates live.
* ` /layouts/default` usually contains a default style for list and single pages by use of `list.html` and `single.html`.

**List Templates - **[**(video)**](https://youtu.be/8b2YTSMdMps)

* List templates give default HTML layout to list content files.
* .

**Resources**

* [A clear and concise beginner hugo tutorial](https://www.linkedin.com/learninglearning-static-site-building-with-hugo-2/build-a-static-site-with-hugoresume=false)
* [CSS Crash Course for Absolute Beginners](https://youtu.be/yfoY53QXEnI)

## HTTP, TCP, IP

**HTTP**

HTTP = Hypertext Transfer Protocol

HTTP is a protocol that allows the fetching of resources such as HTML documents. It allows web-based apps to communicate and exchange data.

HTTP is a client-server protocol. This means requests are initiated by a recipient, usually the web browser, and a complete document is constructed from the files fetched such as text, layout description, images, videos, scripts, etc.

* The client is the one making the request.
* The server responds to this request.

**Three important things about HTTP**

1. HTTP is connectionless: After making the request, the client disconnects from the server. Then when the response is ready, the server re-establishes the connection again and delivers the response.
2. HTTP can deliver any sort of data.
3. HTTP is stateless: The client and server know about each other only during the current request. If the current request closes and the two computers want to connect again, they need to provide information to each other anew. In other words, statelessness means that the connection between the browser and the server is lost once the transaction ends.

To learn about requests and repsonses: [https://youtu.be/eesqK59rhGA?t=275](https://youtu.be/eesqK59rhGA?t=275)

**TCP/IP**

The internet protocol suite is the conceptual model and set of communications protocols used in the internet and similar computer networks. It is commonly known as TCP/IP because the foundational protocols in the suite are the Transmission Control Protocol (TCP) and Internet Protocol (IP).

Communication prootocl: A system of rules that allow two or more entitites of a communications system to transmit information via any kind of variation of a physical quantity.

**Internet Protocol (IP):**

IP has the task of delivering packets from from the source host to the destination host solely based on the IP addresses in the packet headers. For this purpose, IP defines packet structures that encapsulate the data to be delivered.It also defines addressing methods that are used to label the datagrame with source and destination information.

* (network) packets: Formatted units of data carried by a packet-switched network. A packet consists of control information and user data; the latter is also known as the payload. Control information provides data for delivering the payload (e.g. source and destination network addresses, error detection codes, or sequencing information).

Q: What's an IP address?

An Internet Protocol address, or IP address, is a numerical label assigned to each device connected to a computer network tha tuses the Internet Protocol for communication.

**Bandwitdth (computing):**

(Computing) bandwitdth is the maximum rate of data transfer across a given path. Bandwidth can be characterized as network bandwidth, data bandwidth, or digital bandwidth.

Computing bandwidth is different from the bandwidth defined in the field of signal processing, signal bandwidth. Signal bandwidth is the frequency range between lowest and highest attainable frequency while meeting a well-defined impairment level in signal power. It's measured in hertz.

In relation to internet protocol, we often talk about consume dbandwidth in bit/s, which corresponds to achieved throughput or goodput, i.e. the avg rate of successful data transfer through a communication path.

Q: Why is network bandwidth an average rate instead of a current rate?

A channel with $v\_\beta$ may not necessarily transmit data at $v\_t$ rate since protocols, encryption, and other factors can add overhead. For instance, internet traffic often uses TCP, which requires a three-way handshake for each transaction. TCP is efficient, but it does add significant overhead compared to simpler protocols. Additionally, data packets may be lost, further reducing the data throughput.

Packet loss? : Packet loss occurs when one or more packets of data travelling across a computer network fail to reach their destination. Packet loss is either caused by errors in data transmission, typically across wireless networks, or network congestion. Packet loss is measured as a percentage of packets lost with respect to packets sent.

Packet switching : Packet switching is a method of grouping data that is transmitted over a digital netowrk into packets. Packets are made of a header and a payload. Data in the header is used by networking hardware to direct the packet to its destination, where the payload is extracted and used by application software. Packet switching is the primary basis for data communications in computer networks worldwide.

## Domain Name System (DNS)

The Domain Name System is the phonebook fo the internet. Humans access information online through **domain** names like google.com and tim.blog. Web browsers interact through Internet Protocol (IP) addresses. DNS translates domain names into IP addresses so that browsers can load internet resources.

Each device connected to the Internet has a unique IP address which other machines use to find the device. DNS servers eliminate the need for humans to memorize IP addresses such as 192.168.1.1 (in IPv4), or more complex newer alphanumeric IP addresses.

What is the difference between a domain name and a URL?

A **uniform resource locator (URL)**, sometimes called a web address, **contains the domain name** of a site **as well as the transfer protocol and the path**. For example, in the URL "https://github.com/numpy", "github.com" is the domain name, "https" is the protocol and "/numpy" is the path to a specific page on the website.

#### Address (A) records: Record that points to the IP address for a given domain.

"A" stands for "address". The most common usage of A records is IP address lookups, where a domain name is mapped to an IPv4 address. This enable's a device to connect with and load a website without a user needing to memorize or type in the actual IP address. This is carried out automically because the browser sends a query to a DNS resolver.

An A record contains four attributes.
- host:
- type: Ex. "A", "CNAME".
- points to: Ex. "185.107.80.223"
- TTL:
Examples:

| Host | Type | Points to | TTL |
| :--: | :--: | :--: | :--:  |  
| my.blog |	A | 123.456.78.999 | 1 Hour |
| www.my.blog |	CNAME | my.blog | 3600 | 

#### Canonical name (CNAME) records

A **CNAME, or "canonical name"**, record is used in lieu of an A record, when a domain or subdomian is an alias of another domain. All CNAME records must point to a domain rather than an IP address. To be clear, a CNAME record *cannot* point to an IP address.

Suppose that "alias.site.com" has a CNAME record with a value of "example.com". This means that when a DNS server hits the DNS records for "alias.site.com", it triggers another DNS lookup to "example.com"

Why do you use a CNAME text file when setting up a custom domain?

A CNAME reord allows a site to resolve to a different domain while pointing the the true IP address. Let's say that alias.site.com has a CNAME that points to example.com, directing the client to example.com's IP. When the client actually connects to that IP address through alias.site.com, the web server will look at this URL and deliver the page there (alias.site.com) rather than to the homepage (example.com).


#### DNS Resources

* [https://en.wikipedia.org/wiki/Internet\_protocol\_suite](https://en.wikipedia.org/wiki/Internet\_protocol\_suite)
- [What is DNS](https://www.cloudflare.com/learning/dns/what-is-dns/)
- [What is a DNS CNAME record?](https://www.cloudflare.com/learning/dns/dns-records/dns-cname-record/)
- [What is a domain name? | Domain name vs. URL](https://www.cloudflare.com/learning/dns/glossary/what-is-a-domain-name/)
- [DNS A record](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/)
- [DNS resolver](https://www.cloudflare.com/learning/dns/dns-server-types/) 
