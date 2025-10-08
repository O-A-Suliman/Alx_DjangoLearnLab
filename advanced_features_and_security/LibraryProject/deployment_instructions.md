# Deployment Instructions (HTTPS Setup)

## 1. Get an SSL Certificate

Use **Let’s Encrypt** or another provider to get a free SSL certificate.

Example (for Nginx):

```bash
sudo apt install certbot python3-certbot-nginx
sudo certbot --nginx -d yourdomain.com
```

---

## 2. Configure Nginx

Example:

```nginx
server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

---

## 3. Update Django Settings

In `settings.py`:

```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

---

## 4. Test HTTPS

Restart the server and visit:

```
https://yourdomain.com
```
