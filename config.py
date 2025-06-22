# Base URL for Divar website
BASE_URL = "https://divar.ir"

# URL for residential properties in Tehran (buy section)
SEARCH_URL = "https://divar.ir/s/tehran/buy-apartment"

# --- Main Configuration ---

# Target number of ads to scrape
TARGET_AD_COUNT = 10000

# NEW: The number of links to collect in each cycle before starting to scrape them.
# This is the batch-based approach you suggested.
LINK_COLLECTION_BATCH_SIZE = 100

# Name of the CSV file to save the scraped data
CSV_FILE = "divar_tehran_houses.csv"

# File to store visited ad links to prevent duplicates across multiple runs
VISITED_LINKS_FILE = "visited_links.txt"

# --- Timing and Behavior ---

# Minimum and maximum random sleep time between actions (in seconds)
# Helps to mimic human behavior and avoid getting blocked.
MIN_SLEEP_TIME = 4.0
MAX_SLEEP_TIME = 7.0

# Number of ads to scrape before saving to CSV in a batch
# Prevents data loss in case of unexpected crashes.
BATCH_SAVE_SIZE = 10

# Maximum number of times to retry initializing the driver in case of a major crash
MAX_DRIVER_RETRIES = 5

# Time to wait (in seconds) for elements to be visible or clickable
WAIT_TIMEOUT = 15

# Number of scroll attempts before looking for a 'Load More' button in each cycle
SCROLL_ATTEMPTS_PER_CYCLE = 5

# If no new unique ads are found for this many consecutive cycles, stop the link collection phase.
NO_NEW_ADS_BREAK_THRESHOLD = 5

# Timeout for full page load (in seconds) before considering it an error
PAGE_LOAD_TIMEOUT = 45
