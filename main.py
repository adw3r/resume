import webbrowser

import pdfkit

html = 'resume.html'
out = 'resume.pdf'
path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
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

config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
pdfkit.from_file(html, out, configuration=config, options=options)
webbrowser.open(out)
