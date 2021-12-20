from bottle import route, run, get, post, request
from lib.args import get_args
from lib.report_generator import ReportGenerator
from lib.template import Template
import os.path
from jinja2 import Template

args = get_args()

if not os.path.isdir(args.formats_dir):
  raise Exception ("""
    Do you think it makes sense to run when I have no formats
    to work with? get your shit together please.
  """)

report_generator = ReportGenerator(
  formats_dir=args.formats_dir,
  template_engine=Template
)

@route('/generate_report/<format>', method="POST")
def generate_report_route(format):
  data = request.json
  if not isinstance(data, list):
    raise Exception("... I need lists to work dude.")
  return report_generator.generate_report(format=format, data=data)

run(host=args.host, port=args.port, debug=True)
