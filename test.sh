#! /bin/sh

curl http://localhost:5000/data -X POST -H "Content-Type: application/json" -d '{"data":1234}'