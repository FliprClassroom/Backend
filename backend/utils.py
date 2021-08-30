
from rest_framework_simplejwt.authentication import JWTAuthentication

def getUserFromHeader(request):
    # To get user from the token present in header
    JWT = JWTAuthentication()
    header = JWT.get_header(request)
    try: raw_token = JWT.get_raw_token(header)
    except: return {}
    validated_token = JWT.get_validated_token(raw_token)
    user = JWT.get_user(validated_token)
    return user