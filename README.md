# b64tofile

Write base64 encoded contents to files

# Run

## Local

```sh
export FILES_PATHS="/some/conf/folder/conf1,/some/conf/folder/conf2"
export FILES_BASE64="Y29uZjEK,Y29uZjIK"
python b64tofile.py
```

## Docker

```sh
docker run \
  --rm \
  -v /some/conf/folder:/some/conf/folder \
  -e FILES_PATHS="/some/conf/folder/conf1,/some/conf/folder/conf2" \
  -e FILES_BASE64="Y29uZjEK,Y29uZjIK" \
  etiennenapoleone/b64tofile
```
