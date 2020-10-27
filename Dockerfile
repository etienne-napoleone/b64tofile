FROM python:3.7-alpine

ENV FILES_PATHS ""
ENV FILES_BASE64 ""

COPY b64tofile.py /usr/local/bin/b64tofile

ENTRYPOINT [ "b64tofile" ]
