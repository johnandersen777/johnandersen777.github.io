+++
date = 2021-04-02T15:00:00Z
lastmod = 2021-04-02T15:00:00Z
author = "default"
title = "Kernelci"
+++


Neelima and John setting up KernelCI

Working off https://github.com/kernelci/kernelci-backend-config/blob/master/INSTALL.md

We clone the config

```console
git clone https://github.com/kernelci/kernelci-backend-config.git
```

We found out that you have to create a file for each host under `host_vars/`

```diff

```

```
127.0.0.1 - - [07/Apr/2021 14:22:13] "GET / HTTP/1.1" 500 -
Traceback (most recent call last):
  File "/srv/kernelci-frontend/.venv/lib/python2.7/site-packages/flask/app.py", line 2301, in __call__
    return self.wsgi_app(environ, start_response)
  File "/srv/kernelci-frontend/.venv/lib/python2.7/site-packages/flask/app.py", line 2287, in wsgi_app
    response = self.handle_exception(e)
  File "/srv/kernelci-frontend/.venv/lib/python2.7/site-packages/flask/app.py", line 1733, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "/srv/kernelci-frontend/.venv/lib/python2.7/site-packages/flask/app.py", line 2284, in wsgi_app
    response = self.full_dispatch_request()
  File "/srv/kernelci-frontend/.venv/lib/python2.7/site-packages/flask/app.py", line 1807, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/srv/kernelci-frontend/.venv/lib/python2.7/site-packages/flask/app.py", line 1705, in handle_user_exception
    return self.handle_http_exception(e)
  File "/srv/kernelci-frontend/.venv/lib/python2.7/site-packages/flask/app.py", line 1642, in handle_http_exception
    return handler(e)
  File "/srv/kernelci-frontend/app/dashboard/__init__.py", line 155, in internal_server_error
    return render_template("500.html", page_content=page_content), 500
  File "/srv/kernelci-frontend/.venv/lib/python2.7/site-packages/flask/templating.py", line 133, in render_template
    ctx.app.update_template_context(context)
  File "/srv/kernelci-frontend/.venv/lib/python2.7/site-packages/flask/app.py", line 790, in update_template_context
    context.update(func())
  File "/srv/kernelci-frontend/app/dashboard/__init__.py", line 128, in inject_variables
    back_version=backend.get_version(),
  File "/srv/kernelci-frontend/.venv/lib/python2.7/site-packages/flask_cache/__init__.py", line 537, in decorated_function
    rv = f(*args, **kwargs)
  File "/srv/kernelci-frontend/app/dashboard/utils/backend.py", line 420, in get_version
    data, status_code, headers = request_get(url)
  File "/srv/kernelci-frontend/app/dashboard/utils/backend.py", line 277, in request_get
    abort(500)
  File "/srv/kernelci-frontend/.venv/lib/python2.7/site-packages/werkzeug/exceptions.py", line 772, in abort
    return _aborter(status, *args, **kwargs)
  File "/srv/kernelci-frontend/.venv/lib/python2.7/site-packages/werkzeug/exceptions.py", line 753, in __call__
    raise self.mapping[code](*args, **kwargs)
InternalServerError: 500 Internal Server Error: The server encountered an internal error and was unable to complete your request. Either the server is overloaded or there is an error in the application.
```

Which made it so that every time I made a request, I started seeing this in the
logs (directly above the traceback).

```
http://api.mydomain.local/version
127.0.0.1 - - [07/Apr/2021 14:22:13] "GET / HTTP/1.1" 500 -
Traceback (most recent call last):
```

So it's making a request to: `http://api.mydomain.local/version`

I then looked in the /etc/hosts file, and saw that we must have lost the entries
for api.mydomain.local and frontend.mydomain.local So I re-added them and it's
no longer dumping the same traceback page.

Also, I created a systemd unit file to start the frontend service. It wasn't
clear to me how it was supposed to get started. I didn't see any docs about it
or anything in the repo or in the config repo for the frontend.

Create the virtualenv

```console
$ python2 -m virtualenv /srv/kernelci-frontend/.venv
```

Activate the virtualenv and install dependencies
```console
$ . srv/kernelci-frontend/.venv/bin/activate
$ pip install -r requirements.txt
```

Create the systemd service for the frontend

```console
cat > /etc/systemd/system/kernelci-frontend.service <<'EOF'
[Unit]
Description=Kernel CI Frontend Service
Requires=kernelci-backend.service
After=kernelci-backend.service

[Service]
Type=simple
User=www-data
Group=www-data
ProtectSystem=full
ProtectHome=true
NoNewPrivileges=true
PrivateTmp=true
SyslogIdentifier=kernelci-frontend
LimitNOFILE=65536
RestartSec=5
Restart=always
WorkingDirectory=/srv/kernelci-frontend/app
ExecStart=/srv/kernelci-frontend/.venv/bin/python -OO -R server.py

[Install]
WantedBy=multi-user.target
EOF
```

Reload the systemd daemon to see the new service file

```console
$ systemctl daemon-reload
```

Enable the frontend service to start on boot and use --now to start it now too

```console
$ systemctl enable --now kernelci-frontend
```

I had to do the systemd service file to see the log output. I think you had been
running it from an ssh session or something. So I stopped that process, and now
it runs under systemd. Which means we can see the log output with journalctl -xe

Oh, and the backend code is broken. So the patch in the that PR above needs to
be applied or else nothing works.

```console
cd /srv/kernelci-backend
curl -sfL https://github.com/kernelci/kernelci-backend/pull/285.patch | git am
```
