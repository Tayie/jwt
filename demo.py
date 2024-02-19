import base64
import hmac
def jwtbasencode(h: str, p: str, a: str):
    header = h.encode()
    payload = p.encode()

    h_b = base64.b64encode(header).replace(b'=',b'')
    p_b = base64.b64encode(payload).replace(b'=',b'')
    hp_b = h_b + b'.' + p_b

    c = hmac.new(a.encode(),hp_b,digestmod='sha512').digest() # digest 将hamc生成密文转为bytes  此处加密算法根据实际更改

    sig = base64.b64encode(c).replace(b'=',b'').replace(b'+',b'-').replace(b'/',b'_')

    jwt = hp_b + b'.' + sig
    return jwt



#顺便写个无脑的解密 当然解不出签名
def jwtbasedecode(s:str):
    h, p, sig = s.split('.')

    h += "=="
    p += "=="
    sig += "=="

    header = base64.b64decode(h)
    payload = base64.b64decode(p)
    print(header)
    print(payload)




if __name__ == '__main__':


    h = '{"alg":"HS512"}'
    p = '{"iat":1709136008,"admin":"true","user":"Tom"}'  # kv 之间不能有空格
    secret = 'your-256-bit-secret'
    print(jwtbasencode(h, p, secret))




