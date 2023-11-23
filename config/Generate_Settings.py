import json

# Defining initial settings and placeholders
settings = {
    "source": "../../data/WA_Fn-UseC_-HR-Employee-Attrition.csv",
    "feature_types": {"feature_names_categorical": [],
                 "feature_names_continuous": [],
                 "feature_names_ordinal": []
                 },
    "target_feature": None
    }

# Write to a JSON file
with open('./config/Shared_Settings.json', 'w') as file:
    json.dump(settings, file, indent=4)
    
print("Successfully generated JSON settings file.\n")