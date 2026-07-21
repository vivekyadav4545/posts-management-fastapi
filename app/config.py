from pydantic_settings import BaseSettings, SettingsConfigDict

# this pydantic model verifiy the setting of environmental variables

class Setting(BaseSettings):
    database_hostname : str
    database_port :str
    database_password :str
    database_name :str
    database_username : str
    secret_key :str
    algorithm :str
    access_token_expire_minutes : int

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=False
    )


settings = Setting()
