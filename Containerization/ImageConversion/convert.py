#!/usr/bin/env python3

import argparse
from os import PathLike
from PIL import Image


def convert(input_image: str|PathLike, output_image: str|PathLike, mode: str = "L") -> None:
    """
    Convert an image from its current mode to another and save it out

    :param input_image: input image
    :param output_image: output image
    :param mode: PIL Convert Mode
    :return: None
    """
    img = Image.open(input_image)
    img = img.convert(mode)
    img.save(output_image)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("input_image", help="input image")
    parser.add_argument("output_image", help="output image")
    parser.add_argument("mode", help="PIL Convert Mode")
    args = parser.parse_args()

    convert(args.input_image, args.output_image, args.mode)
