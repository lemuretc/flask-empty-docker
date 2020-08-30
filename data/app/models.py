from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import datetime
from sqlalchemy import CheckConstraint, Column, DateTime, Float, ForeignKey, Index, Numeric, SmallInteger, String, \
    UniqueConstraint
from sqlalchemy.schema import FetchedValue
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class AcmaOptusFixedRanges(Model):
    __tablename__ = "acma_optus_fixed_ranges"
    ctid = db.Column(String, primary_key=True)
    start_range = db.Column(String(10))
    end_range = db.Column(String(10))
    quantity = db.Column(String(10))
    allocatee = db.Column(String(100))
    charge_zone = db.Column(String(100))


class Xbtpassembly(db.Model):
    __tablename__ = 'xbtpassembly'
    __table_args__ = {'schema': 'public'}

    objectid = db.Column(db.Numeric(38, 0), primary_key=True)
    assemblytype = db.Column(db.String(5), nullable=False)
    assemblyowner = db.Column(db.String(100))
    creationtime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    creationempid = db.Column(db.String(15), nullable=False)
    changetime = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue())
    changeempid = db.Column(db.String(15), nullable=False)
    assemblyoperator = db.Column(db.String(20))
    serviceprovider = db.Column(db.String(20))
    assemblyid = db.Column(db.String(14), nullable=False, index=True)


class Xbtpitn(db.Model):
    __tablename__ = 'xbtpitn'
    __table_args__ = (
        db.CheckConstraint(
            "(pooledcode)::text = ANY ((ARRAY['I'::character varying, 'O'::character varying])::text[])"),
        db.UniqueConstraint('identifier', 'subtype'),
        db.UniqueConstraint('prefix', 'localnumber', 'subtype'),
        db.Index('ak_itn', 'identifier', 'subtype'),
        db.Index('ak_itn_pls', 'prefix', 'localnumber', 'subtype'),
        {'schema': 'public'}
    )

    objectid = db.Column(db.Numeric(38, 0), primary_key=True)
    identifier = db.Column(db.String(320), nullable=False)
    prefix = db.Column(db.String(320), nullable=False)
    localnumber = db.Column(db.Float(53), nullable=False)
    subtype = db.Column(db.String(6))
    vanityclass = db.Column(db.SmallInteger, nullable=False)
    onekblock = db.Column(db.Float(53), nullable=False)
    changereqid = db.Column(db.String(15), nullable=False)
    changeempid = db.Column(db.String(15), nullable=False)
    changetime = db.Column(db.DateTime, nullable=False)
    displayind = db.Column(db.String(1), nullable=False)
    displayempid = db.Column(db.String(15))
    displaytime = db.Column(db.DateTime)
    availabilityind = db.Column(db.String(1), nullable=False)
    svcasgncount = db.Column(db.SmallInteger, nullable=False)
    workingcount = db.Column(db.SmallInteger, nullable=False)
    listcount = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    agingind = db.Column(db.String(1), nullable=False)
    exclusioncode = db.Column(db.String(4))
    svccategory = db.Column(db.String(5), nullable=False)
    clecind = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    releasedate = db.Column(db.DateTime)
    analogind = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    pooledcode = db.Column(db.String(1))
    assemblycount = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    status = db.Column(db.String(5))
    derivedstatus = db.Column(db.String(15))
    owningoperator = db.Column(db.String(20))
    owningserviceprovider = db.Column(db.String(20))
    assignedoperator = db.Column(db.String(20))
    assignedserviceprovider = db.Column(db.String(20))
    reseller = db.Column(db.String(20))
    reverttosvccategory = db.Column(db.String(5))


class Xbtpne(db.Model):
    __tablename__ = 'xbtpne'
    __table_args__ = (
        db.CheckConstraint(
            "(autocancelind)::text = ANY ((ARRAY['Y'::character varying, 'N'::character varying])::text[])"),
        db.CheckConstraint(
            "(interceptmsgind)::text = ANY ((ARRAY['Y'::character varying, 'N'::character varying])::text[])"),
        db.CheckConstraint(
            "(removeportind)::text = ANY ((ARRAY['Y'::character varying, 'N'::character varying])::text[])"),
        db.Index('ie_ne', 'siteoid', 'nealtid'),
        {'schema': 'public'}
    )

    objectid = db.Column(db.Numeric(38, 0), primary_key=True)
    neid = db.Column(db.String(100), nullable=False, unique=True)
    siteoid = db.Column(db.ForeignKey('public.xbtpsite.objectid'), nullable=False)
    parent = db.Column(db.Numeric(38, 0))
    ipaddress = db.Column(db.String(50))
    autoreleaseind = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    autocancelind = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    interceptmsgind = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    removeportind = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    nealtid = db.Column(db.String(20))
    netype = db.Column(db.String(6))
    exchangekey = db.Column(db.String(100), index=True)
    mfgrcode = db.Column(db.String(10))
    equipmenttype = db.Column(db.String(6))
    swgenericcode = db.Column(db.String(6))
    restrictioncode = db.Column(db.String(4))
    restrictionstart = db.Column(db.DateTime)
    restrictionend = db.Column(db.DateTime)
    hostexchangekey = db.Column(db.String(100), index=True)
    customername = db.Column(db.String(50))
    customertype = db.Column(db.String(10))
    maintmode = db.Column(db.String(1), index=True)
    remark = db.Column(db.String(200))

    # xbtpsite = db.relationship('Xbtpsite', primaryjoin='Xbtpne.siteoid == Xbtpsite.objectid', backref='xbtpnes')


