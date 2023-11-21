import webbrowser

import pdfkit

source = r'Python dev Naidiuk Oleksii.html'
pdf_out_path = r'Python dev Naidiuk Oleksii.pdf'


def convert_to_pdf():
    options = {
        'page-size': 'A4',
        'zoom': 2,
        'margin-top': '0in',
        'margin-right': '0in',
        'margin-bottom': '0in',
        'margin-left': '0in',
        'encoding': "UTF-8",
        'no-outline': None
    }
    config = pdfkit.configuration(wkhtmltopdf=r'wkhtmltox\wkhtmltox\bin\wkhtmltopdf.exe')
    pdfkit.from_file(source, pdf_out_path, configuration=config, options=options)
    webbrowser.open(pdf_out_path)


if __name__ == '__main__':
    convert_to_pdf()
