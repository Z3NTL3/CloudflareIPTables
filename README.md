# CloudflareIPTables

Configures your firewall to only accept incoming connections from Cloudflare's reverse proxy CIDR/IP ranges. Blocking everything else but SSH port, which is limited (likely a rate-limit or block by ufw's limit pre-rule).

![Showcase](image/README/1709378975089.png)
#### Requirements

- ``python``
- ``httpx``
- ``numpy``

Installation:

```
git clone https://github.com/Z3NTL3/CloudflareIPTables
cd CloudflareIPTables
pip3 install -r requirements.txt
```
