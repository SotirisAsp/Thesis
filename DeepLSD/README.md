# DeepLSD
It can be used to extract **generic line segments from images in-the-wild**, and is **suitable for any task requiring high precision**, such as homography estimation, visual localization, and 3D reconstruction.

## Installation
First clone the repository and its submodules:
```
git clone --recurse-submodules https://github.com/cvg/DeepLSD.git
cd DeepLSD
```

### Quickstart install (for inference only)

To test the pre-trained model on your images, without the final line refinement, the following installation is sufficient:
```
bash quickstart_install.sh
```
You can then test it with the notebook `notebooks/quickstart_demo.ipynb`.



### Full install

Follow these instructions if you wish to re-train DeepLSD, evaluate it, or use the final step of line refinement.

Dependencies that need to be installed on your system:
- [OpenCV](https://opencv.org/)
- [GFlags](https://github.com/gflags/gflags)
- [GLog](https://github.com/google/glog)
- [Ceres](http://ceres-solver.org/)
- DeepLSD was successfully tested with GCC 9, Python 3.7, and CUDA 11. Other combinations may work as well.

Once these libraries are installed, you can proceed with the installation of the necessary requirements and third party libraries:
```
bash install.sh
```

This repo uses a base experiment folder (EXPER_PATH) containing the output of all trainings, and a base dataset path (DATA_PATH) containing all the evaluation and training datasets. You can set the path to these two folders in the file `deeplsd/settings.py`.

## Usage
We provide two pre-trained models for DeepLSD: [deeplsd_wireframe.tar](https://cvg-data.inf.ethz.ch/DeepLSD/deeplsd_wireframe.tar) and [deeplsd_md.tar](https://cvg-data.inf.ethz.ch/DeepLSD/deeplsd_md.tar), trained respectively on the Wireframe and MegaDepth datasets. The former can be used for easy indoor datasets, while the latter is more generic and works outdoors and on more challenging scenes.
The example notebook `notebooks/demo_line_detection.ipynb` showcases how to use DeepLSD in practice. Please refer to the comments on the config of this notebook to understand the usage of each hyperparameter.

You can download the two models with the following command:
```
mkdir weights
wget https://cvg-data.inf.ethz.ch/DeepLSD/deeplsd_wireframe.tar -O weights/deeplsd_wireframe.tar
wget https://cvg-data.inf.ethz.ch/DeepLSD/deeplsd_md.tar -O weights/deeplsd_md.tar
```

## Inference