class Xbtpitnlnsvc(db.Model):
    __tablename__ = 'xbtpitnlnsvc'
    __table_args__ = (
        db.CheckConstraint(
            "(extendasgn)::text = ANY ((ARRAY['Y'::character varying, 'N'::character varying])::text[])"),
        db.CheckConstraint(
            "(pendingcode)::text = ANY ((ARRAY['I'::character varying, 'O'::character varying])::text[])"),
        db.CheckConstraint(
            "(portedcode)::text = ANY ((ARRAY['I'::character varying, 'E'::character varying, 'L'::character varying, 'Y'::character varying])::text[])"),
        db.CheckConstraint(
            "(svcorderbuilt)::text = ANY ((ARRAY['Y'::character varying, 'N'::character varying])::text[])"),
        {'schema': 'public'}
    )

    objectid = db.Column(db.Numeric(38, 0), primary_key=True)
    numberoid = db.Column(db.ForeignKey('public.xbtpitn.objectid'), nullable=False, index=True)
    extendasgn = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())
    custid = db.Column(db.String(100))
    custordnum = db.Column(db.String(22))
    svcreqnum = db.Column(db.String(12))
    duedate = db.Column(db.DateTime)
    svcclass = db.Column(db.String(5))
    svctype = db.Column(db.String(1))
    svcusage = db.Column(db.String(30))
    nonpublished = db.Column(db.String(1))
    direction = db.Column(db.String(1))
    activitytype = db.Column(db.String(1))
    activitynum = db.Column(db.String(19))
    pendingcode = db.Column(db.String(1))
    pendingcount = db.Column(db.SmallInteger, nullable=False, server_default=db.FetchedValue())
    workingne = db.Column(db.ForeignKey('public.xbtpne.objectid'), index=True)
    portedcode = db.Column(db.String(1), index=True)
    assigndate = db.Column(db.DateTime)
    carrierid = db.Column(db.String(14))
    workingregion = db.Column(db.ForeignKey('public.xbtpregion.objectid'))
    svcorderbuilt = db.Column(db.String(1), nullable=False, server_default=db.FetchedValue())

    # xbtpitn = db.relationship('Xbtpitn', primaryjoin='Xbtpitnlnsvc.numberoid == Xbtpitn.objectid', backref='xbtpitnlnsvcs')
    # xbtpne = db.relationship('Xbtpne', primaryjoin='Xbtpitnlnsvc.workingne == Xbtpne.objectid', backref='xbtpitnlnsvcs')
    # xbtpregion = db.relationship('Xbtpregion', primaryjoin='Xbtpitnlnsvc.workingregion == Xbtpregion.objectid', backref='xbtpitnlnsvcs')


class Xbtpregion(db.Model):
    __tablename__ = 'xbtpregion'
    __table_args__ = (
        db.UniqueConstraint('regiontype', 'regionid', 'statecountrycode'),
        db.Index('ak_region', 'regiontype', 'regionid', 'statecountrycode'),
        {'schema': 'public'}
    )

    objectid = db.Column(db.Numeric(38, 0), primary_key=True)
    regiontype = db.Column(db.String(15), nullable=False)
    regionid = db.Column(db.String(15), nullable=False)
    statecountrycode = db.Column(db.String(6))
    regionfullname = db.Column(db.String(50))
    remark = db.Column(db.String(200))


class Xbtpsite(db.Model):
    __tablename__ = 'xbtpsite'
    __table_args__ = {'schema': 'public'}

    objectid = db.Column(db.Numeric(38, 0), primary_key=True)
    siteid = db.Column(db.String(100), nullable=False, unique=True)
    provisioningname = db.Column(db.String(6))
    sitename = db.Column(db.String(20), unique=True)
    sitetype = db.Column(db.String(6))
    customername = db.Column(db.String(50))
    customertype = db.Column(db.String(10))
    maintmode = db.Column(db.String(1), index=True)
