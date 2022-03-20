from dataclasses import dataclass

from environs import Env


@dataclass
class Config:

    API_KEY : str
    API_URL : str


def load_config(path="weather/services/.env"):
    
    env = Env()
    env.read_env(path)

    return Config(API_KEY=env.str("API_KEY"), API_URL=env.str("API_URL"))
