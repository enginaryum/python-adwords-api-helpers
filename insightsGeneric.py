# -*- coding: utf-8 -*-
#!/usr/bin/env python

import logging
from googleads import adwords
# from webapp.models import GoogleAdwordsAccount
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)


def main(client=None):
  if not client:
    client = adwords.AdWordsClient.LoadFromStorage()
  report_downloader = client.GetReportDownloader(version='v201705')
  fields = ['CampaignId', 'AdGroupId', 'Id', 'CriteriaType', 'Criteria', 'FinalUrls', 'Impressions', 'Clicks', 'Cost']
  # Create report definition.
  report = {
    'reportName': 'All Time CRITERIA_PERFORMANCE_REPORT',
    'dateRangeType': 'ALL_TIME',
    'reportType': 'CRITERIA_PERFORMANCE_REPORT',
    'downloadFormat': 'CSV',
    'selector': {
      'fields': fields
    }
  }
  result = report_downloader.DownloadReportAsString(
    report, skip_report_header=False, skip_column_header=False,
    skip_report_summary=False, include_zero_impressions=True, client_customer_id='378-771-7443')
  # format string result into json array
  splitted = result.split('\n')
  reportName = splitted.pop(0)
  map(lambda x: x.split(','), splitted)
  headers = splitted.pop(0).split(',')
  data = map(lambda x: x.split(','), splitted)
  resultDict = {'reportName': reportName, 'headers': headers, 'data': data}
  return resultDict


if __name__ == '__main__':
  adwords_client = adwords.AdWordsClient.LoadFromStorage()
  main(client=adwords_client)
