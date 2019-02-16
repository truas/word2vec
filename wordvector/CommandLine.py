import argparse


class CLWord2Vec:
    input_folder = None
    output_arff = None
    model_folder = None
    aggregator = "mean"
    isBin = False
    noHeader = False
    preprocess = False

    def __init__(self):
        parser = self.define_parser_parameters()
        args = parser.parse_args()

        self.input_folder = args.inf
        self.output_arff = args.ouf
        self.aggregator = args.agg
        self.model_folder = args.mod
        self.type = args.type
        self.noHeader = args.nohe
        self.preprocess = args.pre

    def define_parser_parameters(self):
        parser = argparse.ArgumentParser(description="main - convert raw dataset into arff with word2vec features")
        parser.add_argument('--input', type=str, action='store', dest='inf', metavar='<folder>', required=True,
                            help='relative path from your current folder to the destination document folders')
        parser.add_argument('--output', type=str, action='store', dest='ouf', metavar='<file>', required=True,
                            help='name of the arff file')
        parser.add_argument('--model', type=str, action='store', dest='mod', metavar='<folder>', required=True,
                            help='trained word embeddings model')
        parser.add_argument('--aggregator', type=str, action='store', dest='agg', metavar='<value>', required=False,
                            help='type of aggregator to use', choices=["sum", "mean"], default="mean")
        parser.add_argument('--type', type=str, action='store', dest='type', metavar='<value>', required=True,
                            help='select the type of model to load', choices=["model", "bin", "txt"], default=False)
        parser.add_argument('--noheader', type=bool, action='store', dest='nohe', metavar='<value>', required=False,
                            help='set True to remove the arff header', default=False)
        parser.add_argument('--preprocess', type=bool, action='store', dest='pre', metavar='<value>', required=False,
                            help='set True to apply word tokenization otherwise it will assume each row has one word',
                            default=False)
        return parser
