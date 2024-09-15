from Validation import Validation
from models.Merchant import Merchant

class MerchantAllowsModificationsValidation(Validation):
    def __init__(self, merchant: Merchant):
        self.merchant = merchant

    def validate(self) -> bool:
        return self.merchant.allow_modifications
