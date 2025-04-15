# Docker Customization

In our previous example, we saw the basics of pulling, running, and removing a container and its image.

Let's now look at some of the most common ways of customizing the running of the container.

### 1. Specifying a Name

To specify a name, we can specify `--name` to the `docker run` command:

```bash
docker run --name my-ubuntu-container ubuntu:22.04
```

Now, if we check `docker ps`, we'll see this name. This will be helpful for stopping, starting, removing, and networking
with this container

### 2. Mounting Local Storage

One of the many benefits to using Docker containers is the file and process isoloation, but what if we create something
in the container that we want to save for later? What if we have files on our host system that we need to use with the
software inside the container?

We can handle these use cases by **mounting** local directories to the container at runtime. To do this, we'll specify
the `-v` flag, and then hand it the path to the directory on the host system and the path we'd like that directory to be
mounted to.

For example, if we want to mount our local directory `/usr/src/mydirectory` to `/data` inside the container, we'd run:

```bash
mkdir -p /usr/src/mydirectory

docker run -it -v /usr/src/mydirectory:/data ubuntu:22.04
```

Once we're in the container, let's create a file in `/data`:

```bash
cat 'hello world' > /data/myfile.txt
```

And then exit the container:

```bash
exit
```

And now, back on the host system, we can print that file from outside the container:

```bash
cat /usr/src/mydirectory/myfile.txt
```

And we'll see 'hello world'.

**Note:** We can also mount directories to containers read-only so the container can only read the directory and not
change it. We can also pass the `-v` multiple times and mount multiple directories to a single container



### 3. Setting the Entrypoint / Command

While thus far, we have focused on entering and running a container, each container image sets a default entrypoint, or command, that will be run when the container starts. For Ubuntu this is `/bin/bash`. We can choose to change this.

For some containers, we want to change the entrypoint to `/bin/bash` because their default behavior is to start some process or run some script. And then for others, we'll want to skip the `/bin/bash` step and want the container to start software immediately. 

We can do this by appending the command we want to run to the end of our docker run command. So the syntax will be:
```bash
docker run [options] [image URI] [command]
```

such as:
```bash
docker run -it python:3.11 /bin/bash
```

### 4. Running Containers in the Background

The setting of an entrypoint / commmand is a great capability, especially when we pair it with being able to run containers in the background. 

Say we build or find a container that runs some process, like a database or web server. We want these processes to run, but we don't want or need to see its output as it does so. To do this, we can pass an alternative to `-it` to run the container in the background. We do this using the `-d` flag:
```bash
docker run -d ubuntu:22.04 sleep
```


### 5. Automatically Removing Containers

Remember from our first example that when we exit a container, the container only stops and remains on our system. Well, we can change that!

If we specify the `--rm` flag, the container will remove itself upon exit:
```bash
docker run -it --rm ubuntu:22.04
```

### 6. Exposing Ports in the Container

Networking in Docker is incredibly powerful and capable. We will not cover it in this tutorial at great depths, except to mention that if we have a process running in a container, such as a web server or a Jupyter server, we can map ports in the container to ports outside of the container on the host system. 

So for example, if we are going to run a Jupyter notebook on port 8888 inside the container, and want to access that Jupyter instance in our browser on the host system, we'd need to expose the port using the `-p` flag:

```bash
docker run -p 8888:8888 my-jupyter-container
```

## Final Note

All of these options can be combined as we see fit. We are not limited to using only one of them. 

So we could run:
```bash
docker run
  -it   # interactive w/ shell
  --name my-container # name of container
  -v ~/mydir:/output # mount directory RW
  -v /mydatadir:/data:ro # mount another directory readonly
  --rm # remove itself when done
  -p 8888:8888 # map 8888
myregistry.com/myusername/container:tag # name of the container iamge
jupyter notebook --ip 0.0.0.0 --port 8888 --allow-root # command when the container starts
```