from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

PRODUCTS = (
    ('NBU', 'NetBackup'),
    ('OPC', 'OpsCenter'),
)

# OST-Vendors

APPLICATION = (
    ('RD', 'Replication Director'),
    ('NDMP', 'Legacy NDMP'),
    ('SNC', 'Snapshot Client'),
    ('CLOUD', 'Cloud'),
    ('OSTV', 'OST-Vendors'),
)

VERSIONS = (
    ('773', '7.7.3'),
    ('772', '7.7.2'),
    ('771', '7.7.1'),
    ('77', '7.7'),
    ('7612', '7.6.1.2'),
    ('7604', '7.6.0.4'),
    ('7507', '7.5.0.7'),
)


class Line(models.Model):
    text = models.CharField(max_length=255)


class TokenNumberNew(models.Model):
    tok_number = models.PositiveIntegerField(primary_key=True, blank=True, default=1)


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class NBUList(models.Model):
    product = models.CharField(max_length=255)
    # product = models.CharField(max_length=3, choices=PRODUCTS)
    appname = models.CharField(max_length=255)
    # appname = models.CharField(max_length=3, choices=APPLICATION)
    version_num = models.CharField(max_length=255)
    storage_name = models.CharField(max_length=255)
    protocol_name = models.CharField(max_length=255)

    def __str__(self):
        return self.product


class RDProtocol(models.Model):
    NAS = 'NAS'
    SAN = 'SAN'
    # protocol_standard = models.CharField(max_length= 10)
    protocol_standard_choices = (
        (NAS, 'NAS'),
        (SAN, 'SAN')
    )
    protocol_standard = models.CharField(max_length=10, choices=protocol_standard_choices)

    NFS = 'NFS'
    CIFS = 'CIFS'
    NDMP = 'NDMP'
    ISCSI = 'ISCSI'
    FC = 'FC'
    protocol_name_choices = (
        (NFS, 'NFS'),
        (CIFS, 'CIFS'),
        (NDMP, 'NDMP'),
        (ISCSI, 'iSCSI'),
        (FC, 'FC'),

    )
    protocolname = models.CharField(primary_key=True, max_length=15, choices=protocol_name_choices)

    def __unicode__(self):
        return self.protocol_standard + '-' + self.protocolname


class RD(models.Model):
    Yes = 'Supported'
    No = 'Not Supported'
    NA = 'Not Applicable'

    value_choices = (
        (Yes, 'Supported'),
        (No, 'Not Supported'),
        (NA, 'Not Applicable')
    )
    SMode = 'NetApp 7-Mode'
    CMode = 'NetApp C-Mode'
    Vnx = 'EMC-VNX'

    storage_choices = (
        (SMode, 'NetApp 7-Mode'),
        (CMode, 'NetApp C-Mode'),
        (Vnx, 'EMC-VNX')
    )
    v1 = '7.5.0.7'
    v2 = '7.6.0.4'
    v3 = '7.6.1.2'
    v4 = '7.7.1'
    v5 = '7.7.2'

    version_choices = (
        (v1, '7.5.0.7'),
        (v2, '7.6.0.4'),
        (v3, '7.6.1.2'),
        (v4, '7.7.1'),
        (v5, '7.7.2')
    )

    storage = models.CharField(max_length=20, choices=storage_choices)
    version = models.CharField(max_length=10, choices=version_choices)
    rdprotocol = models.ForeignKey(RDProtocol, default='NAS')
    snapshot = models.CharField(max_length=20, choices=value_choices)
    replication = models.CharField(max_length=20, choices=value_choices)
    liveBrowse = models.CharField(max_length=20, choices=value_choices)
    index = models.CharField(max_length=20, choices=value_choices)
    PIT_Rollback = models.CharField(max_length=20, choices=value_choices)
    SFR = models.CharField(max_length=20, choices=value_choices)
    dataMover = models.CharField(max_length=20, choices=value_choices)

    def __unicode__(self):
        return self.storage + ' - ' + self.version


# -----------Trial model----------------------------------------------------
class VehicleBrand(models.Model):
    description = models.CharField(max_length=100)
    code = models.SlugField(primary_key=True)

    def __unicode__(self):
        return self.description


class VehicleModel(models.Model):
    description = models.CharField(max_length=100)
    code = models.SlugField(primary_key=True)
    brand = models.ForeignKey(VehicleBrand)


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

# Db structure to uplo
class NbuModel(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    #browse = models.FileField()
