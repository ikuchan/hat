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

class Greeting(db.Model):
	author = db.StringProperty()
	content = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)

class Task(db.Model):
	client_name = db.StringProperty()
	client_address = db.StringProperty(multiline=True)
	date = db.DateTimeProperty(auto_now_add=True)



class PostHandler(webapp2.RequestHandler):
	def post(self):
		task = Task()
		task.client_name   = self.request.get('client_name')
		task.client_address = self.request.get('client_address')
		task.put()
"""
		tasks = db.GqlQuery("SELECT * FROM Task ORDER BY date DESC LIMIT 10")
		returnDict = {'status':'success'}
		taskDict = {}
		for task in tasks:
			taskDict[task.client_name] = {'client_name': task.client_name,'client_address': task.client_address}

		returnDict['origin']=taskDict

		self.response.out.write(simplejson.dumps(returnDict))
"""
"""
	def get(self):
		self.response.headers['Content-type'] = 'application/json';
		self.response.out.write('<html><body>')
		greetings = db.GqlQuery("SELECT * FROM Greeting ORDER BY date DESC LIMIT 10")
		for greeting in greetings:
			if greeting.author:
				self.response.out.write('<b>%s</b> wrote:' % greeting.author.nickname())
			else:
				self.response.out.write('An anonymous person wrote:')
				self.response.out.write('<blockquote>%s</blockquote>' %
					cgi.escape(greeting.content))

				self.response.out.write("</body></html>")
"""
app = webapp2.WSGIApplication([
    ('/post', PostHandler)
], debug=True)


