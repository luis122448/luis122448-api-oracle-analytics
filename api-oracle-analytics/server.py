import uvicorn
import os

# BaseDir
base_dir = os.path.dirname(os.path.realpath(__file__))

# path_ssl_keyfile = os.path.join(base_dir, "certs/key.pem")
# path_ssl_certfile = os.path.join(base_dir, "certs/cert.pem")

if __name__ == '__main__':
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8000,
                reload=True)