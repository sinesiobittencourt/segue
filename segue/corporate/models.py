import datetime
from sqlalchemy.sql import functions as func
from ..core import db
from ..json import JsonSerializable
from segue.product.models import Product
from segue.purchase.models import Purchase
from segue.account.models import Account
from segue.errors import WrongBuyerForProduct

from serializers import *

class Corporate(JsonSerializable, db.Model):
    _serializers = [ CorporateJsonSerializer ]
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.Text)
    city         = db.Column(db.Text)
    document     = db.Column(db.Text)
    owner_id     = db.Column(db.Integer, db.ForeignKey('account.id'))
    created      = db.Column(db.DateTime, default=func.now())
    last_updated = db.Column(db.DateTime, onupdate=datetime.datetime.now)

    employees    = db.relationship('CorporateAccount', primaryjoin='and_(Corporate.id==CorporateAccount.corporate_id)')

class CorporateAccount(Account):
    __mapper_args__ = { 'polymorphic_identity': 'employee' }
    # TODO: find some way to reference the object directly: 'ca.corporate = c' and not 'ca.corporate_id = c.id', as it is now.
    corporate_id = db.Column(db.Integer, db.ForeignKey('corporate.id', use_alter=True, name='corporate'), name='cr_corporate_id')

class CorporatePurchase(Purchase):
    __mapper_args__ = { 'polymorphic_identity': 'corporate' }
    corporate_id = db.Column(db.Integer, db.ForeignKey('corporate.id'), name='cr_corporate_id')

class EmployeePurchase(CorporatePurchase):
    __mapper_args__ = { 'polymorphic_identity': 'employee' }

class CorporateProduct(Product):
    __mapper_args__ = { 'polymorphic_identity': 'corporate' }

    def special_purchase_class(self):
        return CorporatePurchase

    def check_eligibility(self, buyer_data):
        if not super(CorporateProduct, self).check_eligibility(buyer_data):
            raise WrongBuyerForProduct()

    def extra_purchase_fields_for(self, buyer_data):
        return { 'corporate_id': buyer_data[u'corporate_id'] }
