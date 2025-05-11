import pandas as pd
from data_collection import clean_data

def test_clean_data():
    # Sample data for testing
    sample_data = {
        'Text': ['Tweet 1', 'Tweet 2', 'Tweet 1', None],
        'Location': ['Location A', 'Location B', 'Location A', 'Location C'],
        'Date': ['2023-01-01', '2023-01-02', '2023-01-01', None]
    }
    
    df = pd.DataFrame(sample_data)
    cleaned_df = clean_data(df)
    
    # Assertions to validate cleaning
    assert cleaned_df.shape[0] == 2  # Should remove duplicates and NaN
    assert 'text' in cleaned_df.columns  # Check if column names are standardized
    assert pd.to_datetime(cleaned_df['date']).notnull().all()  # Check date conversion

if __name__ == "__main__":
    test_clean_data()
    print("All tests passed!") 