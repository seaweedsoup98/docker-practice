FROM nginx:alpine

RUN apk add --no-cache curl

COPY index.html /usr/share/nginx/html/index.html
COPY default.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
