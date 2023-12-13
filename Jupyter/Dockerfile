FROM jupyter/base-notebook

COPY . /data

WORKDIR /data

# Instala las dependencias necesarias
RUN pip install pymongo pandas requests matplotlib seaborn

CMD ["jupyter", "nbconvert", "--execute", "--to", "notebook", "--inplace", "--ExecutePreprocessor.timeout=-1", "imserso.ipynb"]
