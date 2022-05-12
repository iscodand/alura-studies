import re


class ExtractorURL():
    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.url_validation()

    def sanitize_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def url_validation(self):
        if not self.url:
            raise ValueError('Sua URL está vazia!')

        url_pattern = re.compile(
            '(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = url_pattern.match(self.url)
        if not match:
            raise ValueError('A URL não é válida!')

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url

    def __eq__(self, other):
        return self.url == other.url

    @property
    def origin_currency(self):
        return self.parameter_value("moedaOrigem")

    @property
    def destiny_currency(self):
        return self.parameter_value("moedaDestino")

    @property
    def quantity_currency(self):
        return self.parameter_value("quantidade")

    @property
    def url_base(self):
        return self.url[:self.url.find('?')]

    @property
    def url_parameter(self):
        return self.url[self.url.find('?') + 1:]

    def parameter_value(self, search_parameter):
        parameter_index = self.url_parameter.find(search_parameter)
        value_index = parameter_index + 1 + len(search_parameter)
        index_comercial_e = self.url_parameter.find('&', value_index)

        if index_comercial_e == -1:
            return self.url_parameter[value_index:]
        else:
            return self.url_parameter[value_index:index_comercial_e]


class Converter(ExtractorURL):
    def __init__(self, url):
        super().__init__(url)

    def conversion(self, quantity):
        dolar_value = 5.50
        real_value = 0.25
        quantity_in_float = float(quantity)

        if self.origin_currency == "real":
            quantity_in_float *= dolar_value
            return f'USD {self.quantity_currency} -----> R$ {quantity_in_float}'

        elif self.origin_currency == "dolar":
            quantity_in_float *= real_value
            return f'R$ {self.quantity_currency} -----> USD {quantity_in_float}'
        else:
            return 'Não foi possível realizar a conversão!'


url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extractor_url = Converter(url)

quantidade = extractor_url.parameter_value("quantidade")
moeda_origem = extractor_url.parameter_value("moedaOrigem")
moeda_destino = extractor_url.parameter_value("moedaDestino")

print(extractor_url.conversion(quantidade))
