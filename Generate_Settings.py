import json

# Define your settings
settings = {
    "filepaths": {"source": "./data/WA_Fn-UseC_-HR-Employee-Attrition.csv",
                "data_subset_cat": "./data/data_subset_cat.xlsx",
                "data_subset_cont": "./data/data_subset_cont.xlsx",
                "data_subset_ord": "./data/data_subset_ord.xlsx"},
    "column_names": [],
    "target_feature": ["Attrition"]
}

# Write to a JSON file
with open('Shared_Settings.json', 'w') as file:
    json.dump(settings, file, indent=4)