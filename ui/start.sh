# this script basically stops everything and restarts them but re-builds 1 service of choice in the meantime
# run the start.sh with a parameter or no param (default will be backend)
docker-compose down && docker-compose build ${1:-backend} && docker-compose up