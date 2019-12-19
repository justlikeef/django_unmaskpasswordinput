=====
Django_UnmaskPasswordInput
=====

Django_UnmaskPasswordInput provides a password text input that can be unmaksed
by clicking the icon on the right end of the field.


Quick start
-----------

1. Add "django_unmaskpasswordinput" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'django_unmaskpasswordinput',
    ]

2. (optional) Run `python manage.py collectstaticfiles` to copy the required js, css, and resources
to your static files location

3. Run ``python manage.py migrate`` to create the polls models.

4. In your form, import and use the input, for example:
.. code-block:: python
    :linenos:
    
    from django.forms import ModelForm
    from django_unmaskpasswordinput.forms.widgets.UnmaskPasswordInput import UnmaskPasswordInput

    class CredentialForm(ModelForm):
        class Meta:
            model = CredentialModel
            fields = '__all__'
            widgets = {
                'PasswordField': UnmaskPasswordInput(),
            }
