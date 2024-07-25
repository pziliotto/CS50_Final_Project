#Trazendo o código do trabalho final do CS50 para teste
def get_brazil_phone_codes():
  brazil_phone_codes = {
      'AC': {'capital': 'Rio Branco', 'phone_codes': ['68']},
      'AL': {'capital': 'Maceió', 'phone_codes': ['82']},
      'AP': {'capital': 'Macapá', 'phone_codes': ['96']},
      'AM': {'capital': 'Manaus', 'phone_codes': ['92']},
      'BA': {'capital': 'Salvador', 'phone_codes': ['71', '73', '74', '75', '77', '79']},
      'CE': {'capital': 'Fortaleza', 'phone_codes': ['88']},
      'DF': {'capital': 'Brasília', 'phone_codes': ['61', '62']},
      'ES': {'capital': 'Vitória', 'phone_codes': ['27', '28']},
      'GO': {'capital': 'Goiânia', 'phone_codes': ['62']},
      'MA': {'capital': 'São Luís', 'phone_codes': ['98']},
      'MT': {'capital': 'Cuiabá', 'phone_codes': ['65']},
      'MS': {'capital': 'Campo Grande', 'phone_codes': ['67']},
      'MG': {'capital': 'Belo Horizonte', 'phone_codes': ['31', '32', '33', '34', '35', '37', '38']},
      'PA': {'capital': 'Belém', 'phone_codes': ['91', '93', '95', '96', '97', '99']},
      'PB': {'capital': 'João Pessoa', 'phone_codes': ['83']},
      'PR': {'capital': 'Curitiba', 'phone_codes': ['41', '42', '43', '44', '45', '46', '47', '48']},
      'PE': {'capital': 'Recife', 'phone_codes': ['81']},
      'PI': {'capital': 'Teresina', 'phone_codes': ['86']},
      'RJ': {'capital': 'Rio de Janeiro', 'phone_codes': ['21', '22', '24']},
      'RN': {'capital': 'Natal', 'phone_codes': ['84', '85']},
      'RS': {'capital': 'Porto Alegre', 'phone_codes': ['51', '53', '54', '55']},
      'RO': {'capital': 'Porto Velho', 'phone_codes': ['69']},
      'RR': {'capital': 'Boa Vista', 'phone_codes': ['95']},
      'SC': {'capital': 'Florianópolis', 'phone_codes': ['48']},
      'SP': {'capital': 'São Paulo', 'phone_codes': ['11', '12', '13', '14', '15', '16', '17', '18']},
      'SE': {'capital': 'Aracaju', 'phone_codes': ['79']},
      'TO': {'capital': 'Palmas', 'phone_codes': ['63']}
  }
  return brazil_phone_codes

def search_by_state(brazil_phone_codes, state):
  if state in brazil_phone_codes:
      print(f"Phone codes for state {state}: {brazil_phone_codes[state]['phone_codes']}")
      return True
  return False

def search_by_capital(brazil_phone_codes, capital):
  for state, info in brazil_phone_codes.items():
      if info['capital'] == capital:
          print(f"Phone code for capital {capital}: {info['phone_codes'][0]}")
          return True
  return False
def search_by_phone_code(brazil_phone_codes, phone_code):
  for state, info in brazil_phone_codes.items():
      if phone_code in info['phone_codes']:
          print(f"State for phone code {phone_code}: {state}")
          return True
  return False

def main():
  brazil_phone_codes = get_brazil_phone_codes()

  while True:
      print("\nChoose an option:")
      print("1. Search by state")
      print("2. Search by capital")
      print("3. Search by phone code")
      print("4. Exit")

      option = input("Enter the number of your option: ")

      if option == '1':
          state = input("Enter the state: ")
          search_by_state(brazil_phone_codes, state)
      elif option == '2':
          capital = input("Enter the capital: ")
          search_by_capital(brazil_phone_codes, capital)
      elif option == '3':
          phone_code = input("Enter the phone code: ")
          search_by_phone_code(brazil_phone_codes, phone_code)
      elif option == '4':
          print("Exiting...")
          break
      else:
          print("Invalid option. Please try again.")

if __name__ == "__main__":
  main()
