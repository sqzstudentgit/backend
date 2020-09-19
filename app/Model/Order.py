from app.Model.Model import Model

class Order(Model):
    def __init__(self, json):
        self.Id = None
        self.keyPurchaseOrderID = None
        self.organizationId = None
        self.keySupplierAccountID = None
        self.supplierOrgId = None
        self.createdDate = None
        self.instructions = None
        self.deliveryOrgName = None
        self.deliveryContact = None
        self.deliveryEmail = None
        self.deliveryAddress1 = None
        self.deliveryAddress2 = None
        self.deliveryAddress3 = None
        self.deliveryRegionName = None
        self.deliveryCountryName = None
        self.deliveryPostcode = None
        self.billingContact = None
        self.billingOrgName = None
        self.billingEmail = None
        self.billingAddress1 = None
        self.billingAddress2 = None
        self.billingAddress3 = None
        self.billingRegionName = None
        self.billingCountryName = None
        self.billingPostcode = None
        self.isDropship = None
        self.lines = None  # store order detail object (From Emmanuel: had to 
        self.session_id = None                         # change this to lines for SQUIZZ API purchase endpoint)
        self.bill_status = None                       
        super().__init__(json)
