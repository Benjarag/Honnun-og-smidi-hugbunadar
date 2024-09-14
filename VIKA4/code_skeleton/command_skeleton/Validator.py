

from typing import List

from Validation import Validation


class Validator:
    def __init__(self):
        self.validations: List[Validation] = []

    def add_validation(self, validation: Validation):
        self.validations.append(validation)
    
    def validate(self) -> bool:
        return all(validation.validate() for validation in self.validations)
        # for validation in self.validations:
        #     if not validation.validate():
        #         return False
        #     return True
    
