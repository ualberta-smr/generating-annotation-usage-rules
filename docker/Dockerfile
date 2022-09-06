FROM openjdk:8-jdk-alpine

RUN apk update \
    && apk add ca-certificates wget \
    && update-ca-certificates

ENV MAVEN_VERSION 3.8.6

RUN apk update \
 \
 && apk add \
      py3-psutil \
      python3 \
      yaml-dev \
 && ln -s /usr/bin/python3 /usr/bin/python \
 && ln -s /usr/bin/pip3 /usr/bin/pip \
 && pip install --upgrade pip \
 \
 && apk add git bash

RUN wget http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  tar -zxvf apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  rm apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  mv apache-maven-$MAVEN_VERSION /usr/lib/maven

ENV PATH=${PATH}:/usr/lib/maven/bin

WORKDIR /pipeline

ADD bin/ /pipeline/bin
RUN chmod -R +x /pipeline/bin
ENV PATH=/pipeline/bin:${PATH}

ADD rule-miner /pipeline/rule-miner
ADD ui /pipeline/ui
ADD configuration.json /pipeline/

ENV CONFIG_PATH /pipeline/configuration.json

RUN mvn clean package -f ./rule-miner/miner/pom.xml

VOLUME [ "/pipeline/mining-sources", "/pipeline/lib-sources" ]

CMD ["bash"]