# using sax over the xml.dom library
import xml.sax

# will talk over pymongo at a later date
from pymongo import MongoClient

# Grant Load is our model
from grantloan import GrantLoan

#globals strings for xml
_grant_loan = 'grant_loan'
_title = 'title'
_agency = 'agency'
_description = 'description'
_url = 'url'
_government_type = 'government_type'
_industry = 'industry'
_loan_type = 'loan_type'
_is_contractor = 'is_contractor'
_is_development = 'is_development'
_is_disabled = 'is_disabled'
_is_disaster = 'is_disaster'
_is_exporting = 'is_exporting'
_is_general_purpose = 'is_general_purpose'
_is_green = 'is_green'
_is_military = 'military'
_is_minority = 'is_minority'
_is_rural = 'is_rural'
_is_woman = 'is_woman'
#grantloan class


class LoanParse(xml.sax.ContentHandler):
    """
    a utility class to parse an xml file containing federal loans available for small businesses
    usage: python dbutilsbafedxml /path/to/file
    """
    # instance vars
    MONGO_PORT = 27017
    MONGO_HOST = 'localhost'
    db_client = MongoClient(MONGO_HOST, MONGO_PORT)
    sba_fed_db = db_client.sba_fed
    sba_fed_collection = sba_fed_db.sba_fed
    _current_grant_loan = None
    _current_node = None
    _current_node_contents = ''

    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    # event triggered for every open tag
    def startElement(self, name, attrs):
        self.generateloan('start', name=name)

    # event triggered for every close tag
    def endElement(self, name):
        self.generateloan('end', name=name)
        self._current_node_contents = ''

    def characters(self, content):
        self._current_node_contents += content

    # method to handle parsing nodes
    def generateloan(self, position, name):

        if name == _grant_loan and position == 'start':
            print("starting to parse a node")
            self._current_grant_loan = GrantLoan()
        elif name == _grant_loan and position == 'end':
            # insert
            print("insterting{}".format(self._current_grant_loan.generate_mongodbobj()))
            self.sba_fed_collection.insert(self._current_grant_loan.generate_mongodbobj())

        if name == _title and position == 'start':
            self._current_node = _title
        elif name == _title and position == 'end':
            self._current_grant_loan.title = self._current_node_contents.strip()
            print(self._current_grant_loan.title)

        if name == _agency and position == 'start':
            self._current_node = _agency
        elif name == _agency and position == 'end':
            self._current_grant_loan.agency = self._current_node_contents.strip()
            print(self._current_grant_loan.agency)

        if name == _description and position == 'start':
            self._current_node = _description
        elif name == _description and position == 'end':
            self._current_grant_loan.description = self._current_node_contents.strip()
            print(self._current_grant_loan.description)

        if name == _url and position == 'start':
            self._current_node = _url
        elif name == _url and position == 'end':
            self._current_grant_loan.url_link = self._current_node_contents.strip()
            print(self._current_grant_loan.url_link)

        if name == _government_type and position == 'start':
            self._current_node = _government_type
        elif name == _government_type and position == 'end':
            self._current_grant_loan.government_type = self._current_node_contents.strip()
            print(self._current_grant_loan.government_type)

        if name == _loan_type and position == 'start':
            self._current_node = _loan_type
        elif name == _loan_type and position == 'end':
            self._current_grant_loan.loan_type = self._current_node_contents.strip()
            print(self._current_grant_loan.loan_type)

        if name == _industry and position == 'start':
            self._current_node = _industry
        elif name == _industry and position == 'end':
            self._current_grant_loan.industry = self._current_node_contents.strip()
            print(self._current_grant_loan.industry)

        if name == _is_contractor and position == 'start':
            self._current_node = _is_contractor
        elif name == _is_contractor and position == 'end':
            self._current_grant_loan.is_contractor = self._current_node_contents.strip()
            print(self._current_grant_loan.is_contractor)

        if name == _is_development and position == 'start':
            self._current_node = _is_development
        elif name == _is_development and position == 'end':
            self._current_grant_loan.is_development = self._current_node_contents.strip()
            print(self._current_grant_loan.is_development)

        if name == _is_disabled and position == 'start':
            self._current_node = _is_disabled
        elif name == _is_disabled and position == 'end':
            self._current_grant_loan.is_disabled = self._current_node_contents.strip()
            print(self._current_grant_loan.is_disabled)

        if name == _is_disaster and position == 'start':
            self._current_node = _is_disaster
        elif name == _is_disaster and position == 'end':
            self._current_grant_loan.is_disaster = self._current_node_contents.strip()
            print(self._current_grant_loan.title)

        if name == _is_exporting and position == 'start':
            self._current_node = _is_exporting
        elif name == _is_exporting and position == 'end':
            self._current_grant_loan.is_exporting = self._current_node_contents.strip()
            print(self._current_grant_loan.is_exporting)

        if name == _is_general_purpose and position == 'start':
            self._current_node = _is_general_purpose
        elif name == _is_general_purpose and position == 'end':
            self._current_grant_loan.is_general_purpose = self._current_node_contents.strip()
            print(self._current_grant_loan.is_general_purpose)

        if name == _is_green and position == 'start':
            self._current_node = _is_green
        elif name == _is_green and position == 'end':
            self._current_grant_loan.is_green = self._current_node_contents.strip()
            print(self._current_grant_loan.is_green)

        if name == _is_minority and position == 'start':
            self._current_node = _is_minority
        elif name == _is_minority and position == 'end':
            self._current_grant_loan.is_minority = self._current_node_contents.strip()
            print(self._current_grant_loan.is_minority)

        if name == _is_woman and position == 'start':
            self._current_node = _is_woman
        elif name == _is_woman and position == 'end':
            self._current_grant_loan.is_woman = self._current_node_contents.strip()
            print(self._current_grant_loan.is_woman)

        if name == _is_rural and position == 'start':
            self._current_node = _is_rural
        elif name == _is_rural and position == 'end':
            self._current_grant_loan.is_rural = self._current_node_contents.strip()
            print(self._current_grant_loan.is_rural)
