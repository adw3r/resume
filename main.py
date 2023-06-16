import webbrowser

import pdfkit

html = 'Oleksii Naidiuk.html'
out = 'Oleksii Naidiuk.pdf'
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


def main():
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdfkit.from_file(html, out, configuration=config, options=options)
    webbrowser.open(out)


if __name__ == '__main__':
    main()
