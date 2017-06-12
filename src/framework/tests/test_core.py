
def test_my_view(dbsession):
    """Test case for my_test function."""
    from framework.views.core import my_framework_view

    resp = my_framework_view(dbsession)
    assert resp == 'Value: App value'
