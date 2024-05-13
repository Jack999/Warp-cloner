from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)

class Settings(BaseSettings):
    model_config =  SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    BASE_KEYS: list[str] = Field(
        validation_alias='BASE_KEYS',
        default=[
            'c0XD27y5-5Zb918sJ-o8A7b6M5',
            'KF37P92V-4y5BF78L-mL38l5j7',
            '0Tps6J83-ED314Qo8-mjY0B657',
            '4ph7Nb80-bz165ON3-C40If5z8',
            '4S3e91Ym-8Pd6wc93-X98OM6z3',
            'DQ1407Zn-Lg92v47l-5tf70Mo8',
            'J31bFT04-iUg2n349-JGa8T435',
            '59F70AHg-7yJ91iW5-306N8BzE',
            'a81g6PC2-1oZ437We-9ci57E2A',
            '01N6l5Gs-3br972Op-n76bqT32',
        ]
    )
    THREADS_COUNT: int = Field(validation_alias='THREADS_COUNT', default=1)
    PROXY_FILE: str | None = Field(validation_alias='PROXY_FILE', default=None)
    DEVICE_MODELS: list[str] = Field(validation_alias='DEVICE_MODELS', default=[])
    SAVE_WIREGUARD_VARIABLES: bool = Field(validation_alias='SAVE_WIREGUARD_VARIABLES', default=False)
    DELAY: int = Field(validation_alias='DELAY', default=120)
    OUTPUT_FILE: str = Field(validation_alias='OUTPUT_FILE', default='output.txt')
    OUTPUT_FORMAT: str = Field(validation_alias='OUTPUT_FORMAT', default='{key} | {referral_count} GB')
    RETRY_COUNT: int = Field(validation_alias='RETRY_COUNT', default=3)


config = Settings()
