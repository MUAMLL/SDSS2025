# Networking with Docker

One of the powerful features of Docker that we have not looked at thus far is the networking capabilities.

Docker containers run on a Docker network, and this network can be used to enable communication or collaboration between
containers.

We'll see things like Microservice architectures and Docker Compose in the Advanced Section, but for now, let's use
these networking capabilities for a server + client model
### Step 0: Creating the Network

To connect our client and server, we'll need a docker network. Let's create one:
```bash
docker network create my-network
```

### Step 1: Starting the Database

Let's start a PostgreSQL database running in Docker. We can use the official PostgreSQL image and using some environment
variables, we can configure the passsword. We need to specify the network here:

```bash
docker run --rm --name postgres -d -e POSTGRES_PASSWORD=mypassword --network my-network postgres:15
```

### Step 2: Connecting with PSQL

Now, let's connect to our database using the `docker exec` command:

```bash
docker exec -it postgres psql -U postgres
```

This command executes the command `psql -U postgres` on the container named `postgres`.

Now we can create a table and add a couple of rows:

```sql
CREATE TABLE mytable
(
    id          SERIAL PRIMARY KEY,
    description TEXT
);

INSERT INTO mytable(description)
VALUES ('hello'),
       ('world');
```

### Step 3: Connecting from a Python Client

To see how the docker network functions, let's create a Python container while the database container is still up and
running with our scripts mounted. We'll need to specify the same network as the server for our client to see it:

```bash
docker run --rm -it -v ./scripts:/code:ro --network my-network python:3.11 /bin/bash
```

Once we're in the container, let's install a PostgreSQL Python Client:
```bash
pip3 install psycopg2
```

And now let's run our Python Script, named `database.py`:
```python
import psycopg2 as sql
from pprint import pprint

conn = sql.connect(host="postgres", user="postgres", password="mypassword")

with conn.cursor() as cur:
    cur.execute("SELECT * FROM mytable;")
    results = cur.fetchall()

pprint(results)
```

To run it:
```bash
python3 /code/database.py
```

### Step 4: Teardown & Cleanup

We can now remove our client container by simply exiting, and then to remove our server (since we specified `--rm`):
```bash
docker stop postgres
```

and then we can remove our network:
```bash
docker network rm my-network
```

