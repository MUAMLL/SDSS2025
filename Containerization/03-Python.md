# Using Official Containers: Python

Recall from the slides that we can use official images to run docker containers that already have the software we need.

Let's look at that now with Python.

### 1. Building a Script

Let's build a simple Python Script:

```python
from random import random
import sys

assert len(sys.argv) == 2, "Wrong nargs."

n: str = sys.argv[1]
mylist: list = [None] * int(n)

for i in range(int(n)):
    rand: float = random()
    mylist[i] = rand

print(max(mylist))
print(min(mylist))
```

This script has been copied to the `scripts` directory.

### 2. Starting a Container

Let's start a Python container with the scripts directory mounted. By default, the Python container will enter Python
REPL, so let's enter interactively and set the entrypoint to `/bin/bash`

```bash
docker run -it -v ./scripts:/code python:3.11 /bin/bash
```

From inside the container, we can now run our script:

```bash
python3 /code/simple.py 5
```

### 3. Running the Process from Outside the Container

We could also choose to perform this action by **only** changing the entrypoint and allowing the container to exit.

This command will create the container, run the script, print the results, exit, and remove the container:

```bash
docker run --rm -v ./scripts:/code:ro python:3.11 python /code/simple.py 5
```

---

# Using Community Containers: Python

In our simple example, we are using only built-in Python functions because the `python:3.11` container is mostly used as
a base for other containers and does not contain any external packages. Let's now use a community-based Python container
that contains many more packages relevant to data science tasks.

The set of steps does not chage.

We first will need something to run. In your lab / classroom, this may be the software you are looking to run.

```python
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris

X, y = load_iris(return_X_y=True)

model = DecisionTreeClassifier()

model.fit(X, y)

accuracy = model.score(X, y)

print(f"Model Accuracy is {accuracy * 100:.02f}%")

```

Now, let's run our script, using a SciPy Software stack published by the Jupyter project:

```bash
docker run --rm -v ./scripts:/code:ro --entrypoint python quay.io/jupyter/scipy-notebook:python-3.11 /code/decisiontree.py
```



### Entrypoint vs. Command

These two examples have illustrated an important point of difference between container entrypoints and commands.

Both specify how a container starts, but they must be overriden differently:

- Commands can be overriden by passing the entire command following the image URI
- Entrypoints must be overriden by passing the executable to `--entrypoint` and the commands must be passed following
  the image URI

---

# Reviewing the Power of Containerization
Let's review the power of what we've seen so far:
- Our host system does not need to have Python installed, and we do not have to worry about versions or dependencies 
- We did not have to build any containers ourselves, but rather relied on open-source published containers
- We only wrote the Data Science we wanted to perform, and then used open-source container images with our script to run our Data Science
- **This workflow is reliable, consistent, and portable to any computing environment with a container runtime**