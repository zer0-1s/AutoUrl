# AutoUrl
> torchserve与url检测联动

## steps

```
python url.py # generate url.pt
mkdir model_store

torch-model-archiver --model-name url \--version 1.0 \--serialized-file url.pt \--extra-files ./index_to_name.json,./MyHandler.py \--handler my_handler.py  \--export-path model_store -f

torchserve --start --model-store model_store --models url=url.mar
```
## reference:

https://aijishu.com/a/1060000000136517#item-3

https://github.com/FrancescoSaverioZuppichini/torchserve-tryout
