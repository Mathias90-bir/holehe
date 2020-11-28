from holehe.core import *
from holehe.useragent import *

def seoclercks(email):

    s = requests.session()

    headers = {
        'User-Agent': random.choice(ua["browsers"]["firefox"]),
        'Accept': '*/*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://www.seoclerks.com',
        'Connection': 'keep-alive',
    }

    r = s.get('https://www.seoclerks.com', headers=headers)
    try:
        if "token" in r.text:
            token = r.text.split('token" value="')[1].split('"')[0]
        if "__cr" in r.text:
            cr = r.text.split('__cr" value="')[1].split('"')[0]
    except:
        return ({"rateLimit": True, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})

    letters = string.ascii_lowercase
    username = ''.join(random.choice(letters) for i in range(6))
    password = ''.join(random.choice(letters) for i in range(6))

    data = {
      'token': str(token),
      '__cr': str(cr),
      'fsub': '1',
      'droplet': '',
      'user_username': str(username),
      'user_email': str(email),
      'user_password': str(password),
      'confirm_password': str(password)
    }

    response = s.post('https://www.seoclerks.com/signup/check', headers=headers, data=data)
    if 'The email address you entered is already taken.' in response.json()['message']:
        return ({"rateLimit": False, "exists": True, "emailrecovery": None, "phoneNumber": None, "others": None})
    else:
        return ({"rateLimit": False, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
