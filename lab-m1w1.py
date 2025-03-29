import requests
import pandas as pd

def extract_data(limit = 1302) -> pd.DataFrame:
  url = f"https://pokeapi.co/api/v2/pokemon?offset=0&limit={limit}"
  response = requests.get(url)
  data = response.json()


  if response.status_code == 200:
    print ("Data retrieved successfully. Now converting to DataFrame...")
    data = response.json()
    results = data.get("results", [])

    # Step 2: Create a list of dictionaries with name and URL
    pokemon_basic = [{"name": item["name"], "url": item["url"]} for item in results]

    # Step 3: Convert to DataFrame
    df = pd.DataFrame(pokemon_basic)

  else:
    print("Error: Failed to retrieve data")

  return df


def load_data():
  # your code here
  pass

def transform_data():
  # your code here
  pass


def main():
  data = extract_data(20)
  print(data)


if __name__ == "__main__":
  main()
