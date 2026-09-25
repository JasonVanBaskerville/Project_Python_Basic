def lowercase(old_sett):
    new_sett = {}
    for key, value in old_sett.items():
        new_key = key.lower()

        if isinstance(value, str):
            new_value = value.lower()
        else:
            new_value = value

        new_sett[new_key] = new_value
    return new_sett

def add_setting(settings, sett):
    key, value = sett
    key = key.lower()
    if isinstance(value, str):
        value = value.lower()

    if key in settings.keys():
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings, sett):
    key, value = sett
    key = key.lower()
    if isinstance(value, str):
        value = value.lower()

    if key in settings.keys():
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings, key):
    key = key.lower()

    if key in settings.keys():
        del settings[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return f"Setting not found!"

def view_settings(settings):
    if not settings:
        return f"No settings available."
    else: 
        text = "Current User Settings:"
        for key, value in settings.items():
            text += '\n' + key.capitalize() + ': ' + value
        text += '\n'
        return text





test_settings = {
    'Theme': 'dark',
    'Notifications': 'enabled',
    'Volume': 'high'
}
test_settings = lowercase(test_settings)


print(add_setting({'theme': 'light'}, ('THEME', 'dark')))

print(add_setting({'theme': 'light'}, ('volume', 'high')))

print(update_setting({'theme': 'light'}, ('theme', 'dark')))

print(update_setting({'theme': 'light'}, ('volume', 'high')))

print(delete_setting({'theme': 'light'}, 'theme'))

print(delete_setting({'theme': 'light'}, 'volume'))

print(view_settings(test_settings))

