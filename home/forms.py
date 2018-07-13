from django import forms
from home.models import NhanXet


class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.tac_gia = kwargs.pop('tac_gia', None)
        self.sach = kwargs.pop('sach', None)
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['rows'] = '4'

    def save(self, commit=True):
        nhan_xet = super().save(commit=False)
        nhan_xet.tac_gia = self.tac_gia
        nhan_xet.sach = self.sach
        nhan_xet.save()

    class Meta:
        model = NhanXet
        fields = ['noi_dung']