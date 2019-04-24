# -*- coding: utf-8 -*-
import os
from openprocurement.planning.api.tests.base import BasePlanWebTest


class BasePlanArchivariusWebTest(BasePlanWebTest):
    relative_to = os.path.dirname(__file__)
