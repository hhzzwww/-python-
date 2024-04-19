import requests

token_url = 'https://morse-us-prod.adsmoloco.com/v1/tokens'
json = {
    "workplace_id": "TECDO_SOLID",
    "email": "roxy.chen@tec-do.com",
    "password": "Mobisummer123!"

}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}
response = requests.post(url=token_url, json=json, headers=headers).json()
token = response["token"]
# print(response)
# print(token)


account_url = "https://api.moloco.cloud/cm/v1/ad-accounts"

headers_login_data = {
    "Authorization": "Bearer {}".format(token),
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Content-Type": "application/json"
}

response_account = requests.get(url=account_url, headers=headers_login_data).json()

account_id = response_account['ad_accounts'][0]['id']
# print(account_id)

data_url = 'https://api.moloco.cloud/cm/v1/analytics-detail'

data_json = {
    "ad_account_id": "{}".format(account_id),
    "timezone": "America/Los_Angeles",
    "date_range": {"start": "2023-07-01", "end": "2023-07-31"},
    "dimensions": ["AD_ACCOUNT_TITLE", "DATE", "APP_OR_SITE_TITLE", "APP_OR_SITE_ID", "CAMPAIGN_TITLE", "CAMPAIGN_ID"],
    "metrics": ["IMPRESSIONS", "TARGET_ACTIONS", "CLICKS", "INSTALLS", "SPEND", "CTR", "IPM", "CPC", "CPI", "CPA"],
    "dimension_filters": [], "metric_filters": [], "conversion_event_filters": [],
    "conversion_event_metric_filters": [],
    "order_by_filters": [{"dimension": "DATE", "is_descending": True},
                         {"dimension": "APP_OR_SITE_TITLE", "is_descending": True},
                         {"dimension": "CAMPAIGN_TITLE", "is_descending": True}], "limit": "10000"
}

response_data = requests.post(url=data_url, headers=headers_login_data, json=data_json).json()
# print(response_data)

report_datas = response_data['rows']
for data in report_datas:
    print(data)
    campaign_id = data['campaign']['id']
    campaign_name = data['campaign']['title']
    impressions = data['metric']['impressions']
    clicks = data['metric']['clicks']
    installs = data['metric']['installs']
    spend = data['metric']['spend']













