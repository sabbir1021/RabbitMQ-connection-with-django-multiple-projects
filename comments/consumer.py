
from sys import path
from os import environ

import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()
from comments.models import Comment

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost',heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()

channel.queue_declare(queue='comments')

def callback(ch, method, properties, body):
    print("Received in likes...")
    data = json.loads(body)
    print(data)
    print(properties.content_type)
    if properties.content_type == 'comment_created':
        quote = Comment.objects.create(comment=data['comment'],comment_id=data['id'], blog_id=data['blog'])
        quote.save()

channel.basic_consume(queue='comments', on_message_callback=callback, auto_ack=True)
print("-------------")
channel.start_consuming()