FROM jupyter/base-notebook

COPY ./archivos /data

WORKDIR /data

CMD ["jupyter", "notebook", "--no-browser", "--NotebookApp.token=''", "--NotebookApp.password=''"]