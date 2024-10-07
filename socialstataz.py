import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

def fetch_social_media_stats():
    url = 'https://gs.statcounter.com/social-media-stats/all/azerbaijan'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find the table
        table = soup.find('table', class_='stats-snapshot')
        
        # Get rows from table
        rows = table.find_all('tr')
        
        # A list to store data
        stats_data = []
        
        # Loop through each row and get cells
        for row in rows:
            cols = row.find_all('td')  # find cells
            cols = [col.text.strip() for col in cols]  # Get and clear texts
            if cols:  # If there is data in the cells
                stats_data.append(cols)
        
        return stats_data
    else:
        print(f"Veriler alınamadı, durum kodu: {response.status_code}")
        return None

def filter_and_label_stats(stats_data):
    platforms = ['Instagram', 'Facebook', 'Pinterest', 'YouTube', 'Twitter', 'Reddit']
    filtered_stats = []

    # Skip first line (header)
    for i, stat in enumerate(stats_data[1:], start=0):
        if i < len(platforms):
            # Add platform name in front of rate
            filtered_stats.append([platforms[i], stat[0]])  # Only the first cell containing the rate
        else:
            break  # Make as many loops as the number of platforms

    return filtered_stats

def display_stats_table(labeled_stats):
    # Create the PrettyTable object
    table = PrettyTable()
    table.field_names = ["Platform", "Statistika (%)"]

    # Add data to table
    for stat in labeled_stats:
        table.add_row(stat)

    # Print table
    print(table)


if __name__ == '__main__':
    social_media_stats = fetch_social_media_stats()
    
    if social_media_stats:
        labeled_stats = filter_and_label_stats(social_media_stats)
        
        print("Sosial Media Statistikası:")
        display_stats_table(labeled_stats)
