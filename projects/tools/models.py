import random
import string
import base64
import hashlib
from django.db import models

from projects.settings import ENV

# Create your models here.
class Tools:

    @staticmethod
    def genVerifierChallenge()->dict:
        code_verifier = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(43, 128)))
        code_challenge = hashlib.sha256(code_verifier.encode('utf-8')).digest()
        code_challenge = base64.urlsafe_b64encode(code_challenge).decode('utf-8').replace('=', '')
        
        OAUTH_CODE_CLIENT = ENV("OAUTH_CODE_CLIENT")
        
        results:dict = {
            'code_verifier': code_verifier,
            'code_challenge': code_challenge,
            'url': string.Template('http://127.0.0.1:8000/oauth/authorize/?response_type=code&code_challenge=$code_challenge&code_challenge_method=S256&client_id=$OAUTH_CODE_CLIENT&redirect_uri=http://127.0.0.1:8000/noexist/callback')
            .substitute(code_challenge=code_challenge,OAUTH_CODE_CLIENT=OAUTH_CODE_CLIENT)
        }
        
        return results
    