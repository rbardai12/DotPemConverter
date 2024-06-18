import re

og = r'windows/this/that/thecert.crt'
output3 = og
output3 = re.sub('.crt', '', output3)
codecontent3 = f'x509 -inform DER -outform PEM -in "{og}" -out "{output3}.pem"'

print(codecontent3)