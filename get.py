#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
from django.utils import simplejson
from google.appengine.ext import db


class Task(db.Model):
	client_name = db.StringProperty()
	client_address = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)



class PostHandler(webapp2.RequestHandler):
	def get(self):
		tasks = db.GqlQuery("SELECT * FROM Task ORDER BY date DESC")
		taskList = []
		for task in tasks:
			taskList.append({'client_name': task.client_name,'client_address': task.client_address})

		self.response.out.write(simplejson.dumps(taskList))
app = webapp2.WSGIApplication([
    ('/get', PostHandler)
], debug=True)


