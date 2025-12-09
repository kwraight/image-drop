# base image
FROM python:3.11.9

# exposing default port for streamlit
EXPOSE 8501

### set-up packages
USER root
RUN apt-get update \
    && apt-get install wget nano -y

# copy over and install packages
COPY webApp/requirements.txt /code/requirements.txt
RUN pip3 install -r /code/requirements.txt

# copying stuff over
# COPY *.py ./code/
COPY webApp/front_page.py ./code/front_page.py
COPY webApp/pages/* ./code/pages/
COPY webApp/pages/gallery/* ./code/pages/gallery/

# fudge for CERN image
RUN mkdir /.streamlit
COPY webApp/temp_id  /.streamlit/.stable_random_id
RUN chmod 777 /.streamlit/.stable_random_id
RUN chmod -R 777 /code/

# run as not root
RUN adduser appuser
USER appuser

WORKDIR /code

# match exposed port
CMD ["streamlit", "run", "front_page.py","--server.port=8501"]
