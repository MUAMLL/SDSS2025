# SDSS 2025 Short Course Repository

This repo contains the resources used for 2 short courses presented at SDSS 2025: <br />

1. _Building Containerized Applications for Data Science_
2. _Accelerating Data Science Workflows with Kubernetes_

The goal of these resources is to enable Data Science students, practitioners, experts, and researchers to build
familiarity and competency with using Docker and Kubernetes for Data Science workflows

All of the compute used for these tutorials was performed on
the [National Research Platform](https://nationalresearchplatform.org/)

**Content Authors:**

J. Alex Hurt, University of Missouri

## Content

- [Containerization](./Containerization)
  - [Slides](./Containerization/ContainerizationSlides.pdf) - The slides used for the course
  - [Walkthough Markdown Files (01-08.md)](./Containerization) - Markdown files walking through the hands-on concepts
  - Examples
    - [Building Custom Containers](./Containerization/ImageConversion) - Example of building a simple Python Application for Image Processing
    - [Dashboard](./Containerization/dashboard) - Example of a Data Science Dashboard in Docker
    - [Custom Jupyter Containers](./Containerization/GeoJupyter) - Example of Building a Custom Container with Jupyter Capabilities
- [Kubernetes](./Kubernetes)
  - [Slides](./Kubernetes/K8sSlides.pdf) - The slides used for the course
  - Jupyter Notebook Walkthroughs
    - [Config Setup](./Kubernetes/notebooks/00-Config.ipynb)
    - [Creating Persistent Storage](./Kubernetes/notebooks/01-PVC.ipynb)
    - [Creating a Pod](./Kubernetes/notebooks/02-Pod.ipynb)
    - [Creating a Job](./Kubernetes/notebooks/03-Job.ipynb)
  - Jupyter Notebook Examples
    - [CPU Jobs: Sci-Kit Learn](./Kubernetes/examples/01-SKLearn.ipynb)
    - [Running Jupyter in K8s](./Kubernetes/examples/02-Jupyter.ipynb)
    - [CPU Jobs: Sci-Kit Learn](./Kubernetes/examples/03-PyTorch.ipynb)
    - [Job Automation](./Kubernetes/examples/04-Automation.ipynb)
      
## Resources

- [Nautilus Tutorials from the GP-ENGINE Project](https://github.com/MUAMLL/gp-engine-tutorials)
- [Nautilus Resources for Researchers](https://github.com/MUAMLL/nautilus)
