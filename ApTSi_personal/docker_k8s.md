
# Docker & K8s Introduction <!-- omit in toc -->

## Welcome 

### Contents <!-- omit in toc -->
- [Welcome](#welcome)
- [Why use Docker and K8s?](#why-use-docker-and-k8s)
  - [Realistic Case Scenario:](#realistic-case-scenario)
  - [Docker Basic Concepts](#docker-basic-concepts)
  - [OS concepts](#os-concepts)
  - [Containers vs virtual machines:](#containers-vs-virtual-machines)
  - [Containers vs images (Docker):](#containers-vs-images-docker)
- [What is Docker?](#what-is-docker)
- [Docker Install (Windows)](#docker-install-windows)
  - [0. Running `docker run hello-world` fails.](#0-running-docker-run-hello-world-fails)
- [References](#references)
- [Kubernetes Concepts](#kubernetes-concepts)


Containers
- simplify and accelerate worflow when working with mutliple languages, frameworks, architectures, and discontinuous interfaces
- **Docker** is the most popular container technology

Kubernetes AKA K8s
- built by Google based on their experience running containers in production
- now an open-source project
- probably the most popular **container orchestration** technology
- To understand Kubernetes, two fundamental concepts must first be understood: Containers & Orchestration

## Why use Docker and K8s? 

### Realistic Case Scenario: 
Let's say you had a project including an end-to-end stack consisting of a web server, database, messaging system, and orchestration.
- Web server: Express JS (Node JS)
- Database: Mongo DB
- Messaging: Reddit
- Orchestration: Ansible

This application uses a lot of different components and this can cause various issues. For example,
- **Compatibility & Dependency**:
  - Each component may have compatibility issues with the current version underlying OS.
  - Each component may have library and dependency issues. Maybe your web service could require one version of dependent library, while the database or orchestration needs another version.
- **Setup time**: Every time a new developer is braught on board, it can be difficult to get them a working environment. They may have to run hundreds of commands at their CLI, using the right versions of the OS and each component.

The architecture of the project will change over time. And every time something changes, it will be inefficient if you have to go back and handle these compatibility/dependency issues to have each component interact. That situation is ocmmonly referred to in the DevOps world as the "[matrix from hell][matrix from hell]". 

[matrix from hell]: https://sdtimes.com/containers/stuck-new-devops-matrix-hell/#:~:text=So%2C%20what%20is%20the%20matrix,operating%20systems%2Fhardware%2Finfrastructure.

Docker and K8s help us avoid and prevent dealing with the matrix from hell.

### Docker Basic Concepts

Docker allows us to run each component in a what is called a "container". To interact with each piece of software in the stack, users will only need to make sure that they have Docker running on their machines.

What are containers?
-  a standardized unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another.
- Isolated environments that can run their own processes, network and interfaces, and mounts just like virtual machines, except they all share the same OS kernel. 
- Containers are not unique to Docker. There are [different types][different types]. Docker uses [LXC containers][LXC containers].
- Containers have functionality that is "close to the hardware", "low-level". Docker gives a convenient way for developers to interact with the OS at a high-level. 

[different types]: https://containerjournal.com/topics/container-ecosystems/5-container-alternatives-to-docker/
[LXC containers]: https://linuxcontainers.org/

### OS concepts

OS (def): 
> An interface between a computer user and computer hardware. A software which performs all the basic tasks like file management, memory management, process managemenet, handling input and output, and controlling peripheral devices such as disk drives and printers. 

https://youtu.be/rmf04ylI2K0?t=369
All operating systems consist of an OS kernel and a set of application software.

- **[OS Kernel][OS Kernel]**: A program that connects the application software to the hardware of the computer. Facilitates the interaction between hardware and software components.
- **Application software**- This can consist of different UIs, drivers, compilers, file managers, etc. For example, different linux operating systems all use a Unix kernel but have different application software.

[OS Kernel]: https://en.wikipedia.org/wiki/Kernel_(operating_system)

Docker containers share the same underlying kernel. This means you won't be able to run a Windows-based container on an Ubuntu kernel. For that, we'd require Docker on a Windows server. Docker is not meant to virtualize and run different OS kernels on the same hardware. The main purpose of Docker is to containerize applications for deployment. 


### Containers vs virtual machines:

Virtual machines, through the use of a [hypervisor](https://www.vmware.com/topics/glossary/content/hypervisor) or virtual machine montor VMM, can run differnet kernels on the same hardware. However, this causes high utilization of underlying computational resources. VMs also consume much more disk space as each VM is on the order of GBs.

Containers take up disk space on the order of MBs, have lower utilization, and as a result, can boot up much faster.



### Containers vs images (Docker):
- **Docker image**: A package or template just like a VM template in the virtualization world. Used to create containers.
- **Container**: A running instance of a docker image that is isolated and has its own set of processes.

Advantage of using containers:


## What is Docker?

Docker is 
> an open-source project that automates the deployment of software applications inside containers by providing an additional layer of abstraction and automation of OS-level virtualization on Linux.

## Docker Install (Windows)

Get the executable installer from [Docker Hub](https://hub.docker.com/editions/community/docker-ce-desktop-windows/)

Open and run the intaller.

Open a command-line terminal and try out basic Docker commands:
- `docker version`: Chekcs the version
- `docker run hello-world`: Verifies that Docker can pull and run images 
> Docker is available in any terminal as long as the Docker Desktop for Windows app is running. Settings are available on the UI, accessible from the Docker whale in the taskbar.

### 0. Running `docker run hello-world` fails.

After lots of searching around, I found someone wih a [similar issue][similar issue].
- The bottom-most suggestion from [Zoe Tao][zoe tao link] worked when I ran `net start vmcompute` and then rebooted. 

> 1. Open "Window Security"
> 2. Open "App & Browser control"
> 3. Click "Exploit protection settings" at the bottom
> 4. Switch to "Program settings" tab
> 5. Locate "C:\WINDOWS\System32\vmcompute.exe" in the list and expand it
> 6. Click "Edit"
> 7. Scroll down to "Code flow guard (CFG)" and uncheck "Override system settings"
> 8. Start vmcompute from powershell: `net start vmcompute`  
> 9. Reboot your computer. 

This fixed my installation and I was able to successfully use `docker run hello-world` at the Windows PowerShell. 

[similar issue]: https://github.com/docker/for-win/issues/3764
[Zoe Tao link]: https://social.technet.microsoft.com/Forums/azure/en-US/900298bd-4a86-4c9d-9950-11f0c050fa2f/hyperv-manager-unable-to-connect-to-server-quotlocal-computerquot?forum=win10itprovirt



## References

- [Prakhar Srivastav. *Docker for Beginners*](https://docker-curriculum.com/) 
- [Docker 101 Tutorial](https://www.docker.com/101-tutorial) 
- [KodeKloud (2018). *Docker introduction in 15 minutes*](https://youtu.be/rmf04ylI2K0) 
- [Operating System Tutorial][Operating System Tutorial]

[Operating System Tutorial]: https://www.tutorialspoint.com/operating_system/index.htm#:~:text=An%20Operating%20System%20(OS)%20is%20an%20interface%20between%20a%20computer,as%20disk%20drives%20and%20printers.

----

## Kubernetes Concepts

[Kubernetes concepts explained in 9 minutes](https://youtu.be/QJ4fODH6DXI)

If a container was to fail, 

If a docker host was to fail,

large applications with 1000s of containers


Container orchestration: A set of tools and scripts that can  help host containers in the production environment. 
- Consists of multiple docker hosts that can host constainers so that if one container fails, the application will be acessible through the other hosts. 


Kubernetes CLI is known as "kube control". Example kubernetes command to generate a cluster:
```
kubectl run --replicas=100 my-web-server
```

Other tools for container orchestration: Docker Swarm, Mesos





