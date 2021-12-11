FROM python:3.9

# base directory is /code
WORKDIR /code

# install pipenv to manage dependencies and run the app
RUN pip install pipenv

# copy dependency files so that we can create the environment
COPY ./Pipfile* /code/

# install the dependencies
RUN python -m pipenv install

# copy source files
COPY ./src /code/src
COPY ./data /code/data

# set the pythonpath to /code/src so that 
# we will be able to find custom dependencies
ENV PYTHONPATH /code/src

# run the app
CMD ["python", "-m", "pipenv", "run", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "5000"]