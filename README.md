# CloudflareIPTables
Automated script that automatically sets up cloudflare cdn's reverse proxy technology on your iptables and blocks all requests outside of cloudflare cdn's reverse proxy.

Simply a powerful protection against DDOS.

Reverse Proxy technology filters every request with certain algorithms and different methods. This will protect your server well. You have to hide the static IP. Layer 7 attacks will not work after this setup.

This script does it all automatically for you ❤️. 
Scrapes always updated reverse proxy range of cloudflare. Run this script twice a month. Cloudflare updates their range always!

# Requirements
``iptables``
``curl``
``linux/debain OS``
```sudo access, run this as root!```
``Cloudflare``
<br>
sudo apt get install curl

<br>
Do not run this on WINDOWS.

# Logs
``logs.log`` after running the script.

# Reverse Proxy
https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/
