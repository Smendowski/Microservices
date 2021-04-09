import pika

params = pika.URLParameters('amqps://rvxsgnnt:06gGZO8nLd5aP7SlGJE6yUV4FrxAYzw2@kangaroo.rmq.cloudamqp.com/rvxsgnnt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin queue [Django]')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming...')

channel.start_consuming()

channel.close()
