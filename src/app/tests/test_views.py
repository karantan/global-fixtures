
def test_my_view(dbsession):
    """Test case for my_test function."""
    from app.views.views import my_view

    resp = my_view(dbsession)
    assert resp == 'Value: App value'
