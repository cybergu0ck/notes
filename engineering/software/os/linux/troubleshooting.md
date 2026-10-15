[← Back to linux](./contents.md)

# Contents

- [Troubleshooting](#troubleshooting)
  - [Issue with download](#issue-with-download)

<br>
<br>
<br>



# Troubleshooting

<br/>
<br/>
<br/>

## Issue with download

I get the following error when running the following command, because the package that I trying to get doesn't default to correct ipv settings automatically.

```bash
sudo add-apt-repository ppa:openrazer/stable
```

```
Traceback (most recent call last): File "/usr/bin/add-apt-repository", line 452, in <module> sys.exit(0 if addaptrepo.main() else 1) ^^^^^^^^^^^^^^^^^ File "/usr/bin/add-apt-repository", line 435, in main shortcut = handler(source, **shortcut_params) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3/dist-packages/softwareproperties/shortcuts.py", line 40, in shortcut_handler return handler(shortcut, **kwargs) ^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3/dist-packages/softwareproperties/ppa.py", line 89, in __init__ if self.lpppa.publish_debug_symbols: ^^^^^^^^^^ File "/usr/lib/python3/dist-packages/softwareproperties/ppa.py", line 133, in lpppa self._lpppa = self.lpteam.getPPAByName(name=self.ppaname) ^^^^^^^^^^^ File "/usr/lib/python3/dist-packages/softwareproperties/ppa.py", line 120, in lpteam self._lpteam = self.lp.people(self.teamname) ^^^^^^^ File "/usr/lib/python3/dist-packages/softwareproperties/ppa.py", line 111, in lp self._lp = login_func("%s.%s" % (self.__module__, self.__class__.__name__), ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3/dist-packages/launchpadlib/launchpad.py", line 494, in login_anonymously return cls( ^^^^ File "/usr/lib/python3/dist-packages/launchpadlib/launchpad.py", line 230, in __init__ super(Launchpad, self).__init__( File "/usr/lib/python3/dist-packages/lazr/restfulclient/resource.py", line 511, in __init__ self._wadl = self._browser.get_wadl_application(self._root_uri) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3/dist-packages/lazr/restfulclient/_browser.py", line 502, in get_wadl_application response, content = self._request(url, media_type=wadl_type) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3/dist-packages/lazr/restfulclient/_browser.py", line 441, in _request response, content = self._request_and_retry( ^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3/dist-packages/lazr/restfulclient/_browser.py", line 400, in _request_and_retry response, content = self._connection.request( ^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3/dist-packages/httplib2/__init__.py", line 1732, in request (response, content) = self._request( ^^^^^^^^^^^^^^ File "/usr/lib/python3/dist-packages/launchpadlib/launchpad.py", line 144, in _request response, content = super(LaunchpadOAuthAwareHttp, self)._request( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3/dist-packages/lazr/restfulclient/_browser.py", line 204, in _request return super(RestfulHttp, self)._request( ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3/dist-packages/httplib2/__init__.py", line 1452, in _request (response, content) = self._conn_request(conn, request_uri, method, body, headers) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/usr/lib/python3/dist-packages/httplib2/__init__.py", line 1374, in _conn_request conn.connect() File "/usr/lib/python3/dist-packages/httplib2/__init__.py", line 1139, in connect sock.connect((self.host, self.port)) TimeoutError: [Errno 110] Connection timed out
```

The fix is to temporarily disable IPV6 and run the command.

- To temporarily disable IPv6 (until the next reboot), run:

  ```bash
  sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1
  sudo sysctl -w net.ipv6.conf.default.disable_ipv6=1
  sudo sysctl -w net.ipv6.conf.lo.disable_ipv6=1
  ```

- Verify it's disabled:

  ```bash
  cat /proc/sys/net/ipv6/conf/all/disable_ipv6
  ```

- Retry the original command

  ```bash
  sudo add-apt-repository ppa:openrazer/stable
  ```

- Re-enable IPv6

  ```bash
  sudo sysctl -w net.ipv6.conf.all.disable_ipv6=0
  sudo sysctl -w net.ipv6.conf.default.disable_ipv6=0
  sudo sysctl -w net.ipv6.conf.lo.disable_ipv6=0
  ```

- Verify

  ```bash
  cat /proc/sys/net/ipv6/conf/all/disable_ipv6
  ```
