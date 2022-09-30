# Kafka
After installation, we proceed to start Zookeeper, which is a dependency (as of the curent version) to run Kafka, before we run Kafka server.
```sh
# Running the following command will start all the needed services in the correct order, keep it running in the background.
bin/zookeeper-server-start.sh config/zookeeper.properties
zookeeper-server-start /usr/local/etc/kafka/zookeeper.properties

# On another terminal session run:
bin/kafka-server-start.sh config/server.properties
kafka-server-start /usr/local/etc/kafka/server.properties

# Create topic as follows:
kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test

# Check if topic is created:
kafka-topics --bootstrap-server localhost:9092 --list

# Start producer:
kafka-console-producer --broker-list localhost:9092 --topic test

# Start consumer:
kafka-console-consumer --bootstrap-server localhost:9092 --topic test --from-beginning
```


# Python
## FastAPI
We start the application with `uvicorn`. [$$$explain what's uvicorn]
```sh
# Basic start
uvicorn run:app --reload

# with ports
uvicorn run:app --port 8000 --reload

# when start is within a directory; here its under `src`
uvicorn src.main:app --reload
```

## VirtualEnv
This is to start VirtualEnv in Python. Development will be done in `virtualenv`.
```python
# Create the virtual environment (needed only once in the beginning):
python -m venv venv

# Start the virtual environment:
source venv/bin/activate

# To close the environment:
deactivate
```


# Spark