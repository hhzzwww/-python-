from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By

url = 'https://app.singular.net/#/react/reports?query=%7B%22compare%22:false,%22is_goals%22:false,%22dimensions%22:%5B%22adn_account_id%22,%22country_field%22,%22unified_campaign_id%22,%22unified_campaign_name%22%5D,%22metrics%22:%5B%22custom_impressions%22,%22custom_clicks%22,%22custom_installs%22,%22adn_cost%22%5D,%22discrepancy_metrics%22:%5B%5D,%22file_combiner_dimensions%22:%5B%5D,%22granularity_levels%22:%5B%5D,%22enrichment_dimensions%22:%5B%5D,%22source_dimensions%22:%5B%5D,%22metadata_dimensions%22:%5B%5D,%22skan_conversion_dimensions%22:%5B%5D,%22cohort_metrics%22:%5B%22revenue%22%5D,%22modeled_skan_custom_events%22:%5B%5D,%22cohort_periods%22:%5B%22actual%22%5D,%22goals_metrics%22:%5B%5D,%22goals_forecast_metrics%22:%5B%5D,%22filters%22:%5B%5D,%22time_breakdown%22:%5B%22all%22%5D,%22source_attribution_type%22:%5B%5D,%22with_append_tables%22:%5B%5D,%22cross_device_cohort_type%22:%5B%5D,%22dual_attribution_mode%22:%5B%5D,%22cross_device_demo_cohort_type%22:%5B%5D,%22start_date%22:%222023-06-27%22,%22start_date_2%22:%222023-06-20%22,%22end_date%22:%222023-07-03%22,%22end_date_2%22:%222023-06-26%22,%22goal%22:null,%22display_unenriched%22:true,%22display_admon_alignment%22:false,%22skan_redownloads_dimensions%22:%5B%5D,%22skan_validated_dimensions%22:%5B%5D,%22confidence_interval_flag%22:%5B%5D,%22bookmark_id%22:%22%22,%22bookmark_creator%22:%22%22,%22is_fraud%22:false,%22is_skan_summary%22:false,%22is_ios_report%22:false,%22is_skan%22:false,%22is_admon_report%22:false,%22pivot_table%22:%7B%7D,%22query_type%22:%22reports%22,%22is_slim_mode%22:false,%22is_async%22:false,%22is_download_report%22:false,%22post_process_filters_ui%22:%7B%7D,%22column_order%22:%5B%5D%7D'

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, '//div/input[@id="login-email"]').send_keys('wustfanjunhao@163.com')
time.sleep(0.5)

driver.find_element(By.XPATH, '//div/input[@id="login-password"]').send_keys('Fxh1997321.')
time.sleep(0.5)

driver.find_elements(By.XPATH, '//form/button[@ng-click="login()"]')[0].click()

time.sleep(3)

cookies = driver.get_cookies()
# 将之前selenium登录获取的cookie信息保存到requests的会话中,并转化为字典形式
cookie = dict()
for item in cookies:
    cookie[item["name"]] = item["value"]

print(cookie)

data_url = 'https://app.singular.net/api/get_new_data'

data_csrftoken = cookie['csrftoken']
print(data_csrftoken)

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
    "X-Browser-Location": "https://app.singular.net/#/react/reports?query=%7B%22compare%22:false,%22is_goals%22:false,%22dimensions%22:%5B%22adn_account_id%22,%22country_field%22,%22unified_campaign_id%22,%22unified_campaign_name%22%5D,%22metrics%22:%5B%22custom_impressions%22,%22custom_clicks%22,%22custom_installs%22,%22adn_cost%22%5D,%22discrepancy_metrics%22:%5B%5D,%22file_combiner_dimensions%22:%5B%5D,%22granularity_levels%22:%5B%5D,%22enrichment_dimensions%22:%5B%5D,%22source_dimensions%22:%5B%5D,%22metadata_dimensions%22:%5B%5D,%22skan_conversion_dimensions%22:%5B%5D,%22cohort_metrics%22:%5B%22revenue%22%5D,%22modeled_skan_custom_events%22:%5B%5D,%22cohort_periods%22:%5B%22actual%22%5D,%22goals_metrics%22:%5B%5D,%22goals_forecast_metrics%22:%5B%5D,%22filters%22:%5B%5D,%22time_breakdown%22:%5B%22all%22%5D,%22source_attribution_type%22:%5B%5D,%22with_append_tables%22:%5B%5D,%22cross_device_cohort_type%22:%5B%5D,%22dual_attribution_mode%22:%5B%5D,%22cross_device_demo_cohort_type%22:%5B%5D,%22start_date%22:%222023-06-27%22,%22start_date_2%22:%222023-06-20%22,%22end_date%22:%222023-07-03%22,%22end_date_2%22:%222023-06-26%22,%22goal%22:null,%22display_unenriched%22:true,%22display_admon_alignment%22:false,%22skan_redownloads_dimensions%22:%5B%5D,%22skan_validated_dimensions%22:%5B%5D,%22confidence_interval_flag%22:%5B%5D,%22bookmark_id%22:%22%22,%22bookmark_creator%22:%22%22,%22is_fraud%22:false,%22is_skan_summary%22:false,%22is_ios_report%22:false,%22is_skan%22:false,%22is_admon_report%22:false,%22pivot_table%22:%7B%7D,%22query_type%22:%22reports%22,%22is_slim_mode%22:false,%22is_async%22:false,%22is_download_report%22:false,%22post_process_filters_ui%22:%7B%7D,%22column_order%22:%5B%5D%7D",
    "X-Csrftoken": "{}".format(data_csrftoken),
    "X-Org": "dsport"

}

