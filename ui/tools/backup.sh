# Reference: https://gist.github.com/spalladino/6d981f7b33f6e0afe6bb

# Backup
docker exec CONTAINER /usr/bin/mysqldump -u root --password=password database > db_backup.sql

# Restore
cat db_backup.sql | docker exec -i CONTAINER /usr/bin/mysql -u root --password=password database