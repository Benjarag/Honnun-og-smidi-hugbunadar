from typing import List

from Validation import Validation
from ValidationFactory import ValidationFactory


class Validator:
    def __init__(self):
        self.validations: List[Validation] = []

    def add_validation(self, validation_type: str, model_obj):
        validation = ValidationFactory.create_validation(validation_type, model_obj)
        self.validations.append(validation)
    
    def validate(self) -> bool:
        return all(validation.validate() for validation in self.validations)
