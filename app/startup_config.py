try:
    from .storage import load_config
    from .launcher import open_websites
except ImportError:
    from app.storage import load_config
    from app.launcher import open_websites

def main():
    config = load_config()
    if not config.get("startup_enabled", True):
        return
    
    websites = config.get("websites", [])
    if websites:
        open_websites(websites)

if __name__ == "__main__":
    main()