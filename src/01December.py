import pandas as pd

def calculate_sum_of_differences():
    df = pd.read_csv('./data/input.csv')
    df.columns = df.columns.str.strip()
    df_sorted = df.apply(lambda x: sorted(x))
    df_sorted['distance'] = df_sorted['location2'] - df_sorted['location1']
    df_sorted['distance'] = df_sorted['distance'].abs()
    total_distance = df_sorted['distance'].sum()
    return df_sorted

def calculate_similarity_score():
    df = calculate_sum_of_differences()
    df['occurences'] = df['location1'].apply(lambda x: (df['location2']==x).sum())
    df['similarity_points'] = df['location1']*df['occurences']
    similarity_score = df['similarity_points'].sum()
    print(similarity_score)

calculate_similarity_score()