0-world_wide_web file: domain zone so that the subdomain www points to your load-balancer IP (lb-01)

1-haproxy_ssl_termination file: Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www.

100-redirect_http_to_https file: 