import pandas as pd

df = pd.read_csv('copyright_records.csv')  

results = []

for idx, row in df.iterrows():

    query = f"{row['Title']} {row['Copyright Claimant']} {row['Description']}"
    search_url = f"https://www.google.com/search?tbm=isch&q={query.replace(' ', '+')}"
    results.append({
        "Registration Number": row['Registration Number / Date'],
        "Query": query,
        "Google Images Search URL": search_url
    })


pd.DataFrame(results).to_csv('image_search_links.csv', index=False)
print("Google Images search links saved to image_search_links.csv")