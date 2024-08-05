create a minio folder in current dir: 

    mkdir -p $(PWD)/minio/data

install and run a minio docer instance in pwd : 

    docker run \   -p 9000:9000 \   -p 9001:9001 \
       --user $(id -u):$(id -g) \
       --name minio1 \
       -e "MINIO_ROOT_USER=ROOTUSER" \
       -e "MINIO_ROOT_PASSWORD=CHANGEME123" \
       -v $(PWD)/minio/data:/data \
       quay.io/minio/minio server /data --console-address ":9001"