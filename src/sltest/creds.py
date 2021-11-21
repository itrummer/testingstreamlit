'''
Created on Nov 20, 2021

@author: immanueltrummer
'''
import argparse
import json
import toml

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('in_path', type=str, help='Input path (firebase credentials)')
    parser.add_argument('ai_key', type=str, help='Key for OpenAI access')
    parser.add_argument('out_path', type=str, help='Output path (.toml secrets)')
    args = parser.parse_args()
    
    with open(args.in_path) as in_file:
        fb_creds = json.load(in_file)
        secrets = {}
        secrets['firebase'] = fb_creds
        secrets['openai'] = args.ai_key
        with open(args.out_path, 'w') as out_file:
            toml.dump(secrets, out_file)
        with open(args.out_path) as out_file:
            toml_file = toml.load(out_file)
            print(toml_file)