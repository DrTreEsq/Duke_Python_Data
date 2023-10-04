from pathlib import Path

import requests
from tqdm import tqdm


def download(url="http://www.ovh.net/files/10Mb.dat", filename='test.dat'):
    # Streaming, so we can iterate over the response.
    response = requests.get(url, stream=True, allow_redirects=True)
    total_size_in_bytes = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)

    # make the parent directory
    try:
        Path(filename).parent.mkdir()
    except FileExistsError:
        pass

    with open(filename, 'wb') as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()
    if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
        print("ERROR, something went wrong")


if __name__ == '__main__':
    download()
