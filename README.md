django-template-base
===========================

A simple boilerplate for django templates based on Twitter Bootstrap and select parts of the HTML5 Boilerplate project to get you up and running quickly.

This project aims to create a complete base.html (and dependent files) that you can use as a starting point for templates in your django projects. Currently support for Typekit and Google Analytics is baked in.

django-template-base sets you up with the following:

  - [Twitter Bootstrap](http://twitter.github.com/bootstrap/)
  - [HTML5Shiv](http://code.google.com/p/html5shiv/)
  - [jQuery](http://jquery.com/)
  - [Typekit](http://typekit.com)
  - [Google Analytics](http://google.com/analytics)
  
Feel free to fork this project if you'd like to create a different stack.


## How to use

**To avoid backwards compatible changes, you may want to fork this repository before including it in your project**

These instructions assume that you're already using git to manage your project.

If you haven't already, create a templates directory in your project

```
mkdir templates
```

Add the django-template-base into your templates directory as a submodule named "base"

```
git submodule add git@github.com:sesh/django-template-base.git templates/base
```

Create a couple of required files in your templates directory

```    
cd templates && touch style.css && touch header.html && touch footer.html && touch __init__.py
```

Finally, add out template processor to your settings.py files. The best practice for doing this is to extend the existing TEMPLATE_CONTEXT_PROCESSORS variable

Add this to the top of your settings.py:

```python
import django.conf.global_settings as DEFAULT_SETTINGS
```

Then, towards the bottom (I like to do it near the template paths), add update the TEMPLATE_CONTEXT_PROCESSORS as so:

```python
TEMPLATE_CONTEXT_PROCESSORS = DEFAULT_SETTINGS.TEMPLATE_CONTEXT_PROCESSORS + (
  "templates.base.base_processer.js_addins",
)

```

And include the new DJANGO_BASE_TEMPLATE dictionary, shown here with the default values:

```python
DJANGO_BASE_TEMPLATE = {
    'GOOGLE_ANALYTICS': None,       # String, begins with UA-
    'TYPEKIT': None,                # String
}
```

Use the provided sample.html file as a starting point for your own templates.