**Date**: Sep 18, 2026

**Slides**: TBD

* Introduction: What is Deep Learning?
* [One neuron training](https://colab.research.google.com/drive/1TxXqr1w4MNg4HYS8QI8YNArGK5_vO40Y?usp=sharing) demo
* Tools & organization of the course
* PyTorch: tensor, attributes, automatic differentiation
* FashionMNIST dataset: dense vs. convolutional architecture
* Git and GitHub

**Additional materials:**
* [The Zen of Python](https://peps.python.org/pep-0020/): 20 design principles for writing clean Python code
* [What is torch.nn really?](https://docs.pytorch.org/tutorials/beginner/nn_tutorial.html)
* [The Matrix Calculus You Need For Deep Learning](https://explained.ai/matrix-calculus/index.html)

**Assignment 01** (due to Sep 25, 8:30 AM):

* Sign up for our Slack (invite link sent by email).
* Create a [GitHub](https://github.com/) account.
* Open [Colab](https://colab.research.google.com/), create a new notebook and get familiar with Python. In particular, make sure you understand concepts such as variables, strings (and indexing), lists (and indexing), dictionaries (and keys), functions, arrays, and data frames. Test your knowledge with [Python exercises](https://bit.ly/pythonbrno) (you cannot edit the notebook directly, first create a copy with *File* → *Save a copy in Drive*).
* Play with the FashionMNIST scripts (try to improve accuracy on the test set).
* Create your own image dataset and make it publicly available (2-5 categories, 100-300 images per category, cca 1000 images in total). Split it to train and test partitions (75% : 25%). See the required folder format below.
* Train a simple CNN on your dataset. It is ok if it is not optimal - we will improve it next week.
* Fill in the links to your GitHub and the dataset into the form (the link is on Slack).

### Dataset format

* **Top-level folder**: Name of your dataset (e.g., `animals_dataset`)

* **Next level**: Two subfolders — `train/` and `test/` — for training and testing data

* **Next level**: Each class of image (e.g., `cat/`, `dog/`) gets its own folder

* **Final level**: Actual `.jpg` files (image filenames don't matter)

```
animals_dataset/
├── train/
│   ├── cat/
│   │   ├── 001.jpg
│   │   ├── 002.jpg
│   │   └── ...
│   ├── dog/
│   │   ├── 003.jpg
│   │   ├── 004.jpg
│   │   └── ...
│   └── ... (more classes)
├── test/
│   ├── cat/
│   │   ├── 101.jpg
│   │   ├── 102.jpg
│   │   └── ...
│   ├── dog/
│   │   ├── 103.jpg
│   │   ├── 104.jpg
│   │   └── ...
│   └── ... (more classes)
```
