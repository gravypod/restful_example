# restful-example

A really basic example of one interpretation of a JSON/REST API. I am 
using this for testing something that needs to talk to a REST API.


# Configuration

- `ADDRESS`: What to bind for serving. (Defaults to '0.0.0.0')
- `PORT`: Port to bind for serving. (Defaults to '80')


# Endpoints

- Create Thing (`POST /things`)
- Get Thing (`GET /things/{id}`)
- Exists Thing (`HEAD /things/{id}`)
- Update Thing (`PUT /things/{id}`)
- Delete Thing (`DELETE /things/{id}`)
- Health Check (`GET /healthz`)
- Ready Check (`GET /readyz`)
