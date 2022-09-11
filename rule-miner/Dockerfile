# ATTENTION!!!
# This dockerfile is meant to be run from the root directory
FROM docker

RUN apk update \
    && apk add ca-certificates wget \
    && update-ca-certificates

RUN apk add --no-cache openjdk8

ENV LANG=C.UTF-8 \
    JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk

ENV PATH=/usr/lib/jvm/java-1.8-openjdk/bin/:${PATH}
ENV MAVEN_VERSION 3.8.6

RUN apk update \
 \
 && apk add \
      py3-psutil \
      python3 \
      yaml-dev \
      py3-pip \
 && ln -s /usr/bin/python3 /usr/bin/python \
#  && ln -s /usr/bin/pip3 /usr/bin/pip \
 && pip install --upgrade pip \
 && pip install requests randomname \
 \
 && apk add git bash

RUN wget http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  tar -zxvf apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  rm apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  mv apache-maven-$MAVEN_VERSION /usr/lib/maven

ENV PATH=${PATH}:/usr/lib/maven/bin

WORKDIR /pipeline

VOLUME [ "/pipeline/mining-sources", "/pipeline/lib-sources", "/pipeline/exports"]

# copy the important directories and files
ADD rule-miner /pipeline/rule-miner
ADD violation-detector /pipeline/detector

RUN mv /pipeline/rule-miner/configuration.json /pipeline/configuration.json
# add all the scripts to the path
RUN mv /pipeline/rule-miner/bin /pipeline/bin
RUN chmod -R +x /pipeline/bin
ENV PATH=/pipeline/bin:${PATH}

# build the miner
RUN mvn clean package -f ./rule-miner/miner/pom.xml

# start from the bash
CMD ["bash"]