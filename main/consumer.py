import pika

params = pika.URLParameters('amqps://rvxsgnnt:06gGZO8nLd5aP7SlGJE6yUV4FrxAYzw2@kangaroo.rmq.cloudamqp.com/rvxsgnnt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main')


def callback(ch, method, properties, body):
    print('Received in main queue [Flask]')
    print(body)


channel.basic_consume(queue='main', on_message_callback=callback)

print('Started Consuming...')

channel.start_consuming()

channel.close()
