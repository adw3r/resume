import webbrowser

import pdfkit
import argparse

# EXECUTOR = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'

parser = argparse.ArgumentParser()
parser.add_argument("-e", "--executor", help="The executor to use")
args = parser.parse_args()
EXECUTOR = args.executor

OPTIONS = {
    'page-size': 'A4',
    'zoom': 1.4,
    'margin-top': '0in',
    'margin-right': '0in',
    'margin-bottom': '0in',
    'margin-left': '0in',
    # 'encoding': "UTF-8",
    # 'no-outline': None
}


def convert_to_pdf(source, pdf_out_path):
    config = pdfkit.configuration(wkhtmltopdf=EXECUTOR)
    pdfkit.from_file(source, pdf_out_path, configuration=config, options=OPTIONS)


if __name__ == '__main__':
    convert_to_pdf(r'Python dev Naidiuk Oleksii.html', r'Python dev Naidiuk Oleksii.pdf')
    webbrowser.open(r'Python dev Naidiuk Oleksii.pdf')
