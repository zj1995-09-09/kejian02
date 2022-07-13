from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_v1_5
from base64 import b64encode
def get_sign(ts, token):
    s = token[:50] + ts
    key = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDQENQujkLfZfc5Tu9Z1LprzedE\nO3F7g s+7bzrgPsMl29LX8UoPYvIG8C604CprBQ4FkfnJpnhWu2lvUB0WZyLq6sBr\ntuPorOc42+gLnFfyhJAw dZB6SqWfDg7bW+jNe5Ki1DtU7z8uF6Gx+blEMGo8Dg+S\nkKlZFc8Br7SHtbL2tQIDAQAB\n-----END PUBLIC KEY-----\n'
    public_key = RSA.import_key(key)
    cipher = PKCS1_v1_5.new(public_key)
    encrypted_bytes = cipher.encrypt(s.encode())
    return b64encode(encrypted_bytes).decode()

def login():
    user = {
        "mobile_phone": "18211112222",
        "pwd": "12345678"
    }
    resp = requests.request(method='POST',
                            url='http://api.lemonban.com/futureloan' + '/member/login',
                            headers={"X-Lemonban-Media-Type": "lemonban.v3"},
                            json=user
                            )
    resp_json = resp.json()
    token = jsonpath(resp_json, '$..token')[0]
    token_type = jsonpath(resp_json, '$..token_type')[0]
    id = jsonpath(resp_json, '$..id')[0]
    leave_amount = jsonpath(resp_json, '$..leave_amount')[0]
    token = " ".join([token_type, token])
    return {"id": id,
            "token": token,
            "leave_amount": leave_amount}

def test_recharge():
    a = login()
    headers = {"X-Lemonban-Media-Type": "lemonban.v3",
               "Authorization": a['token']}

    ts = str(int(time.time()))
    sign = get_sign(ts, a['token'].split(' ')[1])
    # sign_msg = sign(ts, a['token'].split(' ')[1])
    # sign_data = encrypt(sign_msg)
    # msign = b64encode(sign_data).decode()
    data = {"member_id": a['id'], "amount": 100,
            "timestamp": ts,
            "sign":sign}
    resp = requests.request(url='http://api.lemonban.com/futureloan' + '/member/recharge',
                            method='post',
                            headers=headers,
                            json=data)
    print(resp.json())
if __name__ == '__main__':
    test_recharge()