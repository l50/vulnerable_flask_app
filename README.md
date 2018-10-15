# vulnerable_flask_app
This will allow you to run a vulnerable flask application in a docker
container

## Stand up a vulnerable instance
```make all```

You will find a running instance of the web application at localhost:5000

### Disclaimer

This application has multiple vulnerabilities in it! **Do not upload the code to your hosting provider's public html folder(s) or Internet facing server(s)**, as they will most likely be compromised. Consider using a virtual machine (such as [VirtualBox](https://www.virtualbox.org/) or [VMware](https://www.vmware.com/)) to run the container (or the code on its own), and segregate it from any other machines on your network.

I do not take responsibility for how you decide to use this code, or what you do with any of the knowledge that you glean from using it. I have made it for the purpose of educating developers on the dangers of writing insecure code. If your web server is compromised because you're running this code, or the container, it is not my responsibility.

**TL;DR: Be smart - don't host intentionally vulnerable code on your machines that have important functionality. The same goes with vulnerable containers. If you do and something bad happens, it's not my problem.**

### TODO:
- [] Deserialization
- [] XXE 
- [] SSRF
