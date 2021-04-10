import pika, json, os, django

# TO USE DJANGO MODEL OUTSIDE DJANGO APP
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "microservices.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://rvxsgnnt:06gGZO8nLd5aP7SlGJE6yUV4FrxAYzw2@kangaroo.rmq.cloudamqp.com/rvxsgnnt')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('Received in admin queue [Django]')
    data = json.loads(body)
    print(data)
    product = Product.objects.get(id=data)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased')


channel.basic_consume(queue='admin', on_message_callback=callback)

print('Started Consuming...')

channel.start_consuming()

channel.close()
