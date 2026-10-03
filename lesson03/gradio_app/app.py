from fastai.vision.all import *  # fastai, to load the model
import gradio as gr              # Gradio, for the web app
import timm                      # the library with the pretrained models

# Load the model exported in hints_2_finetuning.ipynb
learn = load_learner("model.pkl")
categories = learn.dls.vocab

# The function behind the app: an image in, the probabilities of all categories out
def classify_image(image):
    prediction, index, probabilities = learn.predict(image)
    return dict(zip(categories, map(float, probabilities)))

# All .jpg images uploaded to the Space are shown as examples
examples = sorted(str(file) for file in Path(".").glob("*.jpg")) or None

app = gr.Interface(fn=classify_image,
                   inputs=gr.Image(width=224, height=224),
                   outputs=gr.Label(),
                   examples=examples)
app.launch()
