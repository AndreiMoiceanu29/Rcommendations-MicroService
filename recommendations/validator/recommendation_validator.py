""" This module validates the recommendations.

It contains a class with static methods for validating recommendations.
Use this class to validate recommendations before they are stored in the repository.
"""

import re
from service_exceptions import InvalidName
from service_exceptions import InvalidRecommendation

class RecommendationValidator:
    """ Validator Class for Recommendation
        Contains static methods for performing validation on Recommendation objects
    """
    @classmethod
    def validate_recommendation(cls, recommendation):
        """ Validate a recommendation.
        Args:
            recommendation: A recommendation to validate.
        Raises:
            InvalidRecommendation: If the recommendation is invalid.
        """
        errors = {}

        try:
            cls.validate_name(recommendation.title)
        except InvalidName as error:
            errors['name'] = error.message
        if len(errors) > 0:
            raise InvalidRecommendation(errors)

    @classmethod
    def validate_name(cls, name):
        """ Validate a name.
        Args:
            name: A name to validate.
        Raises:
            InvalidName: If the name is invalid.
        """
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
