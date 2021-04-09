USER_HEADERS = [
    {'key': 'id', 'label': 'ID', 'required': True, 'type': 'primary_key'},
    {'key': 'username', 'label': 'User Name', 'required': True, 'type': 'text'},
    {'key': 'first_name', 'label': 'First Name', 'required': True, 'type': 'text'},
    {'key': 'middle_name', 'label': 'Middle Name',
        'required': False, 'type': 'text'},
    {'key': 'last_name', 'label': 'Last Name', 'required': True, 'type': 'text'},
    {'key': 'email', 'label': 'Email', 'required': True, 'type': 'text'},
    {'key': 'phone', 'label': 'Phone', 'required': True, 'type': 'text'},
    {'key': 'gender', 'label': 'Gender', 'required': True, 'type': 'text'},
]

LOGIN_HEADERS = [
    {'key': 'email', 'label': 'Email', 'required': True, 'type': 'text'},
    {'key': 'password', 'label': 'Password', 'required': True, "type": 'password'},
]

REGISTER_HEADERS = [
    {'key': 'username', 'label': 'User Name', 'required': True, 'type': 'text'},
    {'key': 'password', 'label': 'Password', 'required': True, 'type': 'text'},
]
