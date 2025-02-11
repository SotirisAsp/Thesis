# SOLD² - Self-supervised Occlusion-aware Line Description and Detection

Method for extracting line segments from images. The outputs are npz files with keys [’line_seg’, ’descriptors’]

Original repo : [SOLD2](https://github.com/cvg/SOLD2)

## Usage

### Using from kornia

SOLD² is integrated into [kornia](https://github.com/kornia/kornia) library since version 0.6.7.

 ```
 pip install kornia==0.6.7
 ```

 Then you can import it as 
 ```python3
 from kornia.feature import SOLD2
 ```

 See tutorial on using SOLD² from kornia [here](https://kornia.github.io/tutorials/nbs/line_detection_and_matching_sold2.html).

### Installation

We recommend using this code in a Python environment (e.g. venv or conda). 
```bash
conda create -n sold2_env python=3.8 -y
conda activate sold2_env
```
The following script installs the necessary requirements with pip:
```bash
pip install -r requirements.txt
```

Set your dataset and experiment paths (where you will store your datasets and checkpoints of your experiments) by modifying the file `config/project_config.py`. Both variables `DATASET_ROOT` and `EXP_PATH` have to be set.

Install the Python package:
```bash
pip install -e .
```
### Pretrained models

We provide the checkpoints of two pretrained models:
- [sold2_synthetic.tar](https://cvg-data.inf.ethz.ch/SOLD2/sold2_synthetic.tar): SOLD² detector trained on the synthetic dataset only.
- [sold2_wireframe.tar](https://cvg-data.inf.ethz.ch/SOLD2/sold2_wireframe.tar): full version of SOLD² trained on the Wireframe dataset.
 
Note that you do not need to untar the models, you can directly used them as they are.


### How to use it

You can use the model to export line features as follows:
```bash
python -m sold2.export_line_features --img_list <list to a txt file containing the path to all the images> --output_folder <path to the output folder> --checkpoint_path <path to your best checkpoint,>
```

```bash
python -m sold2.export_line_features --img_list wireframe.txt --output_folder out --checkpoint_path pretrained_models/sold2_wireframe.tar
```

1) Create the output folder before RUN export_line_features.py
2) Requires a txt with all the image paths. (img_list)
