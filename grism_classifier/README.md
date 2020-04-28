 # Image Classification with PyTorch on HST/WFC3 grism emission line extractions

Project code for Image Classification with PyTorch done with HST/WFC3 grism emission line extractions to automatically classify 2D
images as stellar/artifact/poor modeling, edge of chip, compact, diffuse, and noisy. The first 2 classes will prove 
most useful in removing unusable data from a pointing. Data quality limits a more fine morphology with a 2-orbit depth at z = 0.5. 



## Prerequisites
The Code is written in Python 3.7.3 . If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. 

To install pip run in the command Line
```
python -m ensurepip -- default-pip 
``` 
to upgrade it
```
python -m pip install -- upgrade pip setuptools wheel
```
to upgrade Python
```
pip install python -- upgrade
```
Additional Packages that are required are: [Numpy](http://www.numpy.org/), [Pandas](https://pandas.pydata.org/), [MatplotLib](https://matplotlib.org/), [Pytorch](https://pytorch.org/), PIL and json.\
You can donwload them using [pip](https://pypi.org/project/pip/)
```
pip install numpy pandas matplotlib pil
```
or [conda](https://anaconda.org/anaconda/python)
```
conda install numpy pandas matplotlib pil
```
In order to install PyTorch head over to the [PyTorch site](https://pytorch.org) select your setup and follow the instructions given.	This notebook utilizes version 1.5.

### Project assets:

- `Grism_Classifier.ipynb` Jupyter Notebook
- `grism_classifier.json` which are the classes of animals and their respective directories.


Directory should contain **test**, **train** and **valid** subdirectories containing classification directories and animal images under the main directory.

## Viewing the Jupyter Notebook

Open terminal in current folder where the notebook is and type:
```
jupyter notebook
```


## Prediction
* This neural net is 69% accurate on the test set and is in progress. 

<img src="noisy.png" width="310" height="300" /><img src="diffuse.png" width="370" height="300" />

<img src="artifact.png" width="370" height="300" />


## To Do: 

- [ ] Train on 3D-HST
- [ ] Train on Halpha extractions only
- [ ] Are G102 and G141 grism data interchangeable ?
- [ ] Train with Sersic Index
- [ ] Investigate accuracy dependence on z and orbit depth



