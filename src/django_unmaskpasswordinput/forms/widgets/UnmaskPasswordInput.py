from django.forms.widgets import Input

class UnmaskPasswordInput(Input):
    input_type = 'password'
    template_name = 'forms/widgets/unmaskpassword.html'
    
    class Media:
        css = {
            'all': ('django_unmaskpasswordinput/css/bootstrap.min.css','django_unmaskpasswordinput/css/fontawesome.min.css','django_unmaskpasswordinput/css/solid.min.css','django_unmaskpasswordinput/css/regular.min.css')
        }
        js = ('django_unmaskpasswordinput/js/jquery-3.4.1.min.js','django_unmaskpasswordinput/js/bootstrap.bundle.min.js','django_unmaskpasswordinput/js/bootstrap-show-password.min.js')

    def __init__(self, attrs=None, render_value=False):
        super().__init__(attrs)
        self.render_value = render_value

    def get_context(self, name, value, attrs):
        if not self.render_value:
            value = None
        return super().get_context(name, value, attrs)