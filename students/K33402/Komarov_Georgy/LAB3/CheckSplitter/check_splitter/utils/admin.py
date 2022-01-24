from simple_history.admin import SimpleHistoryAdmin


class ExtendedAdmin(SimpleHistoryAdmin):
    extended_fields = ['created_at', 'created_by', 'updated_at', 'updated_by']

    def get_fieldsets(self, request, obj=None):
        fieldsets = list(super().get_fieldsets(request, obj))

        for fieldset in fieldsets:
            name, data = fieldset
            fields = data.get('fields')
            if fields is not None:
                data['fields'] = list(filter(lambda field: field not in self.extended_fields, fields))

        fieldsets.append(
            ('Служебная информация', {
                'fields': self.extended_fields,
            })
        )
        return fieldsets

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super().get_readonly_fields(request, obj)
        readonly_fields_set = set(readonly_fields)
        readonly_fields_set.update(set(self.extended_fields))
        return list(readonly_fields_set)
