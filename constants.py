




NUM_DEPTS = 99
NUM_STORES = 45
NUM_WEEKS = 52
NUM_WEEKS_HISTORICAL = 143

FUTURE_WEEK_MAX = 182
WEEKS_RANGE_FUTURE = range(NUM_WEEKS_HISTORICAL + 1, FUTURE_WEEK_MAX + 1)

# LAST_STORE_DEBUG = 3
STORES_RANGE = range(1, NUM_STORES + 1)
# STORES_RANGE = range(1, LAST_STORE_DEBUG + 1)
DEPTS_RANGE = range(1, NUM_DEPTS + 1)
WEEKS_RANGE = range(1, NUM_WEEKS + 1)

SAMS_PICKLED_DATA_PATH = "pickled_data/"

DATA_PATH = "data/"
DATA_FILE_NAMES = ["stores.csv", "historical_features.csv", "future_features.csv", "train.csv", "test.csv"]