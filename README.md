# vulnerable_flask_app

## Installation
```
pipenv --python 3.6.5 install
pipenv shell
pip install flask
```

## To run locally
```pipenv shell && export FLASK_APP=xss_flask.py && flask run```

## To expose the app to the rest of the network over port 80
```pipenv shell && export FLASK_APP=xss_flask.py && flask run --host=0.0.0.0 --port=80```

### Disclaimer

This application has multiple vulnerabilities in it! **Do not upload it to your hosting provider's public html folder(s) or Internet facing server(s)**, as they will most likely be compromised. Consider using a virtual machine (such as [VirtualBox](https://www.virtualbox.org/) or [VMware](https://www.vmware.com/)) to run this code, and segregate it from any other machines on your network.

I do not take responsibility for how you decide to use this code, or what you do with any of the knowledge that you glean from using it. I have made it for the purpose of educating developers on the dangers of writing insecure code. If your web server is compromised because you're running this code, it is not my responsibility.

**TL;DR: Be smart - don't host intentionally vulnerable code on your machines that have important functionality. If you do and something bad happens, it's not my problem.**
