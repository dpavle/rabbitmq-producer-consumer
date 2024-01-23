# RabbitMQ Consumer and Producer Scripts

These Python scripts, `consumer.py` and `producer.py`, demonstrate a simple setup for consuming and producing messages using RabbitMQ with the Pika library. The consumer script subscribes to a RabbitMQ queue, while the producer script endlessly publishes FIX messages to the same queue.

TLS encryption is configured between the consumer/producer and the RabbitMQ instance. TLS certificates and keys are read from `./tls/` by default.

## Prerequisites

- Python 3
- RabbitMQ server installed and running
- Pika library (`pip install pika`)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Configuration

### Consumer (`consumer.py`)

Edit the following parameters in the script:

- `rabbitmq_host`: RabbitMQ server hostname.
- `rabbitmq_port`: RabbitMQ server port.
- `rabbitmq_user`: RabbitMQ username.
- `rabbitmq_password`: RabbitMQ password.

### Producer (`producer.py`)

Edit the following parameters in the script:

- `rabbitmq_host`: RabbitMQ server hostname.
- `rabbitmq_port`: RabbitMQ server port.
- `rabbitmq_user`: RabbitMQ username.
- `rabbitmq_password`: RabbitMQ password.

Ensure that SSL certificates and keys are correctly configured in the script for secure connections. By default, the script will look for keys/certificates under the following:  `./tls/client_rabbitmq_(key / certificate).pem`.

## Usage

### Consumer (`consumer.py`)

Run the consumer script:

```bash
python consumer.py
```

The consumer will start listening for messages on the specified RabbitMQ queue.

### Producer (producer.py)

Run the producer script:

```bash
python producer.py
```

The producer will continuously publish FIX messages to the RabbitMQ queue.

### Notes

- Make sure to match the queue name in both scripts (test_fix_stream) for proper communication.
- Uncomment and configure the queue declaration parts in both scripts if necessary.
- Adjust the QoS prefetch count in the consumer script based on your application requirements.

### Acknowledgments

These scripts serve as a basic example for RabbitMQ message consumption and production. Customize them according to your specific use case and requirements.

Feel free to contribute or report issues by creating a pull request or opening an issue in the [GitHub repository](https://github.com/dpavle/rabbitmq-producer-consumer).