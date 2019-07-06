# X-COM: UFO Defense

## App Lay-out

Our App relies on two Docker containers; A Postgres Database
and a Python Flask app that performs data process and exposes REST endpoints.

The two containers are designed to be hosted by a VM or bare metal host machine.

## Provisioning Host Machine

This guide targets on-site deployment where our host machine is a bare metal system
or a VM.

We'll assume our host is a
Debian 9 system (thus the following commands are Debian-specific).

### Dependencies

* Docker CE
* Docker Compose

### Install Docker

First and foremost we'll need to install Docker CE.

```shell
# Install Pre-Reqs
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/debian \
   $(lsb_release -cs) \
   stable"

# Install Docker CE
sudo apt-get update
sudo apt-get install docker-ce
```

### Install Docker Compose

Next we need to install the orchestration tool `docker-compose`.

```shell
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
## Make the binary executable
sudo chmod +x /usr/local/bin/docker-compose
```

## Provisioning Host Machine

Once our host machine is provisioned we can provision the app itself.

### Set-Up

Copy this repository onto the host machine, then run the following command in
the project root directory (where the `docker-compose.yml` file is located).

```shell
sudo docker-compose up -d
```

To check that the app is up run `docker container ls`. You should observe something
similar to the following.

```text
$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                            PORTS                    NAMES
39dc50389a95        xcom:latest         "python3 x_com_app.py"   8 seconds ago       Up 6 seconds (health: starting)   0.0.0.0:5000->5000/tcp   x-com-ufo-defense_flask_1
b3d993bb3d30        postgres:latest     "docker-entrypoint.s…"   10 seconds ago      Up 8 seconds (health: starting)                            x-com-ufo-defense_db_1
```

Now the app is ready to receive HTTP requests at `<host_machine_ip>:5000/<endpoint_name>`.

## Accessing the App

Once the app has been provisioned it will expose port `5000` and the following endpoints:

* `/total_sightings`: Total number of UFO sightings.
* `/unique_ship_shapes`: Total number of unique shapes of alien ships across all sightings.
* `/evac_priorties`: Top-10 Cities in the United States with the most UFO sightings in descending order.
* `/closest_to_area_52`: Information about UFO sightings closest to Area 52.

Each endpoint responds to `GET` requests and does not require a query string.

### Tear Down

In order to de-provision the app including removing all containers and Docker networks
run the following command.

```shell
sudo docker-compose down
```

Note that database information *is persistent* between container starts.

## Initial Population of the Database

Once the app is provisioned for the first time the Database will be empty. We need
to dump information from the CSV file into the database.

For the moment the CSV file along with a parsing script are injected directly into the
`postgres` container used by the app. While this approach is *far from ideal*
it demonstrate what we're trying to accomplish.

First we'll need to get the ID of the container via `docker container ls`

```text
$ docker container ls
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                            PORTS                    NAMES
39dc50389a95        xcom:latest         "python3 x_com_app.py"   8 seconds ago       Up 6 seconds (health: starting)   0.0.0.0:5000->5000/tcp   x-com-ufo-defense_flask_1
b3d993bb3d30        postgres:latest     "docker-entrypoint.s…"   10 seconds ago      Up 8 seconds (health: starting)                            x-com-ufo-defense_db_1
```

Then we'll use `docker exec` to trigger the parsing script which will load data
from the CSV file into a database. Note that our database makes use of persisent
storage volumes so it won't be necessary to run this command more than once.

```shell
sudo docker exec -it <container_id> /opt/data_munging_tools/csv_to_SQL.sh
```

## Sample Outputs

Here are some [outputs generated](./sample_outputs.md) using the app.
