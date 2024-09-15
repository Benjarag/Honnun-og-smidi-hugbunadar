from BuyerHasAgreedToTermsValidation import BuyerHasAgreedToTermsValidation
from MerchantAllowsModificationsValidation import MerchantAllowsModificationsValidation
from OrderIsUnpaidValidation import OrderIsUnpaidValidation
from Validation import Validation


class ValidationFactory:
    @staticmethod
    def create_validation(validation_type: str, model_obj) -> Validation:
        if validation_type == "BuyerHasAgreedToTerms":
            return BuyerHasAgreedToTermsValidation(model_obj)
        elif validation_type == "MerchantAllowsModifications":
            return MerchantAllowsModificationsValidation(model_obj)
        elif validation_type == "OrderIsUnpaid":
            return OrderIsUnpaidValidation(model_obj)
        else:
            raise ValueError("Error, unknown validation type")
