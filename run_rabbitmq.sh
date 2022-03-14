#!/bin/sh

( sleep 5;
rabbitmqctl add_user $RABBITMQ_USER $RABBITMQ_PASSWORD 2>/dev/null ;
rabbitmqctl set_user_tags $RABBITMQ_USER administrator ;
rabbitmqctl add_vhost myvhost ;
rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*" 2>/dev/null ; 
rabbitmq-server;)
