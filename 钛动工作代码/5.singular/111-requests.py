import json

import requests

# headers中的X-Csrftoken和cookies中的csrf_token都用cookie中的token
# 获取cookies中的csrf_token
# from sqlalchemy import

url = 'https://app.singular.net/'
response_cookie = requests.get(url)
csrf_token = response_cookie.cookies.get('csrftoken', '')
# print(csrf_token)
# print(response_cookie.cookies)

# 登录接口
login_url = 'https://app.singular.net/login-user'

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Content-Length": "102",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://app.singular.net",
    "Pragma": "no-cache",
    "Referer": "https://app.singular.net/login?redir=%2F",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "",
    "emptySec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "X-Csrftoken": "{}".format(csrf_token)
}
requests_payload = {
    "email": "wustfanjunhao@163.com",
    "fragment": "/react/reports?query=%7B%22compare%22:False,%22is_goals%22:False,%22dimensions%22:%5B%22adn_account_name%22,%22country_field%22,%22unified_campaign_id%22,%22unified_campaign_name%22%5D,%22metrics%22:%5B%22custom_impressions%22,%22custom_clicks%22,%22custom_installs%22,%22adn_cost%22%5D,%22discrepancy_metrics%22:%5B%5D,%22file_combiner_dimensions%22:%5B%5D,%22granularity_levels%22:%5B%5D,%22enrichment_dimensions%22:%5B%5D,%22source_dimensions%22:%5B%5D,%22metadata_dimensions%22:%5B%5D,%22skan_conversion_dimensions%22:%5B%5D,%22cohort_metrics%22:%5B%22revenue%22%5D,%22modeled_skan_custom_events%22:%5B%5D,%22cohort_periods%22:%5B%22actual%22%5D,%22goals_metrics%22:%5B%5D,%22goals_forecast_metrics%22:%5B%5D,%22filters%22:%5B%5D,%22time_breakdown%22:%5B%22all%22%5D,%22source_attribution_type%22:%5B%5D,%22with_append_tables%22:%5B%5D,%22cross_device_cohort_type%22:%5B%5D,%22dual_attribution_mode%22:%5B%5D,%22cross_device_demo_cohort_type%22:%5B%5D,%22start_date%22:%222023-06-24%22,%22start_date_2%22:%222023-06-17%22,%22end_date%22:%222023-06-30%22,%22end_date_2%22:%222023-06-23%22,%22goal%22:None,%22display_unenriched%22:True,%22display_admon_alignment%22:False,%22skan_redownloads_dimensions%22:%5B%5D,%22skan_validated_dimensions%22:%5B%5D,%22confidence_interval_flag%22:%5B%5D,%22bookmark_id%22:%22%22,%22bookmark_creator%22:%22%22,%22updatedInstanceId%22:%22%22,%22is_fraud%22:False,%22is_skan_summary%22:False,%22is_ios_report%22:False,%22is_skan%22:False,%22is_admon_report%22:False,%22pivot_table%22:%7B%7D,%22query_type%22:%22reports%22,%22is_slim_mode%22:True,%22is_async%22:False,%22is_download_report%22:False,%22post_process_filters_ui%22:%7B%7D%7D",
    "mfaToken": "None",
    "password": "Fxh1997321."
}

cookies = {
    'csrftoken': '{}'.format(csrf_token)
}
# 创建一个Session 对象
# session = requests.Session()

login_response = requests.post(url=login_url, headers=headers, json=requests_payload, cookies=cookies)

login_cookies = login_response.cookies

# 数据接口请求头对应的csrf_token
data_csrf_token = login_response.cookies.get('csrftoken', '')
# print(data_csrf_token)

# 检查登录是否成功
if login_response.status_code == 200:
    print("登录成功！")
else:
    print("登录失败。")

# 在后续的请求中继续使用同一个 Session 对象,获取数据
data_url = 'https://app.singular.net/api/get_new_data'

headers_data = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "no-cache",
    "Content-Length": "3240",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://app.singular.net",
    "Pragma": "no-cache",
    "Referer": "https://app.singular.net/",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
    "X-Browser-Location": "https://app.singular.net/#/react/reports?query=%7B%22compare%22:False,%22is_goals%22:False,%22dimensions%22:%5B%22adn_account_id%22,%22country_field%22,%22unified_campaign_id%22,%22unified_campaign_name%22%5D,%22metrics%22:%5B%22custom_impressions%22,%22custom_clicks%22,%22custom_installs%22,%22adn_cost%22%5D,%22discrepancy_metrics%22:%5B%5D,%22file_combiner_dimensions%22:%5B%5D,%22granularity_levels%22:%5B%5D,%22enrichment_dimensions%22:%5B%5D,%22source_dimensions%22:%5B%5D,%22metadata_dimensions%22:%5B%5D,%22skan_conversion_dimensions%22:%5B%5D,%22cohort_metrics%22:%5B%22revenue%22%5D,%22modeled_skan_custom_events%22:%5B%5D,%22cohort_periods%22:%5B%22actual%22%5D,%22goals_metrics%22:%5B%5D,%22goals_forecast_metrics%22:%5B%5D,%22filters%22:%5B%5D,%22time_breakdown%22:%5B%22all%22%5D,%22source_attribution_type%22:%5B%5D,%22with_append_tables%22:%5B%5D,%22cross_device_cohort_type%22:%5B%5D,%22dual_attribution_mode%22:%5B%5D,%22cross_device_demo_cohort_type%22:%5B%5D,%22start_date%22:%222023-06-27%22,%22start_date_2%22:%222023-06-20%22,%22end_date%22:%222023-07-03%22,%22end_date_2%22:%222023-06-26%22,%22goal%22:None,%22display_unenriched%22:True,%22display_admon_alignment%22:False,%22skan_redownloads_dimensions%22:%5B%5D,%22skan_validated_dimensions%22:%5B%5D,%22confidence_interval_flag%22:%5B%5D,%22bookmark_id%22:%22%22,%22bookmark_creator%22:%22%22,%22is_fraud%22:False,%22is_skan_summary%22:False,%22is_ios_report%22:False,%22is_skan%22:False,%22is_admon_report%22:False,%22pivot_table%22:%7B%7D,%22query_type%22:%22reports%22,%22is_slim_mode%22:False,%22is_async%22:False,%22is_download_report%22:False,%22post_process_filters_ui%22:%7B%7D,%22column_order%22:%5B%5D%7D",
    "X-Csrftoken": "{}".format(data_csrf_token),
    "X-Org": "dsport"
}

