# set the base image
FROM python:3.8

# set the working directory in the container
WORKDIR /app

# copy the requirements file into the container
COPY requirements.txt .

# install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# copy the source code into the container
COPY . .

# set the environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV DOTA_BACKEND_API=https://dota2-api-backend.onrender.com

# expose the port on which the Flask app will listen
EXPOSE 5000

# start the Flask app
CMD ["gunicorn", "app:app"]
