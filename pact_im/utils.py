import re


def camel_to_snake(value: str) -> str:
    value = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', value)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', value).lower()


def snake_to_camel(value: str) -> str:
    return ''.join(word.title() for word in value.split('_'))
