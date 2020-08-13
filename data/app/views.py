import datetime
import logging
from flask import redirect
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi
from . import appbuilder, db
from .models import AcmaOptusFixedRanges, Xbtpassembly, Xbtpitn, Xbtpne, Xbtpitnlnsvc, Xbtpregion, Xbtpsite
from flask_appbuilder.actions import action

class AcmaOptusFixedRangesView(ModelView):
    datamodel = SQLAInterface(AcmaOptusFixedRanges)

    list_columns = ["start_range", "end_range", "quantity", "allocatee", "charge_zone"]

    base_order = ("start_range", "asc")
    show_fieldsets = [
        ("Summary", {"fields": ["start_range", "end_range"]}),
        (
            "Extra Info",
            {
                "fields": [
                    "quantity",
                    "allocatee",
                    "charge_zone",
                ],
                "expanded": True,
            },
        ),
    ]

    add_fieldsets = [
        ("Summary", {"fields": ["start_range", "end_range"]}),
        (
            "Extra Info",
            {
                "fields": [
                    "quantity",
                    "allocatee",
                    "charge_zone",
                ],
                "expanded": True,
            },
        ),
    ]

    edit_fieldsets = [
        ("Summary", {"fields": ["start_range", "end_range"]}),
        (
            "Extra Info",
            {
                "fields": [
                    "quantity",
                    "allocatee",
                    "charge_zone",
                ],
                "expanded": True,
            },
        ),
    ]

class XbtpitnView(ModelView):
    datamodel = SQLAInterface(Xbtpitn)

    @action("reserve", "Reserve", "Please confirm, reserve phone number?", "fa-hand-rock-o")
    def	reserve(self, items):
        logging.info("KORE Reserve Print action")
        if isinstance(items, list):
            for item in items:
                logging.info("KORE item:")
                logging.info(item.__class__())
                logging.info(item.objectid)
                logging.info(item.subtype)
                logging.info(item.status)
                item.status = "AS"
                item.availabilityind = "N"
                item.changetime = datetime.datetime.now()
                item.changeempid = "Kostya POC"
                self.datamodel.edit(item)
                self.update_redirect()
        else:
            logging.info("KORE single item:")
            logging.info(items.__class__())
            logging.info(items.objectid)
            logging.info(items.subtype)
            logging.info(items.status)
            items.status = "AS"
            items.availabilityind = "N"
            items.changetime = datetime.datetime.now()
            items.changeempid = "Kostya POC"
            self.datamodel.edit(items)
            self.update_redirect()
        return redirect(self.get_redirect())

    @action("release", "Release", "Please confirm, Release phone number?", "fa-chain-broken")
    def	release(self, items):
        logging.info("KORE Print release action")
        if isinstance(items, list):
            for item in items:
                logging.info("KORE item:")
                logging.info(item.__class__())
                logging.info(item.objectid)
                logging.info(item.subtype)
                logging.info(item.status)
                item.status = "AV"
                item.availabilityind = "Y"
                item.changetime = datetime.datetime.now()
                item.changeempid = "Kostya POC"
                self.datamodel.edit(item)
                self.update_redirect()
        else:
            logging.info("KORE single item:")
            logging.info(items.__class__())
            logging.info(items.objectid)
            logging.info(items.subtype)
            logging.info(items.status)
            items.status = "AV"
            items.availabilityind = "Y"
            items.changetime = datetime.datetime.now()
            items.changeempid = "Kostya POC"
            self.datamodel.edit(items)
            self.update_redirect()
        return redirect(self.get_redirect())

    list_columns = ["objectid", "subtype",  "status",	"identifier",	"prefix",	"localnumber",	"onekblock",	"changereqid",	"changeempid",	"changetime",	"svccategory",	"assemblycount"]
    #list_columns = ["objectid",	"identifier",	"prefix",	"localnumber",	"subtype",	"onekblock",	"changereqid",	"changeempid",	"changetime",	"svccategory",	"assemblycount",	"status"]

    #base_order = ("objectid", "asc")
    show_fieldsets = [
        ("Summary", {"fields": ["objectid",	"identifier",	"prefix",	"localnumber",	"subtype",	"vanityclass",	"onekblock",	"changereqid",	"changeempid",	"changetime",	"displayind"]}),
        (
            "Extra Info",
            {
                "fields": ["displayempid",	"displaytime",	"availabilityind",	"svcasgncount",	"workingcount",	"listcount",	"agingind",	"exclusioncode",	"svccategory",	"clecind",	"releasedate",	"analogind",	"pooledcode",	"assemblycount",	"status",	"derivedstatus",	"owningoperator",	"owningserviceprovider",	"assignedoperator",	"assignedserviceprovider",	"reseller",	"reverttosvccategory"],
                "expanded": True,
            },
        ),
    ]

    add_fieldsets = [
        ("Summary", {"fields": ["objectid",	"identifier",	"prefix",	"localnumber",	"subtype",	"vanityclass",	"onekblock",	"changereqid",	"changeempid",	"changetime",	"displayind"]}),
        (
            "Extra Info",
            {
                "fields": ["displayempid",	"displaytime",	"availabilityind",	"svcasgncount",	"workingcount",	"listcount",	"agingind",	"exclusioncode",	"svccategory",	"clecind",	"releasedate",	"analogind",	"pooledcode",	"assemblycount",	"status",	"derivedstatus",	"owningoperator",	"owningserviceprovider",	"assignedoperator",	"assignedserviceprovider",	"reseller",	"reverttosvccategory"],
                "expanded": True,
            },
        ),
    ]

    edit_fieldsets = [
        ("Summary", {"fields": ["objectid",	"identifier",	"prefix",	"localnumber",	"subtype",	"vanityclass",	"onekblock",	"changereqid",	"changeempid",	"changetime",	"displayind"]}),
        (
            "Extra Info",
            {
                "fields": ["displayempid",	"displaytime",	"availabilityind",	"svcasgncount",	"workingcount",	"listcount",	"agingind",	"exclusioncode",	"svccategory",	"clecind",	"releasedate",	"analogind",	"pooledcode",	"assemblycount",	"status",	"derivedstatus",	"owningoperator",	"owningserviceprovider",	"assignedoperator",	"assignedserviceprovider",	"reseller",	"reverttosvccategory"],
                "expanded": True,
            },
        ),
    ]

