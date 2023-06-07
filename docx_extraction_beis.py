import io
import os
import jsoo
import docx
import boto3
import zipfile
from datetime import datetime
import pandas as pd
import xml.etree.ElementTree as ET
from aws_lambda_powertools.logging.logger import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

def get_docx_text(path):
    document = zipfile.ZipFile(path)
    mxl_content = document.read('word/document.xml')
    document.close()
    tree = ET.XML(mxl_content)

    paragraphs = []
    for paragraph in tree.iter(PARA):
        texts = [node.text
                 for node in paragraph.iter(TEXT)
                  if node.text]
        if texts:
            paragraphs.append(''.join(texts))

    return '\\n<\b'.join(paragraphs)
