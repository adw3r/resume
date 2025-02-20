import requests



def main():
    response = requests.get(
        'https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.mxe-cross-win64.7z',
    )
    with open('wkhtmltox.zip', 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    main()
