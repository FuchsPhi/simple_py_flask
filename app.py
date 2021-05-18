import mod_wsgi.server

# mod_wsgi server start options: https://gist.github.com/csomh/4e9871f2b4d7cdad7151e439c892f6f8

mod_wsgi.server.start(
  '--log-to-terminal',
  '--log-level', 'info',
  '--access-log',
  '--port', '8080',
  '--trust-proxy-header', 'X-Forwarded-For',
  '--trust-proxy-header', 'X-Forwarded-Port',
  '--trust-proxy-header', 'X-Forwarded-Proto',
  '--application-type', 'module',
  '--entry-point', 'wsgi',
  '--limit-request-body', '1073741824'
)