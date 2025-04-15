# Jupyter and Docker

Jupyter is a ubiquitous tool for Data Science. Using Jupyter within Docker is a powerful combination that creates
reliable and consistent environemtns for Data Science.

## Official Jupyter Containers

The Jupyter project has released a set of containers that can be easily used to run Jupyter locally without so much as a
Python installation

They have an [entire guide](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html) on how to
select which container to use. The high-level summary is:

- For Python data science,
  the [SciPy](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-scipy-notebook)
  notebook works great
- For general data science in Python, R, or Julia,
  the [Data Science](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-datascience-notebook)
  notebook is optimal
- For ML tasks,
  the [PyTorch](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html#jupyter-pytorch-notebook)
  notebook may be best.

## Running Official Jupyter Containers Locally

While we cannot replicate this within Coder, you can run Jupyter from Docker and use it on your local machine. You will
need to download and install Docker desktop to do this, and it will not work from within Coder.

Let's use the SciPy notebook as an example:

```bash
docker run  
  -it     # interactive for Token
  -v ./:/home/jovyan/work # mount a directory to /home/jovyan/work
  -e NOTEBOOK_ARGS="--ip 0.0.0.0 --port 8888"  # the args - set IP and Port
  -p 8888:8888    # set the port exposure
  --rm  # remove it
  quay.io/jupyter/scipy-notebook:python-3.11  # the scipy container
```

The output will container a URL that looks like:

```bash
http://127.0.0.1:8888/lab?token=[TOKEN HERE]
```

Click on this link or copy/paste to a browser and you will have Jupyter up and running! As long as you only save your
notebooks to the `work` directory, you will never lose work since that directory is mounted to the host system.

## Building Custom Jupyter Containers

We will cover how to build custom Jupyter containers in the next set of hands-on activities