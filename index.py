import hashlib
import requests
import getpass

def hash_password(password):
  password_bytes = bytes(password, 'utf-8')
  password_hash = hashlib.sha1(password_bytes)
  hash_hex = password_hash.hexdigest().upper()
  return hash_hex

def slice_hash(hash):
  return hash[0:5], hash[5:]

def get_leaks(prefix):
  try:
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
      return response.text, None
    if response.status_code == 429:
      return None, 'rate_limit'
    else:
      return None, f'status_{response.status_code}'
  except requests.exceptions.RequestException:
    return None, 'Conexão'

def password_leak(sufix, leaks:list):
  for leak in leaks:
    sufix_leak, quant = leak.split(':')
    if sufix_leak == sufix:
      return quant
  return False

def main():
  password = getpass.getpass('Digite sua senha: ') #senha
  hash_hex = hash_password(password)
  prefix, sufix = slice_hash(hash_hex)
  response, error = get_leaks(prefix)
  if not response:
    print(f'Erro ao consultar senhas vazadas.Erro:{error}. Por favor tente novamente mais tarde')
    return
  leaks = response.splitlines()
  leak = password_leak(sufix, leaks)
  if leak:
    print(f'Sua senha foi vazada: {leak} vezes')
    return
  print('Sua senha não foi encontrada e possivelmente não foi vazada')

main()