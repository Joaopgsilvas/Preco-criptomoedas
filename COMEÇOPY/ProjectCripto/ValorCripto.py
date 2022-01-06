import requests
simb_moeda = input('Digite o simbolo da criptomoeda que você deseja ver o preço : ').upper()
simb_base = input('Digite o simbolo da criptomoeda que você deseja, que seja a base para a comparação, ex: USDT ou BRL : ').upper()


simbolo = simb_moeda + simb_base

url = f"https://api.binance.com/api/v3/ticker/price?symbol={simbolo}"

requisicao = requests.get(url)

preco = requisicao.json()

preco_r = preco["price"]

print(f'o valor do {simbolo} equivale a {preco_r}')



