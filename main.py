from bottle import route, run, get, post, request
from lib.args import get_args
from lib.report_generator import ReportGenerator

args = get_args()
report_generator = ReportGenerator(formats_dir=args.formats_dir)

@route('/generate_report/<format>', method="POST")
def generate_report_route(format):
  data = request.json
  return report_generator.generate_report(format=format, data=data)

run(host=args.host, port=args.port, debug=True)
