# Revenue API

## HTTPs API for customer revenues

### Setup the environment

Setup a virtual environment and install necessary packages with requirements.txt

Python requirement: `> Python3.7.5`
`$ pip install -r requirements.txt`

**Note**: Install and create a certificate for HTTPs

- **Windows installation:** `choco install mkcert`
- **macOS/Linux installation:** `brew install mkcert`
- **Create certificate:** `mkcert -key-file key.pem -cert-file cert.pem <example.com>`
- **Install certificate:** `mkcert -install`
- **Windows/Linux compatibility:** `cp` your `rootCA-key.pem` and `rootCA.pem` from Windows mkcert directory to  Linux mkcert directory. `cd ~`. Then, create and install the certificates once again. 

**IP address change:**
Need to assign <name> to the default IP address (127.0.0.1) in `hosts`
- **Windows path:** `C:\\Windows\system32\driver\etc
- **macOS/Linux:** '/etc/'

**Start API on Linux:**
`$ sudo env/bin/uvicorn application:app --port 443 --ssl-keyfile=/home/<username>/key.pem --ssl-certfile=/home/<username>/cert.pem` --reload

**Example curl cmds:**
- No revenue example: `curl -X GET "https://<name>/hourly?branch=352h67i328fh&from=2020-06-20&to=2020-06-22" -H  "accept: application/json"`
- Invalid start/end date format: `curl -X GET "https://<name>/revenue?branch=352h67i328fh&from=2021%2F02%2F04&to=2021%2F02%2F10" -H  "accept: application/json"`
- Different start and end dates for /hourly: `curl -X GET "https://<name>/hourly?branch=352h67i328fh&from=2021-02-04&to=2021-02-05" -H  "accept: application/json"`

**Corresponding url cmds:**
- No revenue example: `https://<name>/revenue?branch=352h67i328fh&from=2021-02-04&to=2021-02-10`
- Invalid start/end date format: `https://<name>/revenue?branch=352h67i328fh&from=2021%2F02%2F04&to=2021%2F02%2F10`
- Different start and end dates for /hourly: `https://<name>/hourly?branch=352h67i328fh&from=2021-02-04&to=2021-02-05`

**Swagger UI**:
- https://<name>/

