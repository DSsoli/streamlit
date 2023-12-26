import streamlit as st
import streamlit_authenticator as stauth

# credentials = \
# {'usernames': 
#     {'jsmith': 
#         {
#             'email': 'jsmith@gmail.com',
#             'name': 'John Smith', 
#             'password': 'abc'
#         }, 
#     'rbriggs': 
#         {
#             'email': 'rbriggs@gmail.com', 
#             'name': 'Rebecca Briggs', 
#             'password': 'def'
#         }
#     }
# }
# hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

# credentials = \
# {'usernames': 
#     {'jsmith': 
#         {
#             'email': 'jsmith@gmail.com',
#             'name': 'John Smith', 
#             'password': hashed_passwords[0]
#         }, 
#     'rbriggs': 
#         {
#             'email': 'rbriggs@gmail.com', 
#             'name': 'Rebecca Briggs', 
#             'password': hashed_passwords[1]
#         }
#     }
# }


import yaml
from yaml.loader import SafeLoader

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)
hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
print(hashed_passwords)
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

# authenticator = stauth.Authenticate(credentials=credentials,
#                                     key='some_signature_key',
#                     cookie_name='some_cookie_name',
#                     cookie_expiry_days=0)

name, authentication_status, username = authenticator.login('Login', 'main')
if authentication_status:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{name}*')
    st.title('Some content')
elif authentication_status is False:
    st.error('Username/password is incorrect')
elif authentication_status is None:
    st.warning('Please enter your username and password')
    
# if authentication_status:
#     try:
#         if authenticator.reset_password(username, 'Reset password'):
#             st.success('Password modified successfully')
#     except Exception as e:
#         st.error(e)
        

try:
    if authenticator.register_user('Register user', preauthorization=False):
        st.success('User registered successfully')
        with open('config.yaml', 'w') as file:
            yaml.dump(config, file, default_flow_style=False)
except Exception as e:
    st.error(e)