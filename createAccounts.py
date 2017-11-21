# -*- coding: utf-8 -*-
# !/usr/bin/env python

import logging
from googleads import adwords
from webapp.models import GoogleAdwordsAccount

logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.transport').setLevel(logging.DEBUG)


def createAdwordsAccounts(request, client=None):
  if not client:
    client = adwords.AdWordsClient.LoadFromStorage()
  customerService = client.GetService('CustomerService')
  customers = customerService.getCustomers()
  accounts = []
  for customer in customers:
    if not GoogleAdwordsAccount.objects.filter(customerId=str(customer['customerId'])).first():
      createdAccount = GoogleAdwordsAccount.objects.create(
        autoTaggingEnabled=customer['autoTaggingEnabled'],
        canManageClients=customer['canManageClients'],
        currencyCode=customer['currencyCode'],
        customerId=customer['customerId'],
        datetimeZone=customer['dateTimeZone'],
        descriptiveName=customer['descriptiveName'],
        testAccount=customer['testAccount'],
        turtleAccount=request.user.account
      )
      accounts.append(createdAccount)
  return accounts
