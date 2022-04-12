FROM ubuntu:16.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install netcat g++ valgrind curl make -y

WORKDIR /usr/src
RUN curl \
    --location https://github.com/Kitware/CMake/releases/download/v3.13.1/cmake-3.13.1-Linux-x86_64.sh \
    -o curl-install.sh
RUN chmod u+x curl-install.sh
RUN ./curl-install.sh --skip-license --prefix=/usr/local
