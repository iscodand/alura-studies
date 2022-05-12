url = 'https://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real'

# Sanitização da URL
url.strip()

# Validação da URL
if url == "":
    raise ValueError('Sua URL está vazia')

# Separa base e parâmetros
interrogation_index = url.find('?')
url_base = url[:interrogation_index]
url_parameters = url[interrogation_index + 1:]
print(url_parameters)

# Busca o valor dos parâmetros
search_parameter = 'moedaOrigem'
parameter_index = url_parameters.find(search_parameter)
value_index = parameter_index + 1 + len(search_parameter)
index_comercial_e = url_parameters.find('&', value_index)
if index_comercial_e == -1:
    value = url_parameters[value_index:]
else:
    value = url_parameters[value_index:index_comercial_e]
print(value)
