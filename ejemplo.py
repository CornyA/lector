#!/usr/bin/python3
import argparse

def main(nombres):
    for nombre in nombres:
        print(nombre)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-n","--nombre",dest = "nombres", help="Nombre de personas", action = "append", required=True)
    args = parser.parse_args()
    nombres = args.nombres
    main(nombres)

