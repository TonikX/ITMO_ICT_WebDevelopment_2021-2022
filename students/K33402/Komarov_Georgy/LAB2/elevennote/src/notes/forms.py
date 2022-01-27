from django import forms

from .models import Note, Tag
from accounts.models import User


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'body']

    field_order = ['title', 'tags', 'shared', 'body']

    tags = forms.CharField(label='Tags', required=False,
                           widget=forms.TextInput(attrs={'data-role': 'tagsinput',
                                                         'placeholder': 'Add a tag',
                                                         'class': 'd-block w-25'}))

    shared = forms.CharField(label='Share to users', required=False,
                             widget=forms.TextInput(attrs={'data-role': 'tagsinput',
                                                           'placeholder': 'Share to users',
                                                           'class': 'd-block w-25'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk is not None:
            existing_tags = ','.join(map(str, self.instance.tags.all()))
            if existing_tags:
                self.fields['tags'].widget.attrs['value'] = existing_tags

            shared_users = ','.join(map(str, self.instance.shared.all()))
            if shared_users:
                self.fields['shared'].widget.attrs['value'] = shared_users

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        tags_list = list(filter(lambda tag: tag, tags.split(',')))  # Remove empty tags from list
        max_length = Tag._meta.get_field('name').max_length
        cleaned_tags = list(filter(lambda tag: 0 < len(tag) < max_length, tags_list))

        if len(cleaned_tags) != len(tags_list):
            raise forms.ValidationError(f'Tag name must not exceed {max_length} characters! '
                                        f'Please, remove these tags: {", ".join(set(tags_list) - set(cleaned_tags))}')
        return cleaned_tags

    def clean_shared(self):
        shared_users = self.cleaned_data.get('shared')
        users_list = list(filter(lambda user: user, shared_users.split(',')))

        users_existing = []
        users_not_found = []
        for user_email in users_list:
            try:
                user_db = User.objects.get(email=user_email)
                users_existing.append(user_db)
            except User.DoesNotExist:
                users_not_found.append(user_email)
        if users_not_found:
            raise forms.ValidationError(f'User(s) {", ".join(users_not_found)} not found!')
        return users_existing

    def save(self, commit=True):
        instance = super().save(commit=commit)

        tags = self.cleaned_data.get('tags')
        instance.tags.clear()

        for tag in tags:
            tag, created = Tag.objects.get_or_create(name=tag)
            instance.tags.add(tag)

        shared_users = self.cleaned_data.get('shared')
        instance.shared.set(shared_users)

        instance.save()
        return instance
