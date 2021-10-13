import pika

params = pika.URLParameters('amqps://xaoqrcjf:X-D5jGWtuRA4qGt2tUSCVB4c3Ewtt8pH@snake.rmq2.cloudamqp.com/xaoqrcjf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print("Started Consuming")

channel.start_consuming()

channel.close()