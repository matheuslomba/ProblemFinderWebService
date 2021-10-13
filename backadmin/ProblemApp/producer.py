import pika, json

params = pika.URLParameters('amqps://xaoqrcjf:X-D5jGWtuRA4qGt2tUSCVB4c3Ewtt8pH@snake.rmq2.cloudamqp.com/xaoqrcjf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)