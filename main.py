import requests
import pandas as pd


date = "2022-01-18"
url = 'https://disclosure.edinet-fsa.go.jp/api/v2/documents'
url_request = url + '.json'
Subscription_key = "77115a3156904bf89035bcf4e0c059fc"

params = {
    "date": date,
    "type": 2,
    "Subscription-key": Subscription_key
}

res = requests.get(url_request, params=params, verify=False)
res_json = res.json()
df = pd.DataFrame(res_json["results"])

print(df)
# res_df.columns
# doc_id = "S100FIZV"
# url_result = url + doc_id
# params = {
#     "type": 5,
#     "Subscription_key": Subscription_key
# }

# filename = doc_id + ".zip"
# res = requests.get(url_result, params=params, verify=False)

