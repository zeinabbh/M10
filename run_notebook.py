import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

filename = "/rds/general/user/ztb25/home/PBMC_datasets/6/dataset6_preprocessing.ipynb"
outname = "/rds/general/user/ztb25/home/PBMC_datasets/6/dataset6_preprocessing_executed.ipynb"
workdir = "/rds/general/user/ztb25/home/PBMC_datasets/6/"

with open(filename, encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=-1, kernel_name="m10")
ep.preprocess(nb, {"metadata": {"path": workdir}})

with open(outname, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)