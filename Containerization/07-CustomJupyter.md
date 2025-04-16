# Building Custom Jupyter Containers

As previously mentioned, Jupyter is ubiquitous for Data Science workflows. As such, being able to use Jupyter in Docker
is highly effective and powerful.

While there exist many community containers, knowing how to build your own is incredibly helpful.

### Step 1: Starting from Jupyter Base

While not explicitly required, the most effective way to build a customized Jupyter container is to use one of the
community published Jupyter containers as a base image and then customize from there.

Common starting places would be:

```dockerfile
# for Python-based Data Science
FROM quay.io/jupyter/scipy-notebook:latest

# for R-based Data Science
FROM quay.io/jupyter/r-notebook:latest

# for any/all DataScience - best used for flexibility
FROM quay.io/jupyter/datascience-notebook:latest

# for ML Workflows
FROM quay.io/jupyter/pytorch-notebook:latest
FROM quay.io/jupyter/tensorflow-notebook:latest

 
```

**Note**: Do not override the `CMD` or `ENTRYPOINT` for these containers as they have been configured

### Step 2: Dockerfile

While these official Jupyter images contain many of the packages that you may need for Data Science, it is common that
you may have custom dependencies or a missing package.

We can fix this using `pip` installs in a custom Dockerfile.

Say, for example, that we want to do some Geospatial Data Processing. We may need to install some additional packages
not present in the SciPy notebook:

```dockerfile
FROM quay.io/jupyter/scipy-notebook:latest

RUN pip install geopandas shapely geoplot

```

And that's it! From this simple 2-line Dockerfile, we have everything we need to do our data science!

### Step 3: Build the Custom Container

With our We've placed our Dockerfile in the [GeoJupyter](GeoJupyter) directory. We are now ready to build:

```bash
docker build -t geo-jupyter:latest ./GeoJupyter
```

### Step 4: Start the Container

Start your custom container identically to how you would for a community-based container:

```bash
docker run  
  -it     # interactive for Token
  -v ./:/home/jovyan/work # mount a directory to /home/jovyan/work
  -e NOTEBOOK_ARGS="--ip 0.0.0.0 --port 8888"  # the args - set IP and Port
  -p 8888:8888    # set the port exposure
  --rm  # remove it
  geo-jupyter:latest
```

### Step 5: Using the Container

Once we navigate to the link, we can use Jupyter to perform some geospatial analysis. For this example, let's build a
map of the U.S. with Cities. The notebook is called [GeoVis.ipynb](./GeoJupyter/GeoVis.ipynb)

---

## GPU-Enabled Jupyter Containers

Many modern Data Science workflows rely on GPU-enabled code, both in Python libraries, as well as within Jupyter environments.

We'll note here that this entire workflow can work with GPU-enabled versions of the Jupyter containers.

The Jupyter Project provides GPU-enabled versions of several of their containers. You can read more [here](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#cuda-enabled-variants)

The basic steps to use a GPU-enabled container do not change. Our Dockerfile should still inherit from Jupyter, but this from the GPU-enabled version.

```dockerfile

FROM quay.io/jupyter/pytorch-notebook:cuda12-python-3.11.8

RUN pip install geopandas shapely geoplot

```

We should still build our container the same way:
```bash
docker build -t geo-jupyter:gpu-latest [Path to Directory with Dockerfile]
```

And then when we run the container, we'll need to specify that the GPUs should be passed into the container:
```bash
docker run  
  -it     # interactive for Token
  -v ./:/home/jovyan/work # mount a directory to /home/jovyan/work
  -e NOTEBOOK_ARGS="--ip 0.0.0.0 --port 8888"  # the args - set IP and Port
  -p 8888:8888    # set the port exposure
  --rm  # remove it
  --gpus all # pass in the GPUs
  geo-jupyter:gpu-latest
```