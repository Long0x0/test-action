import os
import send_message
print('hello world!')
try:
    if os.getenv('ACCOUNT'):
        print('account get.')
    if os.getenv('PASSWORD'):
        print('password get.')
    if os.getenv('token'):
        print('token get.')
    if os.getenv('INPUT_ACCOUNT'):
        print('input account get.')
    if os.getenv('INPUT_PASSWORD'):
        print('input password get.')
    if os.getenv('INPUT_TOKEN'):
        print('input token get.')
    token = os.environ['INPUT_TOKEN']
    if token:
        send_message.send_serverChan_message('test', 'test ok.', token)
        print('success')
    else:
        print('fail. empty token.')
except:
    print('fail. no token.')

print(*os.listdir())
with open("requirements.txt", "r", errors = "ignore") as f:
    f = f.read()
    print(f)
