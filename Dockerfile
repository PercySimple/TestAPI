# set base image
FROM python

ADD ./src/app.py .

# set the working directory in the container
WORKDIR /code

# COPY the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt
RUN pip install requests python-dotenv

# copy the content of the local src directory to the working directory
COPY src/ .

# command to run on container start
CMD [ "python", "app.py" ]