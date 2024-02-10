# Use official Python runtime as a parent image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
ARG PROJ_DIR=/my_proj


RUN mkdir -p ${PROJ_DIR}
COPY ./project ${PROJ_DIR}

WORKDIR ${PROJ_DIR}
# Install dependencies

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY ./compose/django/entry.sh /entry.sh
RUN chmod +x /entry.sh
ENTRYPOINT ["/entry.sh"]

