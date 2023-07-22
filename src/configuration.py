import yaml

def load_config():
    with open("./../config.yaml", "rb") as fh:
        config = yaml.safe_load(fh)
        fh.close()

    return config

if __name__ == "__main__":
    print(load_config())