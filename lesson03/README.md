**Date**: Oct 2, 2026 (remote, via Google Meet)

* Going through the last two notebooks from [Lesson 02](../lesson02/) together:
  * [Notebook 4: The same with fastai](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson02/04_fastai.ipynb)
  * [Notebook 5: Fine-tuning a pretrained model](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson02/05_finetuning.ipynb)
* Watching the video [Visualizing transformers and attention](https://www.youtube.com/watch?v=KJtZARuO3JY&t=2371s) by Grant Sanderson (3Blue1Brown), a talk for TNG Big Tech Day '24

**Assignment 02** (due Oct 15, 18:00):

> **Update (Oct 12):** Hugging Face no longer offers free Gradio Spaces to new accounts (since summer 2026), so the deployment step moves from Hugging Face Spaces to **Streamlit Community Cloud** (see below). **For the Oct 15 deadline, it is enough to submit your dataset and your training notebook.** The deployed app is optional this week, but I will be glad if you try.

* Create your own image dataset and make it publicly available (2-5 categories, 100-300 images per category, cca 1000 images in total). Split it into train and test partitions (75% : 25%). See the required folder format below. Hints: [hints_1_dataset.ipynb](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson03/hints_1_dataset.ipynb)
* Fine-tune a model on your dataset, using fastai. Be sure to run the training on GPU. Export the model ~~and download it~~ and upload it to a [Hugging Face](https://huggingface.co/) model repository (model repositories are still free, only Gradio Spaces are not). Hints: [hints_2_finetuning.ipynb](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson03/hints_2_finetuning.ipynb), sections 6 and 7.
* ~~Create a free [HuggingFace account](https://huggingface.co/). Try to run a Gradio app that takes an image as input and outputs the predicted class, first locally (e.g. in Colab). Then deploy it to [HuggingFace Spaces](https://huggingface.co/spaces). You can use [hints_3_gradio.ipynb](https://colab.research.google.com/github/simecek/dspracticum2026/blob/main/lesson03/hints_3_gradio.ipynb) and the files in [gradio_app](gradio_app/) to guide you (CPU runtime is fine, you do not need GPU for this step). The result should look something like [this](https://huggingface.co/spaces/simecek/teaching_img_classifier).~~ *(no longer free for new Hugging Face accounts)*
* Deploy your model as a [Streamlit](https://streamlit.io/) app on [Streamlit Community Cloud](https://share.streamlit.io/) (free, you sign in with your GitHub account). Example: [the app](https://beans-classifier-test.streamlit.app/) and [its code](https://github.com/simecek/beans-classifier).
  1. Create a public GitHub repository with two files, `app.py` and `requirements.txt`. Copy them from the [example](https://github.com/simecek/beans-classifier). In `app.py`, change `REPO_ID` to your Hugging Face model repository, and the title and texts to fit your dataset. Keep `requirements.txt` unchanged: it pins the same versions as Colab.
  2. On [share.streamlit.io](https://share.streamlit.io/): *Create app* → your repository, branch `main`, file `app.py`.
  3. **Advanced settings → Python version → 3.13**, the same as Colab. A model exported in Colab does not load on other Python versions. The version cannot be changed later; you would have to delete the app and create it again.
  4. *Deploy*. The first build takes a few minutes, and the first page load downloads your model from Hugging Face.
* Submit the links to your dataset, your training notebook and ~~your app~~ (optional this week) your app through the form (I will share the link on Slack).

**Notes:**
* ~~We have not covered Gradio and HuggingFace Spaces yet. I will explain them in the lesson on Oct 9, so it is a good idea to have your dataset and model ready by then.~~
* If you have any questions, ask them in the lesson on Oct 9.
* If you prefer another framework to ~~Gradio~~ Streamlit (e.g. you vibe-code a small web app and host it on DigitalOcean or elsewhere), feel free to do that. The app just needs to be publicly accessible, so that you can submit its link.

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
