import pandas as pd

def extract_feature_values(data):
    """ Given a params dict, return the values for feeding into a model"""
    
    # Replace these features with the features for your model. They need to 
    # correspond with the `name` attributes of the <input> tags
    EXPECTED_FEATURES = [
        "game_minutes_remaining",
        "half_minutes_remaining",
        "quarter_minutes_remaining",
        "qtr",
        "down",
        "drive",
        "posteam_score",
        "defteam_score",
        "score_differential",
        "yardline_100",
        "goal_to_go",
        "ydstogo",
        "posteam_timeouts_remaining",
        "defteam_timeouts_remaining",
        "shotgun",
        "no_huddle",
        "wp"
    ]

    # This assumes all inputs will be numeric. If you have categorical features
    # that the user enters as a string, you'll want to rewrite this as a for
    # loop that treats different features differently
    values = [[float(data[feature]) for feature in EXPECTED_FEATURES]]
    return pd.DataFrame(values, columns=EXPECTED_FEATURES)