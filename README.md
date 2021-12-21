# Python pdf report server

This is a report server that is built on top of
flask and weasyprint trough the weasyprint extension
for flask, it is quite trivial to implement something
like this in your flask or django app, but sometimes
when you have your code base in other language where
the alternatives are not quite as good, this kind
of software could be really useful.

## USE

just create a template using flask default conventions for
folders and templating engine, and it would be reachable as a pdf file trough the endpoint
`http POST reports/generate/<report>`

it uses a POST method because the server knows absolutely nothing about your business
logic, its just a way to declare templates and render them as pdf, so the
data to populate the template must be provided by the consumer.
