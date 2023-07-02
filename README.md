# Caesar Cipher

This is a Python program that implements the Caesar cipher encryption and decryption technique. The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of positions down or up the alphabet.

## Installation

To run this program, make sure you have Python 3 installed on your system. You can download Python from the official website: [Python](python.org).

## Usage

1. Run the program by executing the Python script.
   ```
      python main.py
   ```
3. The program will display a logo and prompt you to choose whether you want to encode or decode a message.
   ```
      Type 'encode' to encrypt, type 'decode' to decrypt:
   ```
5. Enter your message that you want to encrypt or decrypt.
   ```
      Type your message:
   ```
7. Enter the shift number, which determines the number of positions each letter should be shifted in the alphabet.
   ```
      Type the shift number:
   ```
9. The program will display the resulting text after encryption or decryption.
   ```
      The encoded/decoded text is <result>
   ```
11. After displaying the result, the program will ask if you want to restart or exit.
    ```
      Do you want to restart the cipher program? [yes, no]:
    ```
12. If you choose "yes," you can perform another encryption or decryption. If you choose "no," the program will exit.

## Example

Here's an example of how to use the Caesar Cipher program:
```
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP""" """"  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""" """" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88     

Type 'encode' to encrypt, type 'decode' to decrypt:
encode
Type your message:
hello world
Type the shift number:
3
The encoded text is khoor zruog

Do you want to restart the cipher program? [yes, no]:
yes

Type 'encode' to encrypt, type 'decode' to decrypt:
decode
Type your message:
khoor zruog
Type the shift number:
3
The decoded text is hello world

Do you want to restart the cipher program? [yes, no]:
no
Goodbye

```

In this example, the program first encrypts the message "hello world" with a shift of 3, resulting in "khoor zruog". Then it decrypts the encrypted message back to the original text.

Feel free to explore different messages and shift numbers to see the encryption and decryption in action.

## License

This project is licensed under the MIT License. Feel free to use and modify it according to your needs. See the [LICENSE](LICENSE) file for more information.




    
