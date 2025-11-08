import datetime
from pathlib import Path
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import rsa


main_folder = Path(__file__).parent
cerificate_folder = main_folder / "Certificates"
mitm_ca = cerificate_folder / "mitmproxy-ca.pem"
roblox_ca = cerificate_folder / "ca-cert.pem"


def generate_ca_files():
    
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    subject = issuer = x509.Name([x509.NameAttribute(NameOID.COMMON_NAME, "ProxyRBX"),])

    cert_builder = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(private_key.public_key())
        .serial_number(x509.random_serial_number())
        .not_valid_before(datetime.datetime.now(datetime.timezone.utc))
        .not_valid_after(datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(days=1095))
        .add_extension(x509.BasicConstraints(ca=True, path_length=None), critical=True)
        .add_extension(
            x509.KeyUsage(
                digital_signature=False,
                content_commitment=False,
                key_encipherment=False,
                data_encipherment=False,
                key_agreement=False,
                key_cert_sign=True,
                crl_sign=False,
                encipher_only=False,
                decipher_only=False
            ), critical=True
        )
    )

    certificate = cert_builder.sign(private_key, hashes.SHA256())
    cerificate_folder.mkdir(exist_ok=True)

    with open(mitm_ca, 'wb') as f:
        f.write(private_key.private_bytes(encoding=serialization.Encoding.PEM, format=serialization.PrivateFormat.PKCS8, encryption_algorithm=serialization.NoEncryption()))
        f.write(certificate.public_bytes(serialization.Encoding.PEM))
    
    with open(roblox_ca, "w") as f:
        f.write("MITMPROXY TRUSTED ROOT\n=========================\n")
        f.write(certificate.public_bytes(serialization.Encoding.PEM).decode('utf-8'))

def add_cert_to_roblox():
    paths = [
        # Add more bootstrapper paths for compatibility
        Path.home() / "AppData/Local/Fishstrap/Versions",
        Path.home() / "AppData/Local/Roblox/Versions",
        Path.home() / "AppData/Local/Bloxstrap/Versions",
        Path.home() / "AppData/Local/Frosttrap/Versions",
        Path.home() / "AppData/Local/Voidstrap/Versions",
    ]
    found = False
    
    for folder_path in paths:
        if not folder_path.exists():
            continue
            
        subdirectories = [d for d in folder_path.iterdir() if d.is_dir()]
        if not subdirectories:
            continue
        
        for version_folder in subdirectories:
            cacert_path = version_folder / "ssl" / "cacert.pem"
            
            if cacert_path.exists():
                found = True
                update_cacert(cacert_path)
    
    if not found:
        print("Warning: Could not find Roblox installation")

def update_cacert(cacert_path):
    with open(cacert_path, "r") as f:
        original_ca = f.read()
    
    if "MITMPROXY TRUSTED ROOT" in original_ca:
        original_ca = original_ca.split("MITMPROXY TRUSTED ROOT")[0]
    
    with open(roblox_ca, "r") as f:
        mitm_ca = f.read()
    
    with open(cacert_path, "w") as f:
        f.write(original_ca.strip() + "\n" + mitm_ca)
    
if not mitm_ca.exists():
    generate_ca_files()

add_cert_to_roblox()
