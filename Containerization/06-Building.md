# Building a Custom Docker Container Image

Let's see the container image build process in action. For this example, let's build an application that takes in the
path to an image, a conversion code, and the path to the output

### Step 1: Create the Dockerfile

The first step is to create a Dockerfile. For this example, our Dockerfile will be relatively simple:

```dockerfile
ARG PYVERSION=3.11

FROM python:$PYVERSION

ENV PATH=/app/src/bin:$PATH

RUN apt update -y && apt install -y wget

ADD / /app/src



RUN pip3 install -r /app/src/requirements.txt

RUN mkdir -p /app/src/bin
RUN ln -sf /app/src/convert.py /app/src/bin/convert
RUN chmod +x /app/src/convert.py
RUN chmod +x /app/src/bin/convert

CMD ["/bin/bash"]

```

### Step 2: Build the Container Image

All of the files needed for this example have been copied to [ImageConversion](ImageConversion).

Let's build our container image and give it a name:

```bash
docker build -t image-convert:latest ./ImageConversion
```

We could also build an alternative version with an older version of python if we needed, say for an older system:

```bash
docker build -t image-convert:python-3.9 --build-arg PYVERSION=3.9 ./ImageConversion
```

This works by overriding the default ARG on line 1 of our Dockerfile from 3.11 to 3.9 and thus changes our base
container from Python 3.11 to Python 3.9.

### Step 3: Run the Container

Now, let's start our container:

```bash
docker run -it -v ./:/output image-convert
```

If we type `convert` and press enter, you'll see our script is invoked!

### Step 4: Use the Container

Let's use our conversion script.

First, we'll download an image:

```bash
wget http://farm8.staticflickr.com/7441/9539317874_8b108e4489_z.jpg  -O  /output/image.jpg
```

And then, we'll convert it with our custom script:

```bash
convert /output/image.jpg /output/image_gray.jpg L
```

### Running without Entering the Container

Alternatively, we could have run a conversion without ever entering the container by simply placing the command after
the image URI. Because we've added our script to the $PATH variable, we can just run:

```bash
docker run --rm -v ./:/output image-convert convert /output/image.jpg /output/image_rgb.jpg RGB
```