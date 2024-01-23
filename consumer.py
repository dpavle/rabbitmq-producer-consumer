import time
import ssl
import pika

def process_message(msg):
    print("Processing message...")
    print(f"[x] Recieved {str(msg)}")
    time.sleep(0.1)
    print("Message successfully processed")
    return

class PikaClient:
    def __init__(self, rabbitmq_host, rabbitmq_port, rabbitmq_user, rabbitmq_password):
        # Establishing a pika connection to the RabbitMQ server
        credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)

        context = ssl.create_default_context(
                cafile="./tls/ca_certificate.pem"
        )

        context.verify_mode = ssl.CERT_REQUIRED
        context.load_cert_chain("./tls/client_rabbitmq_certificate.pem",
                                "./tls/client_rabbitmq_key.pem")

        ssl_options = pika.SSLOptions(context, rabbitmq_host)

        params = pika.ConnectionParameters(host=rabbitmq_host,
                                        port=rabbitmq_port,
                                        credentials=credentials,
                                        ssl_options=ssl_options)

        self.connection = pika.BlockingConnection(params)

client = PikaClient(rabbitmq_host="rabbitmq",
                    rabbitmq_port=5673,
                    rabbitmq_user="consumer",
                    rabbitmq_password="consumer123")

channel = client.connection.channel()

# Declare a stream, named test_stream
#channel.queue_declare(
#        queue="test_stream",
#        durable=True,
#        arguments={"x-queue-type": "stream"}
#)

# Define a function that is called on incoming messages
def callback(ch, method, properties, body):
    process_message(body)

    # Acknowledge the message
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Set the consumer QoS prefetch
channel.basic_qos(
	prefetch_count=100
)

# Consume messages published to the stream
channel.basic_consume(
	"test_fix_stream",
	callback,
)

# Start consuming
channel.start_consuming()
client.connection.close()
