# this script basically stops everything and restarts them but re-builds 1 service of choice in the meantime
# run the start.sh with a parameter or no param (default will be backend)
docker-compose down
# start.sh localhost

host="http://${1:-localhost}"
backend="$host:5000"
tutorial="$host:8000/README.md"

RVT_BACKEND="${backend}" RVT_TUTORIAL="${tutorial}"; docker-compose up --build -d