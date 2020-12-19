def get_form_fields(instance):
    """"
    Return names of all available fields from given Form instance.

    :arg instance: Form instance
    :returns list of field names
    :rtype: list
    """

    fields = []
    for item in instance.__dict__.items():
        if item[0] == 'declared_fields' or item[0] == 'base_fields':
            for field in item[1]:
                if hasattr(instance.Meta, 'exclude'):
                    if field not in instance.Meta.exclude:
                        fields.append(field)
                else:
                    fields.append(field)
    return fields


def get_model_fields(model):
    return model._meta.fields