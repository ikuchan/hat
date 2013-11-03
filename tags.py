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

class TagsHandler(webapp2.RequestHandler):
	def get(self):
		self.response.headers['Content-type'] = 'application/json';
		obj = [
			'tag_test_name1',
			'tag_test_name2',
			'tag_test_name3',
			'tag_test_name4',
			'tag_test_name5',
			'tag_test_name6',
			'tag_test_name7',
			'tag_test_name8',
			'tag_test_name9',
			'tag_test_name10',
			'tag_test_name11',
			'tag_test_name12',
			'tag_test_name13',
			'tag_test_name14',
			'tag_test_name15',
			'tag_test_name16',
			'tag_test_name17',
			'tag_test_name18',
			'tag_test_name19',
			'tag_test_name20',
			'tag_test_name21',
			'tag_test_name22',
		]
		self.response.out.write(simplejson.dumps(obj))

app = webapp2.WSGIApplication([
    ('/tags', TagsHandler)
], debug=True)
