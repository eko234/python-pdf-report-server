import argparse

def get_args():
  parser = argparse.ArgumentParser(description="parameterize the pdf server")
  parser.add_argument("--host", metavar="H", type=str, help="The host of the server, duh...")
  parser.add_argument("--port", metavar="P", type=str, help="I think you got the point already... don't you?")
  parser.add_argument("--formats_dir", metavar="F", type=str, help="This is the directory where the server will look up for templates or formats to generate reports.")
  args = parser.parse_args()
  return args
