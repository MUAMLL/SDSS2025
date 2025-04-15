# Docker Client

### 1. Docker System

Let's see if we have any running containers:

```bash
docker ps
```

What about any container images?

```bash
docker images
```

### 2. Pulling and Running Community Containers

Using the Container Image URI, we can pull in container images from official sources or from the open-source community:

Let's pull in a basic container image for Ubuntu 22.04 LTS now:

```bash
docker pull ubuntu:22.04
```

Let's run this container:

```bash
docker run ubuntu:22.04
```

Hmmm....nothing happened. Why? --> Because without any additional flags, docker will perform the `ENTRYPOINT` or `CMD`
of the container and then exit. If we want an interactive shell, we need to specify `-it`.

Let's try that again:

```bash
docker run -it ubuntu:22.04
```

Now we're in a container!

### 3. Using the Container

We have now entered the container. We now have process and file isolation, meaning the files and processes inside this
container are unique to the container, and run isolated from the processes inside the host system.

We can now use any software in the container, or install new software if we have root in the container (which we do
here).

Because this image's base container is Ubuntu, we can only run commands available in a Ubuntu 22.04 system. Let's try
invoking Rocky Linux's Package manager, `yum`:

```bash
yum install vim
```

This errors because Ubuntu does not use the Yum package manager. Let's try that again using `apt`, the package manager
for ubuntu:

```bash
apt update -y && apt install -y vim
```

Now we have vim installed!

In this example, we do not have any pre-installed software we need, but we'll see in other examples how this process can
be used for Data Science workflows

Let's exit from the container. To do this, we can send the EOF (Ctrl+D) or type `exit`:

```bash
exit
```

### 4. Viewing and Deleting Containers

Now, we're back in the host system. You may think that the container we just used is gone, but when we exit the
container, its status moves from `RUNNING` to `STOPPED`, but **it is still on our system, taking up space**.

This is an important consideration when using Docker. Your exited containers are still using space, which is great at
times because we can re-start the container if we need, but it can also lead to lots of stopped containers sitting on
your hard drive if you don't clean them up.

Let's view all of our containers, regardless of status. To do this, we use the `ps` command but with the `-a` flag:

```bash
docker ps -a
```

Now, if we want to delete that container, we can use it's name or ID and pass it to the `rm` command:

```docker
docker rm [CONTAINER NAME OR ID]
```

What about the image? It also still exists on our system, which is great because we can continue to create more
containers from it, but if we are fully finished, we may wish to remove it to reclaim that space on our system.

To do that, we'll run the `rmi` command with the name of the image:

```bash
docker rmi ubuntu:22.04
```
