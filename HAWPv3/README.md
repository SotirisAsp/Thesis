# Holistically-Attracted Wireframe Parsing: From Supervised Learning to Self-Supervised Learning

Method for extracting wireframes (lines+junctions) from images. The implemantation is for HAWPv3 version.

Original repo : [HAWP](https://github.com/cherubicXN/hawp)

## Installation 

- Clone the code repo: ``git clone https://github.com/cherubicXN/hawp.git``.
- Install ninja-build by ``sudo apt install ninja-build``.
- Create a conda environment by
```bash
conda create -n hawp python==3.9
conda activate hawp
pip install -e .
```
- Run the following command lines to install the dependencies of HAWP
```bash
# Install pytorch, please be careful for the version of CUDA on your machine
pip install torch==1.12.0+cu116 torchvision==0.13.0+cu116 torchaudio==0.12.0 --extra-index-url https://download.pytorch.org/whl/cu116 
# Install other dependencies
pip install -r requirement.txt
```
- Verify the installation.
```bash
python -c "import torch; print(torch.cuda.is_available())" # Check if the installed pytorch supports CUDA.
```
- Downloading the offically-trained checkpoints of both **HAWPv2** and **HAWPv3**.
```bash
sh downloads.sh
```

## Changes
- Replace hawp/ssl/predict.py with predict.py from my repo.
   
## Inference
- Run HAWPv3 for multiple images with Run_hawp.py (from my repo)
1) Specify input_folder and output_folder
2) ext : (1) png -> images with wireframes (2) json -> json file with lines and junctions (3) txt -> txt with th predicted lines
3) threshold : confidence threshold , 0.1 is a good threshold
```bash
  python Run_hawp.py
  ```
## Checkpoints
|Model Name|Comments|
|---|---|
|[hawpv3-fdc5487a.pth](https://github.com/cherubicXN/hawp-torchhub/releases/download/HAWPv3/hawpv3-fdc5487a.pth)| Trained on the images of Wireframe dataset |
|[hawpv3-imagenet-03a84.pth](https://github.com/cherubicXN/hawp-torchhub/releases/download/HAWPv3/hawpv3-imagenet-03a84.pth)| Trained on 100k images of ImageNet dataset|
