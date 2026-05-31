# using dictionarys, conditional logic and loops

test_settings = {
    'theme': 'dark',
    'language': 'english',
    'notifications': 'disabled'
}
test_settings2 = {}

def add_setting(settings_dictionary, setting_to_add):
    key, value = setting_to_add
    key = key.lower()
    value = value.lower()
    if key in settings_dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings_dictionary[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
        
def update_setting(settings_dictionary, setting_to_update):
    key, value = setting_to_update
    key = key.lower()
    value = value.lower()
    if key in settings_dictionary:
        settings_dictionary[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    
def delete_setting(settings_dictionary, setting_to_delete):
    key = setting_to_delete
    key = key.lower()
    if key in settings_dictionary:
        del settings_dictionary[key]
        return f"Setting '{key}' deleted successfully!"
    else:
       return f"Setting not found!"   

def view_settings(settings_dictionary):
    if not bool(settings_dictionary):
        return "No settings available."
    user_settings = "Current User Settings:\n"
    for key, value in settings_dictionary.items():
        key = key.capitalize()
        user_settings += f"{key}: {value}\n"
    return user_settings
