import requests

cookies = {
    '_octo': 'GH1.1.2045407306.1670336220',
    '_device_id': '4080764a6f93b98d37a7aba816e05ad3',
    'user_session': 'ibAmk7NvagOLNz9sBvSOYLzUNkd-6Frbi1HXv1XC6O3C-18z',
    'logged_in': 'yes',
    'dotcom_user': 'adw3r',
    'color_mode': '%7B%22color_mode%22%3A%22dark%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark_dimmed%22%2C%22color_mode%22%3A%22dark%22%7D%7D',
    'preferred_color_mode': 'dark',
    'tz': 'Europe%2FKiev',
    'has_recent_activity': '1',
    '_gh_sess': 'cmMUYnEemYgZGf0tsmVXiwoFHLblI%2BYzeDX5gq2%2BGPE94JowuSpBFY2mhWZcLYa%2FmgCrIt1AgVKr7LM%2F8CKKPxm950nqQoiP49X5dAROPW7BiHte93UoSGRBLHRm6sAZ5S%2F4nvyrZZVC0%2F5d%2FNzFO4Cq8zeq4welnsPk90ThwRXanLYcKWzyeSjGd31IpTW4kJLyVWIC43FzYtxyZDGY3J%2F7%2Bz4CO4DSKL2mR5O9nC96%2F7xGas3q6wSo23JE0l9iuQgKS%2B8OjPiQ8DbXwBvUdm%2BNM8XT1iGWThtNoBNB8KmFCGJFfw%2BwiO675WqJmUnctzCR1KBbCI7knXVherxU6Q0GYt6Wh1yWIPACi%2FEew4iN2sDZ0r8V6iEyIBgc4fq0MkcgwDbm9KqYoUmg5HleVB76twPBe1%2FVQFvCKaOnOFDoQ8frCqqgRCp%2FyImKnFwtwcFBQPnQPdDNmUlu--oFg6hhLtMwbCN%2FZY--QRtHfleJDqrAKhqmpuOXeQ%3D%3D',
}

headers = {
    'authority': 'github.com',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'referer': 'https://wkhtmltopdf.org/',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
}


def download_wkhtmltox():
    response = requests.get(
        'https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox-0.12.6-1.mxe-cross-win64.7z',
        cookies=cookies,
        headers=headers,
    )
    with open('wkhtmltox.zip', 'wb') as file:
        file.write(response.content)


if __name__ == '__main__':
    download_wkhtmltox()
