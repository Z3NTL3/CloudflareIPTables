# CloudflareIPTables
Automated script that automatically sets up cloudflare cdn's reverse proxy technology on your iptables and blocks all requests outside of cloudflare cdn's reverse proxy.

Simply a powerful protection against DDOS.

Reverse Proxy technology filters every request with certain algorithms and different methods. This will protect your server well. You have to hide the static IP. Layer 7 attacks will not work after this setup.


# Requirements
``iptables``
``curl``
``linux/debain OS``
<br>
sudo apt get install curl

<br>
Do not run this on WINDOWS.

# Logs
``logs.log`` after running the script.

# Revere Proxy
https://www.cloudflare.com/learning/cdn/glossary/reverse-proxy/
