from service_exceptions import InvalidName
from service_exceptions import InvalidRecommendation
import re

class RecommendationValidator:
    @classmethod
    def validate_recommendation(cls, recommendation):
        errors = {}

        try:
            cls.validate_name(recommendation.title)
        except InvalidName as e:
            errors['name'] = e.message
        
        if len(errors) > 0:
            raise InvalidRecommendation(errors)

    @classmethod
    def validate_name(cls, name):
        errors = []
        # Name shoud be between 3-20 characters long
        if len(name) < 3 or len(name) > 20:
            errors.append('Name should be between 3-20 characters long')
        # Name should only contain letters, numbers, spaces, and dashes
        if not re.match(r'^[a-zA-Z0-9 -]+$', name):
            errors.append('Name should only contain letters, numbers, spaces, and dashes')
        # Name should start with capital letter
        if not name[0].isupper():
            errors.append('Name should start with capital letter')
        if len(errors) > 0:
            raise InvalidName(errors)