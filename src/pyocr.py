from PIL import Image
import sys
import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)
tool = tools[0]
txt = tool.image_to_string(
    Image.open("/database/text-tool03.png"),
    lang="jpn+eng",
    builder=pyocr.builders.TextBuilder(tesseract_layout=6)
)
print(txt)