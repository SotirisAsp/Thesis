# SOLD² - Self-supervised Occlusion-aware Line Description and Detection

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

We recommend using this code in a Python environment (e.g. venv or conda). The following script installs the necessary requirements with pip:
```bash
pip install -r requirements.txt
```

Set your dataset and experiment paths (where you will store your datasets and checkpoints of your experiments) by modifying the file `config/project_config.py`. Both variables `DATASET_ROOT` and `EXP_PATH` have to be set.

Install the Python package:
```bash
pip install -e .
```
