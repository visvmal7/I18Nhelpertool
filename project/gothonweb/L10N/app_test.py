import sys

print sys.executable
print sys.path

from nose.tools import *
# from gothonweb.bin.app import app
from bin.form import app
from tests.tools import assert_response


def test_index():
    # check that we get a 404 on the / URL
    # resp = post_form.request ("/")
    resp = app.request("/")
    print "response of resp %r from tools" % resp
    assert_response(resp, status="404")

    # resp = post_form.request("/item")
    resp = app.request("/item")
    assert_response(resp)

    # resp = post_form.request ("/item", method = "POST")
    resp = app.request("/item", method="POST")
    assert_response(resp, contains="Nobod")

    data = ['Name: zeed', "greet: Hloa"]
    # resp = post_form.request(resp, method = "POST", data=data)
    resp = app.request(resp, method="POST", data=data)
    assert_response(resp, contains="Zed")


if __name__ == "__main__":
    test_index.run()
