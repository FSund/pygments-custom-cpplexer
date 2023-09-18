FROM texlive/texlive:latest

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    make \
    git \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/FSund/pygments-custom-cpplexer.git \
    && cd pygments-custom-cpplexer \
    && python setup.py install
