from core.config import INPUT_FILE, OUTPUT_FILDER
from logging import log

def main():
    print("this is entry point")
    with open(INPUT_FILE, "r") as f, open(OUTPUT_FILDER + "_output.csv", "w", newline="") as csvfile:
        for unclean_domain in list:
            unclean_domain = unclean_domain.strip()


if __name__ == "__main__":
    main()