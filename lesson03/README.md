**Date**: Oct 2, 2026 (remote, via Google Meet)

* Going through the last two notebooks from [Lesson 02](../lesson02/) together:
  * [Notebook 4: The same with fastai](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson02/04_fastai.ipynb)
  * [Notebook 5: Fine-tuning a pretrained model](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson02/05_finetuning.ipynb)
* Watching the video [Visualizing transformers and attention](https://www.youtube.com/watch?v=KJtZARuO3JY&t=2371s) by Grant Sanderson (3Blue1Brown), a talk for TNG Big Tech Day '24

**Assignment 02** (due Oct 15, 18:00):

* Create your own image dataset and make it publicly available (2-5 categories, 100-300 images per category, cca 1000 images in total). Split it into train and test partitions (75% : 25%). See the required folder format below. Hints: [hints_1_dataset.ipynb](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson03/hints_1_dataset.ipynb)
* Fine-tune a model on your dataset, using fastai. Be sure to run the training on GPU. Export and download the model. Hints: [hints_2_finetuning.ipynb](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson03/hints_2_finetuning.ipynb)
* Create a free [HuggingFace account](https://huggingface.co/). Try to run a Gradio app that takes an image as input and outputs the predicted class, first locally (e.g. in Colab). Then deploy it to [HuggingFace Spaces](https://huggingface.co/spaces). You can use [hints_3_gradio.ipynb](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson03/hints_3_gradio.ipynb) and the files in [gradio_app](gradio_app/) to guide you (CPU runtime is fine, you do not need GPU for this step). The result should look something like [this](https://huggingface.co/spaces/simecek/teaching_img_classifier).
* Submit the links to your dataset and your app through the form (I will share the link on Slack).

**Notes:**
* We have not covered Gradio and HuggingFace Spaces yet. I will explain them in the lesson on Oct 9, so it is a good idea to have your dataset and model ready by then.
* If you have any questions, ask them in the lesson on Oct 9.
* If you prefer another framework to Gradio (e.g. you vibe-code a small web app and host it on DigitalOcean or elsewhere), feel free to do that. The app just needs to be publicly accessible, so that you can submit its link.

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
