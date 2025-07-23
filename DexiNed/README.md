## Instructions
* [Video](https://www.youtube.com/watch?v=Hz0uU04B3U8)

## Installation
First clone the repository and its submodules:
```
git clone https://github.com/xavysp/DexiNed.git
cd DexiNed
```
## Requirements

* [Python 3.7](https://www.python.org/downloads/release/python-370/g)
* [Pytorch >=1.4](https://pytorch.org/) (Last test 1.9)
* [OpenCV](https://pypi.org/project/opencv-python/)
* [Matplotlib](https://matplotlib.org/3.1.1/users/installing.html)
* [Kornia](https://kornia.github.io/)
* Other package like Numpy, h5py, PIL, json. 

## Download Checkpoints
* Download from -> [Checkpoints](https://drive.google.com/file/d/1V56vGTsu7GYiQouCIKvTWl5UKCZ6yCNu/view) and place it into the DexiNed folder like: checkpoints/BIPED/10/

## Inference
-change line 200 from main.py to -> default=9,
-place your images to 'data' folder
-results to -> 'result' folder