json = {
    "{\"is_dashboard\"": "false,",
    "\"display_unenriched\"": "true,",
    "\"display_admon_alignment\"": "false,",
    "\"is_default\"": "true,",
    "\"chart\"": "true,",
    "\"is_goals\"": "false,",
    "\"start_date\"": "\"2023-06-27\",",
    "\"end_date\"": "\"2023-07-03\",",
    "\"start_date_2\"": "\"2023-06-20\",",
    "\"end_date_2\"": "\"2023-06-26\",",
    "\"compare\"": "false,",
    "\"dimensions\"": "[\"adn_account_id\",\"country_field\",\"unified_campaign_id\",\"unified_campaign_name\"],",
    "\"metrics\"": "[\"custom_impressions\",\"custom_clicks\",\"custom_installs\",\"adn_cost\"],",
    "\"goals_metrics\"": "[],",
    "\"goals_forecast_metrics\"": "[],",
    "\"goal\"": "null,",
    "\"discrepancy_metrics\"": "[],",
    "\"cohort_metrics\"": "[\"revenue\"],",
    "\"cohort_periods\"": "[\"actual\"],",
    "\"filters\"": "[{\"dimension\":\"country_field\",\"operator\":\"in\",\"values\":[\"PH\",\"ID\",\"MY\"],\"options\":{\"no_lowercase\":true}}],",
    "\"time_breakdown\"": "[\"day\"],",
    "\"valid_key_name_list_for_charts\"": "[\"country_field\",\"unified_campaign_name\",\"adn_account_id\",",
    "\"unified_campaign_id\"],": "",
    "\"file_combiner_dimensions\"": "[],",
    "\"granularity_levels\"": "[],",
    "\"enrichment_dimensions\"": "[],",
    "\"source_dimensions\"": "[],",
    "\"metadata_dimensions\"": "[],",
    "\"skan_conversion_dimensions\"": "[],",
    "\"modeled_skan_custom_events\"": "[],",
    "\"source_attribution_type\"": "[],",
    "\"with_append_tables\"": "[],",
    "\"cross_device_cohort_type\"": "[],",
    "\"dual_attribution_mode\"": "[],",
    "\"cross_device_demo_cohort_type\"": "[],",
    "\"skan_redownloads_dimensions\"": "[],",
    "\"skan_validated_dimensions\"": "[],",
    "\"confidence_interval_flag\"": "[],",
    "\"bookmark_id\"": "\"\",",
    "\"bookmark_creator\"": "\"\",",
    "\"is_fraud\"": "false,",
    "\"is_skan_summary\"": "false,",
    "\"is_ios_report\"": "false,",
    "\"is_skan\"": "false,",
    "\"is_admon_report\"": "false,",
    "\"pivot_table\"": "{},",
    "\"query_type\"": "\"charts\",\"is_slim_mode\":true}",
    "permutation_keys": '[{"name":"country_field","display_name":"Country","is_default":false,"visible":true,"slim_mode_visible":true,"fraud_visible":true,"creative_visible":true,"ad_monetization_visible":false,"cross_device_visible":true,"skan_visible":true,"skan_summary_visible":true,"standard_analytics_visible":true,"id":36,"display_format":null,"sorting_id":null,"type":"dimension"},{"name":"unified_campaign_name","display_name":"Campaign Name","is_default":false,"visible":true,"slim_mode_visible":true,"creative_visible":true,"fraud_visible":true,"skan_visible":true,"skan_summary_visible":true,"cross_device_visible":true,"ios_report_visible":true,"standard_analytics_visible":true,"id":38,"display_format":null,"sorting_id":null,"type":"dimension"},{"name":"adn_account_id","display_name":"Account ID","visible":true,"slim_mode_visible":true,"is_default":false,"creative_visible":true,"cross_device_visible":true,"standard_analytics_visible":true,"id":43,"display_format":null,"sorting_id":null,"type":"dimension"},{"name":"unified_campaign_id","display_name":"Campaign ID","is_default":false,"visible":true,"slim_mode_visible":true,"cross_device_visible":true,"creative_visible":true,"fraud_visible":true,"skan_visible":true,"skan_summary_visible":true,"ios_report_visible":true,"standard_analytics_visible":true,"id":220,"display_format":null,"sorting_id":null,"type":"dimension"}]'

}

