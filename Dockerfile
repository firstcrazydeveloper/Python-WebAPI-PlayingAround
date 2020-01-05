FROM python:3
WORKDIR /webapp

# copy and publish app and libraries
WORKDIR /webapp/

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /webapp/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /webapp

# ENTRYPOINT [ "python" ]
CMD [ "python", "SampleController.py" ]
