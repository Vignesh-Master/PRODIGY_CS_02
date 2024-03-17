from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image


key = b'This is a 16 byte key'[:16]  

def encrypt_image(image_path, key):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(image_path, 'rb') as f:
        img_bytes = bytearray(f.read())
    
    padded_data = pad(img_bytes, AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    
    with open('encrypted_image.png', 'wb') as f:
        f.write(encrypted_data)

def decrypt_image(encrypted_image_path, key):
    cipher = AES.new(key, AES.MODE_ECB)
    with open(encrypted_image_path, 'rb') as f:
        encrypted_data = bytearray(f.read())
    
    decrypted_data = unpad(cipher.decrypt(encrypted_data), AES.block_size)
    
    with open('decrypted_image.png', 'wb') as f:
        f.write(decrypted_data)


while True:
    print("Choose an option:")
    print("1. Encrypt Image")
    print("2. Decrypt Image")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        image_path = input("Enter the path to the image you want to encrypt: ")
        encrypt_image(image_path, key)
        print("Image encrypted successfully!")
    elif choice == '2':
        encrypted_image_path = input("Enter the path to the encrypted image: ")
        decrypt_image(encrypted_image_path, key)
        print("Image decrypted successfully!")
    elif choice == '3':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please enter a valid option.")
