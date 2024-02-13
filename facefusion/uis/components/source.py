from typing import Optional, List
import gradio

import facefusion.globals
from facefusion import wording
from facefusion.uis.typing import File
from facefusion.filesystem import are_images
from facefusion.uis.core import register_ui_component
import os

SOURCE_IMAGE : Optional[gradio.Image] = None


def render() -> None:
	global SOURCE_IMAGE
	SOURCE_IMAGE = gradio.Image(
		type="filepath",
		visible = True,
	)
	register_ui_component('source_image', SOURCE_IMAGE)
	arquivos = [f for f in os.listdir('/content/facenico5/exemplos') if os.path.isfile(os.path.join('/content/facenico5/exemplos', f))]
	files = []
	for x in arquivos:
		files.append('/content/facenico5/exemplos/' + x)

	#examples = gradio.Examples(sorted(files), SOURCE_IMAGE, examples_per_page=20)


def listen() -> None:
	SOURCE_IMAGE.change(update)


def update() -> None:
	facefusion.globals.source_paths = [SOURCE_IMAGE.value]
	print(facefusion.globals.source_paths)