response_data = requests.post(url=data_url, headers=headers_data, json=json, cookies=cookie)
# print(response_data.text)



# data = {
#     "is_dashboard": "false",
#     "display_unenriched": "true",
#     "display_admon_alignment": "false",
#     "is_default": "true",
#     "chart": "true",
#     "is_goals": "false",
#     "start_date": "2023-06-27",
#     "end_date": "2023-07-03",
#     "start_date_2": "2023-06-20",
#     "end_date_2": "2023-06-26",
#     "compare": "false",
#     "dimensions": "[adn_account_id,country_field,unified_campaign_id,unified_campaign_name]",
#     "metrics": "[custom_impressions,custom_clicks,custom_installs,adn_cost]",
#     "goals_metrics": "[]",
#     "goals_forecast_metrics": "[]",
#     "goal": "null",
#     "discrepancy_metrics": "[]",
#     "cohort_metrics": "[revenue]",
#     "cohort_periods": "[actual]",
#     "filters": "[{dimension:country_field,operator:in,values:[PH,ID,MY,US,TH],options:{no_lowercase:true}}]",
#     "time_breakdown": "[day]",
#     "valid_key_list_for_charts": "[[Philippines,Test-Gem-MobiSummer,N%2FA,Test-Gem-MobiSummer],[Indonesia,Test-Gem-MobiSummer,N%2FA,Test-Gem-MobiSummer],[Malaysia,Test-Gem-MobiSummer,N%2FA,Test-Gem-MobiSummer],[United%20States,Test-Gem-MobiSummer,N%2FA,Test-Gem-MobiSummer],[Thailand,Test-Gem-MobiSummer,N%2FA,Test-Gem-MobiSummer]]",
#     "valid_key_name_list_for_charts":'["country_field","unified_campaign_name","adn_account_id","unified_campaign_id"]',
#     "file_combiner_dimensions": "[]",
#     "granularity_levels": "[]",
#     "enrichment_dimensions": "[]",
#     "source_dimensions": "[]",
#     "metadata_dimensions": "[]",
#     "skan_conversion_dimensions": "[]",
#     "modeled_skan_custom_events": "[]",
#     "source_attribution_type": "[]",
#     "with_append_tables": "[]",
#     "cross_device_cohort_type": "[]",
#     "dual_attribution_mode": "[]",
#     "cross_device_demo_cohort_type": "[]",
#     "skan_redownloads_dimensions": "[]",
#     "skan_validated_dimensions": "[]",
#     "confidence_interval_flag": "[]",
#     "bookmark_id": "",
#     "bookmark_creator": "",
#     "is_fraud": "false",
#     "is_skan_summary": "false",
#     "is_ios_report": "false",
#     "is_skan": "false",
#     "is_admon_report": "false",
#     "pivot_table": "{}",
#     "query_type": "charts",
#     "is_slim_mode": "true",
#     "permutation_keys":'[{"name":"country_field","display_name":"Country","is_default":false,"visible":true,"slim_mode_visible":true,"fraud_visible":true,"creative_visible":true,"ad_monetization_visible":false,"cross_device_visible":true,"skan_visible":true,"skan_summary_visible":true,"standard_analytics_visible":true,"id":36,"display_format":null,"sorting_id":null,"type":"dimension"},{"name":"unified_campaign_name","display_name":"Campaign Name","is_default":false,"visible":true,"slim_mode_visible":true,"creative_visible":true,"fraud_visible":true,"skan_visible":true,"skan_summary_visible":true,"cross_device_visible":true,"ios_report_visible":true,"standard_analytics_visible":true,"id":38,"display_format":null,"sorting_id":null,"type":"dimension"},{"name":"adn_account_id","display_name":"Account ID","visible":true,"slim_mode_visible":true,"is_default":false,"creative_visible":true,"cross_device_visible":true,"standard_analytics_visible":true,"id":43,"display_format":null,"sorting_id":null,"type":"dimension"},{"name":"unified_campaign_id","display_name":"Campaign ID","is_default":false,"visible":true,"slim_mode_visible":true,"cross_device_visible":true,"creative_visible":true,"fraud_visible":true,"skan_visible":true,"skan_summary_visible":true,"ios_report_visible":true,"standard_analytics_visible":true,"id":220,"display_format":null,"sorting_id":null,"type":"dimension"}]'
# }