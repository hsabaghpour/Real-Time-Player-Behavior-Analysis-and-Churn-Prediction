
Table of Contents:

	1.	Overview
	2.	Prerequisites
	3.	Setting Up Kafka and Zookeeper on Docker
	•	Docker Compose Setup
	•	Running the Kafka and Zookeeper Containers
	4.	Interacting with Kafka
	•	Creating Kafka Topics
	•	Producing Messages
	•	Consuming Messages
	5.	Useful Commands Summary
	6.	Next Steps in the Project

1. Overview

This document outlines the steps to set up Apache Kafka using Docker for real-time message streaming. The setup is a foundational part of the “Real-Time Player Behavior Analysis and Churn Prediction” project, where Kafka will serve as the messaging system for data streaming.

2. Prerequisites

	•	Docker installed on your machine (Mac, Linux, or Windows).
	•	Basic knowledge of using the terminal.
	•	Installed Kafka client commands (kafka-console-producer.sh, kafka-console-consumer.sh) available in the Docker container.


3. Setting Up Kafka and Zookeeper on Docker

Docker Compose Setup:

We used Docker Compose to run Kafka and Zookeeper. Here’s the docker-compose.yml file that sets up both services:


version: '2'
services:
  zookeeper:
    image: 'bitnami/zookeeper:latest'
    environment:
      - ALLOW_ANONYMOUS_LOGIN=yes
    ports:
      - '2181:2181'
  kafka:
    image: 'bitnami/kafka:latest'
    environment:
      - KAFKA_BROKER_ID=1
      - KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181
      - KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092
      - ALLOW_PLAINTEXT_LISTENER=yes
    ports:
      - '9092:9092'
    depends_on:
      - zookeeper


Save the file as docker-compose.yml.

Running the Kafka and Zookeeper Containers:

To start the services, run the following command in the directory where your docker-compose.yml file is located:


docker-compose up -d

This command will:

	•	Start Zookeeper on port 2181.
	•	Start Kafka on port 9092.

4. Interacting with Kafka

4.1. Creating a Kafka Topic

To create a new topic (in this case, test_topic), use the following command:


docker exec -it kafka-kafka-1 bash
kafka-topics.sh --create --topic test_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1


4.2. Producing Messages to the Kafka Topic

Run the producer command to start sending messages to test_topic:

docker exec -it kafka-kafka-1 bash
kafka-console-producer.sh --topic test_topic --bootstrap-server localhost:9092

After this, you can start typing your messages in the terminal, e.g.:

>Hello, this is my first Kafka message!
>This is another message.
>
>4.3. Consuming Messages from the Kafka Topic

To read messages from the test_topic:

docker exec -it kafka-kafka-1 bash
kafka-console-consumer.sh --topic test_topic --from-beginning --bootstrap-server localhost:9092


This will show the messages you produced earlier.

5. Useful Commands Summary

Command	Description
docker-compose up -d	Starts Kafka and Zookeeper containers in detached mode.
docker ps	Lists the running Docker containers.
docker exec -it kafka-kafka-1 bash	Opens a terminal in the Kafka container.
kafka-topics.sh --create --topic test_topic --bootstrap-server localhost:9092	Creates a new Kafka topic (test_topic).
kafka-console-producer.sh --topic test_topic --bootstrap-server localhost:9092	Starts producing messages to a Kafka topic.
kafka-console-consumer.sh --topic test_topic --from-beginning --bootstrap-server localhost:9092	Starts consuming messages from a Kafka topic.


6. Next Steps in the Project

After setting up Kafka:

	1.	Step 2: Data Ingestion and Storage in Kafka: Set up a Python script or PySpark job to ingest and stream player behavior data into Kafka.
	2.	Step 3: Real-Time Data Processing Using PySpark: Configure PySpark on Databricks or another environment to process the streaming data for behavior analysis.
	3.	Step 4: Build Churn Prediction Model: Use the processed data to build machine learning models for predicting player churn.



 

