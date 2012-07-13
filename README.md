django-template-boilerplate
===========================

A simple boilerplate for django templates based on Twitter Bootstrap and parts of the HTML5 Boilerplate project.

This project aims to create a complete base.html (and dependent files) that you can use as a starting point for templates in your django projects.


## How to use

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