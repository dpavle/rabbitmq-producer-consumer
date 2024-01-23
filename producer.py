import ssl
import pika

class PikaClient:
    '''Establish a connection to RabbitMQ using the Pika client library.'''
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
                    rabbitmq_user="producer",
                    rabbitmq_password="producer123")

channel = client.connection.channel()

# Declare a stream, named test_stream
#channel.queue_declare(
#	queue="test_fix_stream",
#	durable=True,
#	arguments={"x-queue-type": "stream",
#               "x-max-length-bytes": 2147483648,
#               "x-max-age": "30D"}
#)

# Test FIX message from https://fixsim.com/sample-fix-messages
FIX="8=FIX.4.49=28935=834=109049=TESTSELL152=20180920-18:23:53.67156=TESTBUY16=113.3511=63673064027889863414=3500.000000000015=USD17=2063673064633531000021=231=113.3532=350037=2063673064633531000038=700039=140=154=155=MSFT60=20180920-18:23:53.531150=F151=3500453=1448=BRK2447=D452=110=151"

# Endlessly publish messages to test_stream
N = 0
while True:
    N += 1
    channel.basic_publish(
		exchange="",
		routing_key="test_fix_stream",
		body=f"{FIX}: {N}"
		)
