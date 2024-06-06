from hash import *
import argparse
import os, time

def get_params():
    parser = argparse.ArgumentParser()
    algorithms = ["sha1", "sha256", "sha384", "sha512", "sha224", "sha3_224", "sha3_256", "sha3_384", "sha3_512"]
    parser.add_argument("--algorithms", type=str, required=True, choices=algorithms)
    parser.add_argument("--input_path", type=str, default= "input")
    parser.add_argument("--output_path", type= str, default= "output")
    parser.add_argument("--input_file", type= str, default="fox.txt")
    parser.add_argument("--output_file", type= str, default="output.txt")
    parser.add_argument("--text", type=str, default=None)
    parser.add_argument("--timed", action= "store_true")
    
    return parser.parse_args()

def get_file(path, name):
    return os.path.join(path, name)

def check_path(path):
    if not os.path.exists(path):
        os.mkdir(path)

def main():
    p = get_params()
    if p.text is not None:
        message = p.text
    else:
        check_path(p.input_path)
        with open(get_file(p.input_path, p.input_file), "r") as f:
            message = f.read()
    
    start_time = time.perf_counter()
    encrypt = 0
    match p.algorithms:
        case "sha1": 
            encrypt = sha1().digest(message)
        case "sha256": 
            encrypt = sha256().digest(message)
        case "sha512": 
            encrypt = sha512().digest(message)
        case "sha224": 
            encrypt = sha224().digest(message)
        case "sha384": 
            encrypt = sha384().digest(message)
        case "sha3_224": 
            encrypt = sha3_224().digest(message)
        case "sha3_256": 
            encrypt = sha3_256().digest(message)
        case "sha3_384": 
            encrypt = sha3_384().digest(message)
        case "sha3_512": 
            encrypt = sha3_512().digest(message)
    end_time = time.perf_counter()

    check_path(p.output_path)
    with open(get_file(p.output_path, p.output_file), 'w') as file:
        file.write(f'{encrypt}\n')
        
    print(f'Input: {message}')
    print(f'Output: {encrypt}')
    print(f'Result has been saved to {p.output_path}/{p.output_file}')
    if p.timed:
        elapsed_time = end_time - start_time
        print(f'Time: {elapsed_time}')

if __name__ == "__main__":
    main()