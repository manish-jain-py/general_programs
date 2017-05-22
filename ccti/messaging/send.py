#!/usr/bin/env python

import sys
sys.path.append('/usr/local/lib/python2.7/site-packages')
import pika




def send_info(message):
    print "Sending ", message
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=message)
    connection.close()