import json
import os
from functools import wraps
from urllib.request import urlopen
from fastapi import HTTPException, requests
from fastapi.security.oauth2 import get_authorization_scheme_param
from starlette.requests import Request
from jose import jwt

AUTH_USER = os.environ.get('AUTH0_USER')
AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
ALGORITHMS = os.environ.get('ALGORITHMS')
API_AUDIENCE = os.environ.get('API_AUDIENCE')
# AuthError Exception
'''
AuthError Exception
A standardized way to communicate auth failure modes
'''


class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code


# Auth Header
def get_token_auth_header(request: Request):
    if 'authorization' not in request.headers:
        raise AuthError({
            'code': 'autorization_header_messing',
            'description': 'Authorization header is expected.'
        }, 401)
    auth_headers = request.headers['authorization']
    header_parts = auth_headers.split(' ')
    if len(header_parts) != 2:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Auth header must be bearer token.'
        }, 401)
    if len(header_parts) > 2:
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Token not found.'
        }, 401)
    if header_parts[0].lower() != 'bearer':
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Authorization header must start withh "Bearer".'
        }, 401)
    return header_parts[1]


def check_permissions(permission, payload):
    print('2')
    # Check if permission is contained in payload
    print(payload, permission)
    if len(payload['permissions']) == 0:
        raise AuthError({
            'code': 'invalid_claims',
            'description': 'You have no permissions'
        }, 401)

    if 'permissions' not in payload:
        raise AuthError({
            'code': 'invalid_claims',
            'description': 'Permissions not included in JWT'
        }, 400)
    if permission not in payload['permissions']:
        raise AuthError({
            'code': 'unauthorized',
            'description': 'Permission not found'
        }, 401)
    return True


def verify_decode_jwt(token):
    # GET PUBLIC KKEY FROM 0AUTH
    rsa_key = {}
    url = 'http://%s/.well-known/jwks.json' % (AUTH0_DOMAIN)
    json_url = urlopen(url)
    jwks = json.loads((json_url.read()))
    unverified_header = jwt.get_unverified_header(token)
    for key in jwks['keys']:
        if key['kid'] == unverified_header['kid']:
            rsa_key = {
                'kty': key['kty'],
                'kid': key['kid'],
                'use': key['use'],
                'n': key['n'],
                'e': key['e']
            }
        if rsa_key:
            try:
                payload = jwt.decode(
                    token,
                    rsa_key,
                    algorithms=ALGORITHMS,
                    audience=API_AUDIENCE,
                    issuer='https://' + AUTH0_DOMAIN + '/'

                )
                return payload

            except jwt.ExpiredSignatureError:
                raise AuthError({
                    'code': 'token_expired',
                    'description': 'Token Expired'

                }, 401)
            except jwt.JWTClaimsError:
                raise AuthError({
                    'code': 'invalid_claims',
                    'description': 'Incorrect claims. check the audience and '
                                   'issuer. '
                }, 401)
            except Exception:
                raise AuthError({
                    'code': 'invalid_header',
                    'description': 'Unable to parse authentaction token.'
                }, 400)
        raise AuthError({
            'code': 'invalid_header',
            'description': 'Unable to find the appropriate key'
        }, 401)


def requires_auth(permission=''):
    def requires_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                req = kwargs.get('request')
                token = get_token_auth_header(req)
                payload = verify_decode_jwt(token)
                check_permissions(permission, payload)
            except Exception as p:
                raise HTTPException(status_code=404, detail="Unauthorized")
            return f(*args, **kwargs)

        return wrapper

    return requires_auth_decorator


def is_authenticated():
    def is_auth_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                token = get_token_auth_header()
                payload = verify_decode_jwt(token)
            except Exception as p:
                raise HTTPException(status_code=401, detail="Unauthorized")
            return f(payload, *args, **kwargs)

        return wrapper

    return is_auth_decorator
