# Security Review

## HTTPS Settings

* **SECURE_SSL_REDIRECT = True** → Redirects all requests to HTTPS
* **HSTS enabled** → Forces browsers to always use HTTPS

## Secure Cookies

* **SESSION_COOKIE_SECURE = True**
* **CSRF_COOKIE_SECURE = True**
  Cookies are sent only over HTTPS.

## Security Headers

* **X_FRAME_OPTIONS = 'DENY'** → Prevents clickjacking
* **SECURE_CONTENT_TYPE_NOSNIFF = True** → Stops content-type guessing
* **SECURE_BROWSER_XSS_FILTER = True** → Helps prevent XSS attacks

## ✅ Result

The app is now secure and works safely with HTTPS.
