# BuyerHasAgreedToTermsValidation.py
from Validation import Validation
from models.Buyer import Buyer

class BuyerHasAgreedToTermsValidation(Validation):
    def __init__(self, buyer: Buyer):
        self.buyer = buyer

    def validate(self) -> bool:
        return self.buyer.has_agreed_to_terms
