import requests
import pandas as pd
import duckdb


def extract_data(limit = 1302):
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

    # Step 4: Save as Parquet file
    df.to_parquet("pokemon_basic.parquet", index=False)

    message = "Parquet file saved as 'pokemon_basic.parquet'"

  else:
    message = "Error: Failed to retrieve data"

  return message

def load_data():
    # Step 1: Connect to (or create) a DuckDB database
    con = duckdb.connect("pokedex.duckdb")

    # Step 2: Create 'pokedex' table (replace it if it already exists)
    con.execute("DROP TABLE IF EXISTS pokedex;")
    con.execute("""
        CREATE TABLE pokedex AS
        SELECT * FROM read_parquet('pokemon_basic.parquet')
    """)

    print("Pokedex data loaded successfully.")
    con.close()

def transform_data():
  # your code here
  pass


def main():
  # data = extract_data(20)
  # print(data)
  load_data()

if __name__ == "__main__":
  main()
