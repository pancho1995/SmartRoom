FROM python:3.9.15-buster

RUN apt-get update && apt-get install -y

WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

#RUN pip install

# Install miniconda
# ENV CONDA_DIR /opt/conda
# RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
#      /bin/bash ~/miniconda.sh -b -p /opt/conda

# # Put conda in path so we can use conda activate
# ENV PATH=$CONDA_DIR/bin:$PATH


ENTRYPOINT ["flask"]

CMD ["run", "-h", "0.0.0.0"]




