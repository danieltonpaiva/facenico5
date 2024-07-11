from typing import Optional, List
import gradio
import os
import facefusion.globals
from facefusion import wording
from facefusion.uis.typing import File
from facefusion.filesystem import are_images
from facefusion.uis.core import register_ui_component

SOURCE_FILE : Optional[gradio.File] = None
SOURCE_IMAGE : Optional[gradio.Image] = None


def render() -> None:
	global SOURCE_FILE
	global SOURCE_IMAGE

	are_source_images = are_images(facefusion.globals.source_paths)
	SOURCE_FILE = gradio.File(
		file_count = 'multiple',
		file_types =
		[
			'.png',
			'.jpg',
			'.webp'
		],
		label = wording.get('source_file_label'),
		value = facefusion.globals.source_paths if are_source_images else None
	)
	
	caminho = '/content/facenico5/exemplos'
	arquivos = [f for f in os.listdir(caminho) if os.path.isfile(os.path.join(caminho, f))]
	files = []
	for x in arquivos:
		if x != "f.txt":
			files.append(caminho + '/' + x)

	examples = gradio.Examples(sorted(files), SOURCE_IMAGE)
	register_ui_component('source_image', inputs=SOURCE_IMAGE)

		
def listen() -> None:
	SOURCE_FILE.change(update, inputs = SOURCE_FILE, outputs = SOURCE_IMAGE)


def update(files : List[File]) -> gradio.Image:
	file_names = [ file.name for file in files ] if files else None
	if are_images(file_names):
		facefusion.globals.source_paths = file_names
		return gradio.Image(value = file_names[0], visible = True)
	facefusion.globals.source_paths = None
	return gradio.Image(value = None, visible = False)
