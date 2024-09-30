import yaml


class ConfigReader:
    with open("utilites/config_file.yml", "r") as f:
        config = yaml.safe_load(f)["config"]

    def return_value(self, key):
        return self.config.get(key)
