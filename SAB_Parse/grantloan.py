# a very simple object for our GrantLoan XML
class GrantLoan(object):
    """
    A Class to represent a node in the SBA Federal Loan XML
    """
    def __init__(self):
        self.title = None
        self.agency = None
        self.description = None
        self.url_link = None
        self.industry = None
        self.government_type = None
        self.loan_type = None
        self.is_contractor = None
        self.is_development = None
        self.is_disabled = None
        self.is_disaster = None
        self.is_exporting = None
        self.is_general_purpose = None
        self.is_green = None
        self.is_military = None
        self.is_minority = None
        self.is_rural = None
        self.is_woman = None

    def __str__(self):
        return self.title

    # an internal method to generate a Pymongo object
    def generate_mongodbobj(self):
        mongodb_dict = {"title": self.title, "description": self.description, "agency": self.agency,
                        "url": self.url_link, "industry": self.industry, "governmentType": self.government_type,
                        "loanType": self.loan_type}

        if self.is_contractor == '1':
            mongodb_dict["isContractor"] = self.is_contractor
        if self.is_development == '1':
            mongodb_dict["isDevelopment"] = self.is_development
        if self.is_disabled == '1':
            mongodb_dict["isDisabled"] = self.is_disabled
        if self.is_disaster == '1':
            mongodb_dict["isDisaster"] = self.is_disaster
        if self.is_exporting == '1':
            mongodb_dict["isExporting"] = self.is_exporting
        if self.is_general_purpose == '1':
            mongodb_dict["isGeneralPurpose"] = self.is_general_purpose
        if self.is_green == '1':
            mongodb_dict["isGreen"] = self.is_green
        if self.is_military == '1':
            mongodb_dict["isMilitary"] = self.is_military
        if self.is_minority == '1':
            mongodb_dict["isMinority"] = self.is_minority
        if self.is_rural == '1':
            mongodb_dict["isRural"] = self.is_rural
        if self.is_woman == '1':
            mongodb_dict["isWoman"] = self.is_woman

        return mongodb_dict

