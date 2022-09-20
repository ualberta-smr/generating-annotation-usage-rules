# ATTENTION!!!
# This dockerfile is meant to be run from the root directory

####################################################################################
# This is a multi-stage build where in the first stage, we build the miner and
# cache the dependencies; and in the second stage, we simply use the already built
# jar file and copy it over to our main container.
# 
# The main purpose of the multi-stage build it to improve the overall built time 
####################################################################################

############################
# Building the miner
############################
FROM docker as base

RUN apk update \
    && apk add ca-certificates wget \
    && update-ca-certificates

# add java 8
RUN apk add --no-cache openjdk8

# set the environment variables
ENV LANG=C.UTF-8 \
    JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
ENV PATH=/usr/lib/jvm/java-1.8-openjdk/bin/:${PATH}
ENV MAVEN_VERSION 3.8.6

# download maven
RUN wget http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  tar -zxvf apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  rm apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  mv apache-maven-$MAVEN_VERSION /usr/lib/maven

# add maven to path
ENV PATH=${PATH}:/usr/lib/maven/bin

WORKDIR /pipeline

# copy the rule-miner directory 
ADD rule-miner /pipeline/rule-miner
# build the miner and cache the .m2 directory.
RUN --mount=type=cache,target=/root/.m2 mvn clean package -f /pipeline/rule-miner/miner/pom.xml

############################
# Creating the environment
############################
FROM docker

RUN apk update \
    && apk add ca-certificates wget \
    && update-ca-certificates

# install java 
RUN apk add --no-cache openjdk8

# set the environment variables
ENV LANG=C.UTF-8 \
    JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
ENV PATH=/usr/lib/jvm/java-1.8-openjdk/bin/:${PATH}
ENV MAVEN_VERSION 3.8.6

# download maven
RUN wget http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  tar -zxvf apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  rm apache-maven-$MAVEN_VERSION-bin.tar.gz && \
  mv apache-maven-$MAVEN_VERSION /usr/lib/maven

ENV PATH=${PATH}:/usr/lib/maven/bin

# install python and some other dependencies
RUN apk update \
 \
 && apk add \
      py3-psutil \
      python3 \
      py3-pip \
 && ln -s /usr/bin/python3 /usr/bin/python \
#  && ln -s /usr/bin/pip3 /usr/bin/pip \
 && pip install --upgrade pip \
 && pip install requests randomname gitpython \
 \
 && apk add git bash

WORKDIR /pipeline

# copy the already built jar file from the previous stage
COPY --from=base /pipeline/rule-miner/miner/target/rule-miner.jar /pipeline/rule-miner.jar

VOLUME [ "/pipeline/mining-sources", "/pipeline/lib-sources", "/pipeline/exports"]

# copy the important directories and files
ADD violation-detector /pipeline/detector
ADD rule-miner/bin /pipeline/bin

# add all the scripts to the path
RUN chmod -R +x /pipeline/bin
ENV PATH=/pipeline/bin:${PATH}

# copy the configuration
ADD config /pipeline/config

# start from the bash
CMD ["bash"]
