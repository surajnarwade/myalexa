FROM fedora:latest

MAINTAINER Suraj Narwade <surajnarwade353@gmail.com>

RUN dnf update -y && dnf clean all

RUN dnf -y install gcc gcc-c++ python-devel libxslt-devel libffi-devel openssl-devel redhat-rpm-config nss_wrapper gettext findutils && dnf clean all

RUN useradd -d /code -u 1001 -o -g 0 alexa 


COPY . /code


WORKDIR /code


RUN pip install -r requirements.txt 

EXPOSE 5000

RUN chown -R 1001:0 /code && chmod -R ug+rwx /code && \
    find /code -type d -exec chmod g+x {} +


USER 1001

CMD ["/code/run.sh"]

