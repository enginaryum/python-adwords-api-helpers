# -*- coding: utf-8 -*-
client_id = ''
client_secret = ''
scopes = [u'https://www.googleapis.com/auth/adwords']

from oauth2client import client
import sys

def step1Exchange():
  flow = client.OAuth2WebServerFlow(
    client_id=client_id,
    client_secret=client_secret,
    scope=scopes,
    user_agent='Ads Python Client Library',
    redirect_uri='urn:ietf:wg:oauth:2.0:oob')

  authorize_url = flow.step1_get_authorize_url()
  return authorize_url


def step2Exchange(code):
  flow = client.OAuth2WebServerFlow(
    client_id=client_id,
    client_secret=client_secret,
    scope=scopes,
    user_agent='Ads Python Client Library',
    redirect_uri='urn:ietf:wg:oauth:2.0:oob')
  try:
    credential = flow.step2_exchange(code)
  except client.FlowExchangeError, e:
    return e
  else:
    return credential

def main(client_id=client_id, client_secret=client_secret, scopes=scopes):
  """Retrieve and display the access and refresh token."""
  flow = client.OAuth2WebServerFlow(
      client_id=client_id,
      client_secret=client_secret,
      scope=scopes,
      user_agent='Ads Python Client Library',
      redirect_uri='urn:ietf:wg:oauth:2.0:oob')

  authorize_url = flow.step1_get_authorize_url()

  print ('Log into the Google Account you use to access your AdWords account'
         'and go to the following URL: \n%s\n' % (authorize_url))
  print 'After approving the token enter the verification code (if specified).'
  code = raw_input('Code: ').strip()

  try:
    credential = flow.step2_exchange(code)
  except client.FlowExchangeError, e:
    print 'Authentication has failed: %s' % e
    sys.exit(1)
  else:

    print ('OAuth2 authorization successful!\n\n'
           'Your access token is:\n %s\n\nYour refresh token is:\n %s'
           % (credential.access_token, credential.refresh_token))
  return credential

