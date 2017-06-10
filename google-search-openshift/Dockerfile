FROM fedora:latest
MAINTAINER Suraj Narwade <surajnarwade353@gmail.com>

RUN dnf -y update; dnf clean all
RUN dnf -y install epel-release; dnf clean all
RUN dnf -y install nodejs; dnf clean all

ADD . /src

WORKDIR /src

EXPOSE 8080

CMD ["node", "index.js"]
