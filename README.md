# AutoUrl
> torchserve与url检测联动

## steps

```
python url.py # generate url.pt
mkdir model_store

torch-model-archiver --model-name url \--version 1.0 \--serialized-file url.pt \--extra-files ./index_to_name.json,./MyHandler.py \--handler my_handler.py  \--export-path model_store -f

torchserve --start --model-store model_store --models url=url.mar

```

## dokcer 

```


docker run --rm --shm-size=1g \
        --ulimit memlock=-1 \
        --ulimit stack=67108864 \
        -p8080:8080 \
        -p8081:8081 \
        -p8082:8082 \
        -p7070:7070 \
        -p7071:7071 \
        --mount type=bind,source=/home/test/model_store,target=/tmp/models pytorch/torchserve:latest  torchserve --model-store=/tmp/models
```
## reference:

https://aijishu.com/a/1060000000136517#item-3

https://github.com/FrancescoSaverioZuppichini/torchserve-tryout
