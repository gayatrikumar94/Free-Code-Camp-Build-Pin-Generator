def add_setting(test_settings,pair):
    key,value=pair
    key=key.lower()
    value=value.lower()
    
    if key in test_settings:
        return (f"Setting '{key}' already exists! Cannot add a new setting with this name.")
    else:
        test_settings[key]=value
        return (f"Setting '{key}' added with value '{value}' successfully!")

def update_setting(test_settings, pairs):
    key,value=pairs
    key=key.lower()
    value=value.lower()
    if key in test_settings:
        test_settings[key] = value
        return (f"Setting '{key}' updated to '{value}' successfully!")
    else:
        return (f"Setting '{key}' does not exist! Cannot update a non-existing setting.")
def delete_setting(test_settings,key):
    key= key.lower()
    if key in test_settings:
        del test_settings[key]
        return (f"Setting '{key}' deleted successfully!")
    else:
        return "Setting not found!"

def view_settings(test_settings):
    if not test_settings:
        return "No settings available."
    else:
        formated_lines = "Current User Settings:\n"
        for k, v in test_settings.items():
            formated_lines+= f"{k.capitalize()}: {v}\n"
        return formated_lines

    
test_settings= {'theme':'light'}
pair=('THEME','dark')
pairs=('theme', 'dark')
key= "theme"
setting={}

add_setting(test_settings,pair)
add_setting({'theme': 'light'}, ('volume', 'high'))
update_setting({'theme': 'light'}, ('theme', 'dark'))
update_setting({'theme': 'light'}, ('volume', 'high'))
delete_setting({'theme':'light'},"theme")
view_settings(setting)
formatted_setting=view_settings(test_settings)


