from flask import Flask, render_template, url_for, request
from flask_weasyprint import HTML, render_pdf
from lib.args import get_args
import sys

args = get_args()

app = Flask(__name__)

def prints(thing):
  print(thing, file=sys.stderr)

@app.route('/generate_report/<report>', methods=["POST"])
def hello_pdf(report):
  data = request.json
  html = render_template(f'{report}.html', data=data)
  res = render_pdf(HTML(string=html))
  pdf_text = res.data
  with open('somefile.pdf', 'wb') as the_file:
    the_file.write(pdf_text)
  return render_pdf(HTML(string=html))

if __name__ == "__main__":
  app.run(host=args.host, port=args.port)
