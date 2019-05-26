https://docs.djangoproject.com/en/1.11/ref/models/fields/
whitenoise django for static files
uploadcare django for uploads

index1.html:
          <li class="{% if url_name == 'shopping_cart' %}active{% endif %}">
            <a class="nav-link" href="{% url 'shopping_cart' %}">Shopping Cart</a>
          </li>
          <li class="{% if url_name == 'login_link' %}active{% endif %}">
            <a class="nav-link" href="{% url 'login_link' %}">Log In</a>
          </li>          
          
https://stackoverflow.com/questions/23343807/decimal12000-is-not-json-serializable?rq=1          
https://stackoverflow.com/questions/1960516/python-json-serialize-a-decimal-object
