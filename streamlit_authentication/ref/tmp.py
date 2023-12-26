import yaml
from yaml.loader import SafeLoader

with open('/home/soli/Desktop/streamlit_authentication/ref/config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

#print(config)

dict_ = \
{
    'cookie': 
    {
        'expiry_days': 30, 
        'key': 'some_signature_key', 
        'name': 'some_cookie_name'
    }, 
    'credentials': 
        {
            'usernames': 
                {
                    'asdf': 
                        {
                            'email': 'asdf@gmail.com', 
                            'name': 'asdf', 
                            'password': '$2b$12$j45vUyYpqemj3zflLZ8rJ.WyuEW.KXovMLTlwXgsrOZNEEWIoghJa'
                        }, 
                    'jsmith': 
                        {
                            'email': 'jsmith@gmail.com', 
                            'name': 'John Smith', 
                            'password': '$2b$12$B.VwWHP22pRPtWotm7B5JOjYnGvuvlO/jw1cIJlnA/4i7S/eOy6DO'
                        }, 
                    'rbriggs': 
                        {
                            'email': 'rbriggs@gmail.com', 
                            'name': 'Rebecca Briggs', 
                            'password': '$2b$12$I.QiR8apCAqYxSjl0TGwyeuLQ7iBK1uIl1Vfn5qiEzb7qAgk.kEe2'
                        }
                }
            }
}