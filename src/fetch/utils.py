import requests
from typing import TextIO, Text, Optional


def download_file(url: TextIO, output: Text) -> Optional[Text]:
    try:
        # NOTE the stream=True parameter
        with requests.get(url, stream=True, verify=False) as r:
            r.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
            with open(output, "wb") as f:
                f.write(r.content)
                f.close()
            r.close()
        return output
    except requests.exceptions.RequestException as _:
        return None