class XbtpassemblyView(ModelView):
    datamodel = SQLAInterface(Xbtpassembly)

    list_columns = ["objectid","assemblytype","assemblyowner","creationtime","creationempid","changetime","changeempid","assemblyoperator","serviceprovider","assemblyid"]

    base_order = ("objectid", "asc")
    show_fieldsets = [
        ("Summary", {"fields": ["objectid","assemblytype","assemblyowner","creationtime","creationempid"]}),
        (
            "Extra Info",
            {
                "fields": ["changetime","changeempid","assemblyoperator","serviceprovider","assemblyid"],
                "expanded": True,
            },
        ),
    ]

    add_fieldsets = [
        ("Summary", {"fields": ["objectid","assemblytype","assemblyowner","creationtime","creationempid"]}),
        (
            "Extra Info",
            {
                "fields": ["changetime","changeempid","assemblyoperator","serviceprovider","assemblyid"],
                "expanded": True,
            },
        ),
    ]

    edit_fieldsets = [
        ("Summary", {"fields": ["objectid","assemblytype","assemblyowner","creationtime","creationempid"]}),
        (
            "Extra Info",
            {
                "fields": ["changetime","changeempid","assemblyoperator","serviceprovider","assemblyid"],
                "expanded": True,
            },
        ),
    ]	

class XbtpneView(ModelView):
    datamodel = SQLAInterface(Xbtpne)

    list_columns = [x.key for x in Xbtpne.__table__.columns]

    #base_order = ("objectid", "asc")
    show_fieldsets = [
        ("All", {"fields": [x.key for x in Xbtpne.__table__.columns]})
    ]

    add_fieldsets = [
        ("All", {"fields": [x.key for x in Xbtpne.__table__.columns]})
    ]

    edit_fieldsets = [
        ("All", {"fields": [x.key for x in Xbtpne.__table__.columns]})
    ]	

class XbtpitnlnsvcView(ModelView):
    datamodel = SQLAInterface(Xbtpitnlnsvc)

    list_columns = [x.key for x in Xbtpitnlnsvc.__table__.columns]

    #base_order = ("objectid", "asc")
    show_fieldsets = [
        ("All", {"fields": [x.key for x in Xbtpitnlnsvc.__table__.columns]})
    ]

    add_fieldsets = [
        ("All", {"fields": [x.key for x in Xbtpitnlnsvc.__table__.columns]})
    ]

    edit_fieldsets = [
        ("All", {"fields": [x.key for x in Xbtpitnlnsvc.__table__.columns]})
    ]	


"""
    Application wide 404 error handler
"""


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
appbuilder.add_view(
    AcmaOptusFixedRangesView,
    "ACMA Optus Fixed Ranges",
    icon="fa-folder-open-o",
    category="Menu",
    category_icon="fa-envelope",
)
appbuilder.add_view(
    XbtpitnView,
    "Phone Numbers list",
    icon="fa-folder-open-o",
    category="Menu",
    category_icon="fa-envelope",
)
appbuilder.add_view(
    XbtpassemblyView,
    "Assembly",
    icon="fa-folder-open-o",
    category="Menu",
    category_icon="fa-envelope",
)
appbuilder.add_view(
    XbtpneView,
    "Phone Number E",
    icon="fa-folder-open-o",
    category="Menu",
    category_icon="fa-envelope",
)
appbuilder.add_view(
    XbtpitnlnsvcView,
    "Number IDs",
    icon="fa-folder-open-o",
    category="Menu",
    category_icon="fa-envelope",
)