from data_collection import collect_social_media_data

def test_collect_social_media_data():
    # Test collecting tweets with a specific query
    df = collect_social_media_data(query='crisis', count=10)
    assert not df.empty, "DataFrame should not be empty"
    assert 'text' in df.columns, "DataFrame should contain 'text' column"
    assert 'sentiment' in df.columns, "DataFrame should contain 'sentiment' column"

if __name__ == "__main__":
    test_collect_social_media_data()
    print("All tests passed!") 