import disciplines


def test_read_downloaded_pages(path):
    pages = disciplines.read_downloaded_pages(None)
    assert len(pages) == 16


def test_get_methods():
    # lists all possible methods
    disciplines.get_methods(None)


def test_get_resources():
    # list all available resources
    discipline.g


def test_venn_disciplines():
    venned_disciplines = discipline.test_venn_disciplines(a, b, get_extra=None)
    assert isinstance(a, Publication)
    assert isinstance(b, Publication)
    venned_disciplines = discipline.test_venn_disciplines(a, b, get_extra=True)
    assert isinstance(a, Publication)
    assert isinstance(b, Publication)
    venned_disciplines = discipline.test_venn_disciplines(a, b, get_extra=True)
    assert isinstance(a, Publication)
    assert isinstance(b, Publication)


def test_venned_publications():
    a, b = Publication(), Publication()
    venned_publications = discipline.test_venn_publications(a, b, get_extra=None)
    assert isinstance(a, Publication)
    assert isinstance(b, Publication)
    venned_publications = discipline.test_venn_publications(a, b, get_extra=True)
    assert isinstance(a, Publication)
    assert isinstance(b, Publication)
    venned_publications = discipline.test_venn_publications(a, b, get_extra=True)
    assert isinstance(a, Publication)
    assert isinstance(b, Publication)


def test_venn_classes(a, b)
    assert isinstance(a, Class)
    discipline.g
