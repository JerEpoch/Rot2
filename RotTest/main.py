
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
import codecs, cgi

form = """


  <head>
    <title>Unit 2 Rot 13</title>
  </head>

  <body>
    <h2>Enter some text to ROT13:</h2>

    <form method="post">
      <textarea name="text"
                style="height: 100px; width: 400px;">%(codestr)s</textarea>
      <br>
      <input type="submit">

    </form>
  </body>


"""

def check_escape(s):
    return cgi.escape(s, quote = True)

def ret_encoded(str):
    return str.encode('rot13')


class MainHandler(webapp2.RequestHandler):

    def write_form(self, codestr=""):
        self.response.out.write(form % {"codestr": check_escape(codestr)})




    def get(self):
        #self.response.write(form)
        self.write_form()

    def post(self):
        user_str = self.request.get('text')

        self.write_form(ret_encoded(user_str))

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
