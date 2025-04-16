# Data Science Dashboards in Docker

For our final example, we'll look at how to run a Data Science Dashboard in Docker.

### Step 1: Build the Dashboard

The first step is to build our Dashboard Application

We've done this in the [dashboard](./dashboard) directory. For this example, we've built a simple application that
allows users to select a state and see the cities present in that state.

### Step 2: Create a Dockerfile

The next step is to build a Dockerfile to contain our dashboard application.

```dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

ADD / /app

RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]

```

### Step 3: Build the Container

We'll now build our container:

```bash
docker build -t dashboard:latest dashboard
```

### Step 4: Run the Dashboard

And then run it, ensuring we map the port we need:

```bash
docker run -it -p 8501:8501 --rm dashboard:latest
```

And now we can see the dashboard at http://localhost:8501

---

## Portability

The great part of this process is that by building a containerized application, we can develop locally with the **exact
same environment** as production, since containerized solutions can be deployed to numerous cloud providers such as GCP,
AWS, and Azure. This enables great flexibility in deployment and more confidence in the functionality of our Data
Science Products.