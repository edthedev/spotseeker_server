""" Copyright 2012, 2013 UW Information Technology, University of Washington

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from spotseeker_server.views.rest_dispatch import RESTDispatch
from spotseeker_server.forms.spot import SpotForm
from spotseeker_server.models import *
from django.http import HttpResponse
from spotseeker_server.require_auth import *
import simplejson as json


class AllSpotsView(RESTDispatch):

    @app_auth_required
    def GET(self, request):
        spots = Spot.objects.all()
        response = []
        for spot in spots:
            response.append(spot.json_data_structure())
        return HttpResponse(response)
