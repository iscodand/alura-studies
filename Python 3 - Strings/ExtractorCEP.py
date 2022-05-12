import re

address = 'VP 17, Quadra 38, Cohab 2, Casa 12, Bacabal, Maranhão, 65700-000'

pattern = re.compile('[0-9]{5}[-]?[0-9]{3}')
search = pattern.search(address)

if search:
    cep = search.group()
    print(cep)
