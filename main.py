import os
import logging
from nifty_cpr.fetch_data import fetch_nifty_data
from nifty_cpr.cpr_calculator import compute_cpr

# Setup logging
os.makedirs("data", exist_ok=True)
logging.basicConfig(
    filename="data/app.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def main():
    logging.info("Starting CPR analysis pipeline...")
    try:
        data = fetch_nifty_data()
        cpr_df = compute_cpr(data)

        output = cpr_df[["High", "Low", "Close", "Pivot", "TC", "BC", "CPR_Width_pct", "CPR_Type"]]
        output.to_csv("data/cpr_output.csv", index=True)
        
        print("Last 10 CPR values:")
        print(output.tail(10))
        logging.info("CPR data successfully saved to CSV.")

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        print("An error occurred. Check app.log for details.")

if __name__ == "__main__":
    main()