# 请求为post,payload是字典格式,就用data,请求字段中很少用到json,一般为data
data = {"is_dashboard": False, "display_unenriched": True, "display_admon_alignment": False, "is_default": True,
        "chart": True, "is_goals": False, "start_date": "2023-06-27", "end_date": "2023-07-03",
        "start_date_2": "2023-06-20", "end_date_2": "2023-06-26", "compare": False,
        "dimensions": ["adn_account_id", "country_field", "unified_campaign_id", "unified_campaign_name"],
        "metrics": ["custom_impressions", "custom_clicks", "custom_installs", "adn_cost"], "goals_metrics": [],
        "goals_forecast_metrics": [], "goal": None, "discrepancy_metrics": [], "cohort_metrics": ["revenue"],
        "cohort_periods": ["actual"], "filters": [
        {"dimension": "country_field", "operator": "in", "values": ["PH", "ID", "MY", "US", "TH"],
         "options": {"no_lowercase": True}}], "time_breakdown": ["day"], "permutation_keys": [
        {"name": "country_field", "display_name": "Country", "is_default": False, "visible": True,
         "slim_mode_visible": True, "fraud_visible": True, "creative_visible": True, "ad_monetization_visible": False,
         "cross_device_visible": True, "skan_visible": True, "skan_summary_visible": True,
         "standard_analytics_visible": True, "id": 36, "display_format": None, "sorting_id": None, "type": "dimension"},
        {"name": "unified_campaign_name", "display_name": "Campaign Name", "is_default": False, "visible": True,
         "slim_mode_visible": True, "creative_visible": True, "fraud_visible": True, "skan_visible": True,
         "skan_summary_visible": True, "cross_device_visible": True, "ios_report_visible": True,
         "standard_analytics_visible": True, "id": 38, "display_format": None, "sorting_id": None, "type": "dimension"},
        {"name": "adn_account_id", "display_name": "Account ID", "visible": True, "slim_mode_visible": True,
         "is_default": False, "creative_visible": True, "cross_device_visible": True,
         "standard_analytics_visible": True, "id": 43, "display_format": None, "sorting_id": None, "type": "dimension"},
        {"name": "unified_campaign_id", "display_name": "Campaign ID", "is_default": False, "visible": True,
         "slim_mode_visible": True, "cross_device_visible": True, "creative_visible": True, "fraud_visible": True,
         "skan_visible": True, "skan_summary_visible": True, "ios_report_visible": True,
         "standard_analytics_visible": True, "id": 220, "display_format": None, "sorting_id": None,
         "type": "dimension"}],
        "valid_key_list_for_charts": [["Philippines", "Test-Gem-MobiSummer", "N%2FA", "Test-Gem-MobiSummer"],
                                      ["Indonesia", "Test-Gem-MobiSummer", "N%2FA", "Test-Gem-MobiSummer"],
                                      ["Malaysia", "Test-Gem-MobiSummer", "N%2FA", "Test-Gem-MobiSummer"],
                                      ["United%20States", "Test-Gem-MobiSummer", "N%2FA", "Test-Gem-MobiSummer"],
                                      ["Thailand", "Test-Gem-MobiSummer", "N%2FA", "Test-Gem-MobiSummer"]],
        "valid_key_name_list_for_charts": ["country_field", "unified_campaign_name", "adn_account_id",
                                           "unified_campaign_id"], "file_combiner_dimensions": [],
        "granularity_levels": [], "enrichment_dimensions": [], "source_dimensions": [], "metadata_dimensions": [],
        "skan_conversion_dimensions": [], "modeled_skan_custom_events": [], "source_attribution_type": [],
        "with_append_tables": [], "cross_device_cohort_type": [], "dual_attribution_mode": [],
        "cross_device_demo_cohort_type": [], "skan_redownloads_dimensions": [], "skan_validated_dimensions": [],
        "confidence_interval_flag": [], "bookmark_id": "", "bookmark_creator": "", "is_fraud": False,
        "is_skan_summary": False, "is_ios_report": False, "is_skan": False, "is_admon_report": False, "pivot_table": {},
        "query_type": "charts", "is_slim_mode": True}
# data_dict1['start_date'] = start_data
# data_dict1['end_dat'] = end_data
# print(data)

response_data = requests.post(url=data_url, headers=headers_data, data=json.dumps(data), cookies=login_cookies).json()

# print(response_data)
# print(response_data)
#
data_fields = response_data['value']["results"]
# print(data_fields)
for data_field in data_fields:
    # print(data_field)
    country = data_field['country_field']
    campaign_name = data_field['unified_campaign_name']
    account_id = data_field['adn_account_id']
    campaign_id = data_field['unified_campaign_id']
    impressions = data_field['custom_impressions']
    clicks = data_field['custom_clicks']
    installs = data_field['custom_installs']
    cost = data_field['adn_cost']
    revenue_actual = data_field['revenue']['actual']
    print(country, campaign_name, account_id, campaign_id, impressions, clicks, installs, cost, revenue_actual)
