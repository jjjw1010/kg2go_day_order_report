import pandas as pd
import warnings

# Ignore UserWarnings
warnings.filterwarnings("ignore", category=UserWarning)

# Load the data
df = pd.read_csv("data02.csv")

patterns = {
    'Set Menu'  : r'.*(set)',
    'Food' : r'(box|bowl|sweet\sshoyu|tangy\sspicy|tofu)',
    'Spicy Pork': r'spicy\spork',
    'Bulgogi' : r'bulgogi',
    'Noodle' : r'^(?!.*(korean\snoodle|side)).*noodle',
    'Fried Rice' : r'^(?!.*(kimchi|side)).*(fried\srice)',
    'Korean Taco' : r'taco',
    'Crazy Chicken' : r'crazy',
    'Katsu' : r'^(?!.*sauce).*katsu',
    'Kimchi Fried Rice': r'kimchi\sbeef',
    'Sides': r'(ramen|extra|tteokbokki\scup|katsu\ssauce)',
    'Tteokbokki': r'tteokbokki',
    'Kimchi': r'kimchi',
    'Korean Noodle (Side)': r'korean\snoodle',
    'Noodle (Side)': r'noodles\s\(side\)',
    'Yum Yum Sauce': r'yum\syum\ssauce',
    'Dumpling': r'dumpling',
    'Egg Roll': r'egg\sroll',
    'Fried Rice (Side)': r'fried\srice\s\(side\)',
    'Radish': r'radish',
    'Drinks' : r'^(?!.*(milk|fresh|black)).*(tea|ramune|drinks|water)',
    'Snacks' : r'\s*(bungo|seaweed|rollers|custard|chocolate|noi|mongshell|nutella|oh|orion|pocky|ppushu|gummy|homerun)\s*',
    'Boba' : r'(fresh|milk|slush|sparkling|taro\slover|black)',
}

def match_pattern(item, regex):
    return pd.Series(item).str.contains(regex, case=False, na=False).any()

df['Category'] = df['Item Name'].apply(lambda x: 
    next((category for category, pattern in patterns.items() if match_pattern(x, pattern)), 'Unknown'))

# Group by the new category and sum the number of items sold
grouped_df = df.groupby('Category').agg({'# of Items Sold': 'sum'}).reset_index().sort_values(by='# of Items Sold', ascending=False)

# Save to a CSV file
grouped_df.to_csv('data03.csv', index=False)
