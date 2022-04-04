#!/bin/sh
# Import data

HOST=mongodb

echo "$(date -u) Import started" > status

gzip -d convocatorias.csv.gz
gzip -d juridicas_1.csv.gz
gzip -d juridicas_2.csv.gz

cp convocatorias-headers.csv c1.csv
cp juridicas-headers.csv j1.csv
cp juridicas-headers.csv j2.csv

cat convocatorias.csv >> c1.csv
cat juridicas_1.csv >> j1.csv
cat juridicas_2.csv >> j2.csv


mongoimport --host $HOST --type csv -d subvenciones -c convocatorias --headerline --drop c1.csv
mongoimport --host $HOST --type csv -d subvenciones -c juridicas --headerline --drop j1.csv
mongoimport --host $HOST --type csv -d subvenciones -c juridicas --headerline j2.csv

rm *.csv

echo "$(date -u) Import done!" >> status
