## Personalize App

You should consider following changes to make Django Accelerator your own.

- **Personalize logo :** Simply switch favicon.ico, favicon.png, logo-blue.png, logo-white.png, and logo.png. These files are located @ `/home/static/assets/img/`

- **Personalize `About Us` page :** Open aboutus.html @ `/home/templates/common/aboutus.html`, and edit content.

- **Personalize `Disclaimer` page :** Open disclaimer.html @ `/home/templates/common/disclaimer.html`, and edit content.

- **Personalize `404` and `500` pages :** Pages are located here [404] @ `/home/templates/404.html` and [500] `/home/templates/500.html`

- **Personalize `Login` page :** Login page is located @ `/templates/account/login.html`

- **Personalize `Home` page :** Page is locaed @ `/home/templates/index.html` 

For example, open `index.html` and add following.
```
{% extends "common/base_sidebar.html" %}
{% load static %} 
{% block page_content %}

    <h1> My Amazing Home Page</h1>

{% endblock %}

```

**Save and refresh home page.**