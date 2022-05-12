import re


url = 'https://www.bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'
url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')

match = url_pattern.match(url)

if not match:
    raise ValueError('A URL não é válida!')

print('URL Válida!')