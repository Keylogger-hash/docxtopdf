FROM rabbitmq:3-management-alpine


COPY run_rabbitmq.sh .
EXPOSE 15672
EXPOSE 5672
RUN ["bash","run_rabbitmq.sh"]
