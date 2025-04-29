#! /bin/bash

LABEL_SELECTOR="app=robin-master"
NAMESPACE="robinio"
ACTIVE_MASTER_POD_NAME=$(kubectl get pods -n $NAMESPACE -l $LABEL_SELECTOR -o jsonpath='{.items[*].metadata.name}')

kubectl exec -t -n $NAMESPACE $ACTIVE_MASTER_POD_NAME -- /bin/bash -c '
db_host=$(cat /etc/pgsqlha/db_server);
db_port=$(cat /etc/pgsqlha/db_port);
db_password=$(cat /etc/pgsqlha/db_password);
db_user=$(cat /etc/pgsqlha/db_user);
PGPASSWORD=$db_password psql -U $db_user -h $db_host -p $db_port robin -c "alter table ldap_servers ADD COLUMN use_ssl BOOLEAN NOT NULL DEFAULT FALSE"'