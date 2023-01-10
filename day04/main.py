import hashlib

not_found = True
secret_key = "bgvyzdsv"
number_to_add = 0

while not_found:
    number_to_add += 1
    addition = str(number_to_add)
    key = secret_key + addition
    hash = hashlib.md5(key.encode("utf-8")).hexdigest()
    if hash[:6] == "000000":
        not_found = False
        print(f"The number to add to the secret key is: {number_to_add}")
