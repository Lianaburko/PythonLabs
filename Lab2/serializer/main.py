import argparse
import serializer.factory

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Serializer to json, toml, yaml')
    parser.add_argument('indir', type=str, help='Input dir for serialization')
    parser.add_argument('begin_format', type=str, help='Serialize format of doc')
    parser.add_argument('result_format', type=str, help='Serialize format to result')
    parser.add_argument('outdir', type=str, help='Output dir for deserialization')
    args = parser.parse_args()

    begin_format = args.begin_format
    result_format = args.result_format

    if begin_format == result_format:
        print("Same type of objects")
        exit()

    begin_format = serializer.factory.Factory.create_serializer(begin_format)
    result_format = serializer.factory.Factory.create_serializer(result_format)

    with open(args.indir) as file:
        obj = begin_format.load(file)
        with open(args.outdir, "w") as output_file:
            result_format.dump(object, output_file)
