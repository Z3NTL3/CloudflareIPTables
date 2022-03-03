# CloudflareIPTables
Automated script that automatically sets up cloudflare cdn's reverse proxy technology on your iptables and blocks all requests outside of cloudflare cdn's reverse proxy.

Simply a powerful protection against DDOS.

Reverse Proxy technology filters every request with certain algorithms and different methods. This will protect your server well. You have to hide the static IP. Layer 7 attacks will not work after this setup.

This script does it all automatically for you ❤️. 
Scrapes always updated reverse proxy range of cloudflare. Run this script twice a month. Cloudflare updates their range always!

# Requirements
``nothing the scripts does it all automaticly for you , you dont even need to connect to your SSH!``

Run at your local Windows 10 CMD or any other Terminal supporting Python3
```python3 cfiptables.py host port username pass```
The script will setup the iptables all automaticly for you and it will block all other traffic outside CF Proxies

# Reverse Proxy
https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/
