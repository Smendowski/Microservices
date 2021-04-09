import pika

params = pika.URLParameters('amqps://rvxsgnnt:06gGZO8nLd5aP7SlGJE6yUV4FrxAYzw2@kangaroo.rmq.cloudamqp.com/rvxsgnnt')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='Hello')
