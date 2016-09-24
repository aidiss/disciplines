import httmock
import pkg_resources as pres

import disciplines


@httmock.all_requests
def response_content(url, request):
    return pres.resource_string('tests', 'fixtures/results.html')


@httmock.with_httmock(response_content)
def test_download():
    disciplines.download_pages()
